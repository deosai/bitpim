### BITPIM
###
### Copyright (C) 2004 Roger Binns <rogerb@rogerbinns.com>
###
### This program is free software; you can redistribute it and/or modify
### it under the terms of the BitPim license as detailed in the LICENSE file.
###
### $Id$

"""Communicate with the Audiovox CDM 8900 cell phone"""

# standard modules
import sha

# our modules
import common
import com_phone
import com_brew
import prototypes
import p_audiovoxcdm8900

class Phone(com_phone.Phone, com_brew.BrewProtocol):
    "Talk to Audiovox CDM 8900 cell phone"

    desc="Audiovox CDM8900"
    protocolclass=p_audiovoxcdm8900
    serialsname='audiovoxcdm8900'
    pbterminator="~"  # packet terminator
    
    def __init__(self, logtarget, commport):
        "Calls all the constructors and sets initial modes"
        com_phone.Phone.__init__(self, logtarget, commport)
	com_brew.BrewProtocol.__init__(self)
        self.log("Attempting to contact phone")
        self.mode=self.MODENONE

    def getfundamentals(self, results):
        """Gets information fundamental to interopating with the phone and UI.

        Currently this is:

          - 'uniqueserial'     a unique serial number representing the phone
          - 'groups'           the phonebook groups
          - 'wallpaper-index'  map index numbers to names
          - 'ringtone-index'   map index numbers to ringtone names

        This method is called before we read the phonebook data or before we
        write phonebook data.
        """
        # use a hash of ESN and other stuff (being paranoid)
        self.log("Retrieving fundamental phone information")
        self.log("Phone serial number")
        results['uniqueserial']=sha.new(self.getfilecontents("nvm/$SYS.ESN")).hexdigest()
        
        # now read groups
        self.log("Reading group information")
        groups={}
        for i in range(self.protocolclass._NUMGROUPS):
            req=self.protocolclass.readgroupentryrequest()
            req.number=i
            res=self.sendpbcommand(req, self.protocolclass.readgroupentryresponse)
            if res.number==self.protocolclass._ALLGROUP:
                continue  # ignore the "All" group
            if len(res.name)==0:
                continue  # must be non-blank name
            groups[i]={'name': res.name}

        results['groups']=groups

        self.log("Fundamentals retrieved")
        return results

    def getcalendar(self, result):
        raise NotImplementedError()

    def getwallpapers(self, result):
        raise NotImplementedError()

    def getringtones(self, result):
        raise NotImplementedError()

    def getphonebook(self, result):
        """Reads the phonebook data.  The L{getfundamentals} information will
        already be in result."""
        pbook={}
        req=self.protocolclass.readpbslotsrequest()
        res=self.sendpbcommand(req, self.protocolclass.readpbslotsresponse)
        slots=[x for x in range(len(res.present)) if ord(res.present[x])]
        numentries=len(slots)
        for i in range(numentries):
            req=self.protocolclass.readpbentryrequest()
            req.slotnumber=slots[i]
            res=self.sendpbcommand(req, self.protocolclass.readpbentryresponse)
            self.log("Read entry "+`i`+" - "+res.entry.name)
            self.progress(i, numentries, res.entry.name)
            entry=self.extractphonebookentry(res.entry, result)
            pbook[i]=entry
            self.progress(i, numentries, res.entry.name)
        self.progress(numentries, numentries, "Phone book read completed")
        result['phonebook']=pbook

        for i in range(0x1e):
            req=self.protocolclass.dunnorequest()
            req.which=i
            self.sendpbcommand(req, self.protocolclass.dunnoresponse)
        
        return pbook

    def extractphonebookentry(self, entry, result):
        """Return a phonebook entry in BitPim format.  This is called from getphonebook."""
        res={}
        # res['serials']=[ {'sourcetype': self.serialsname, 'serial1': entry.serial1, 'serial2': entry.serial2,
        #                  'sourceuniqueid': fundamentals['uniqueserial']} ]
        # numbers
        numbers=[]
        for t, v in ( ('cell', entry.mobile), ('home', entry.home), ('office', entry.office),
                      ('pager', entry.pager), ('fax', entry.fax) ):
            if len(v)==0:
                continue
            numbers.append( {'number': v, 'type': t} )
        if len(numbers):
            res['numbers']=numbers
        # name
        if len(entry.name): # yes, the audiovox can have a blank name!
            res['names']=[{'full': entry.name}]
        # emails (we treat wireless as email addr)
        emails=[]
        if len(entry.email):
            emails.append({'email': entry.email})
        if len(entry.wireless):
            emails.append({'email': entry.wireless})
        if len(emails):
            res['emails']=emails
        # memo
        if len(entry.memo):
            res['memos']=[{'memo': entry.memo}]
        # secret
        if entry.secret:
            res['flags']=[{'secret': True}]
        # group
        if entry.group in result['groups']:
            res['categories']=[{'category': result['groups'][entry.group]['name']}]
        # media
        rt=[]
        if entry.ringtone!=0xffff:
            rt.append({'ringtone': 'avox '+`entry.ringtone`, 'use': 'call'})
        if entry.msgringtone!=0xffff:
            rt.append({'ringtone': 'avox '+`entry.msgringtone`, 'use': 'message'})
        if len(rt):
            res['ringtones']=rt
        if entry.wallpaper!=0xffff:
            res['wallpapers']=[{'wallpaper': 'avox '+`entry.wallpaper`, 'use': 'call'}]
        return res

    def makephonebookentry(self, fields):
        e=self.protocolclass.pbentry()
        # some defaults
        e.secret=0
        e.group=0xff
        e.previous=0xffff
        e.next=0xffff
        e.ringtone=0xffff
        e.msgringtone=0xffff
        e.wallpaper=0xffff
        for f in fields:
            setattr(e, f, fields[f])
        return e

    def savephonebook(self, data):
        self.log("New phonebook\n"+common.prettyprintdict(data['phonebook']))

        pb=data['phonebook']
        keys=pb.keys()
        keys.sort()
        keys=keys[:self.protocolclass._NUMSLOTS]
        # work out the bitmap.  note mild abuse of python booleans
        slots=[]
        for i in range(self.protocolclass._NUMSLOTS):
            if i not in keys:
                slots.append(0)
                continue
            bmp=0
            e=pb[i]
            if len(e['mobile']): bmp|=1
            if len(e['home']):   bmp|=2
            if len(e['office']): bmp|=4
            if len(e['pager']):   bmp|=8
            if len(e['fax']):   bmp|=16
            if len(e['email']):   bmp|=32
            if len(e['wireless']):   bmp|=64
            slots.append(bmp)
        slots="".join([chr(x) for x in slots])
        req=self.protocolclass.writepbslotsrequest()
        req.present=slots
        self.sendpbcommand(req, self.protocolclass.writepbslotsresponse)
        # now write out each slot
        for i in range(len(keys)):
            slot=keys[i]
            req=self.protocolclass.writepbentryrequest()
            req.slotnumber=slot
            req.entry=self.makephonebookentry(pb[slot])
            self.log('Writing entry '+`slot`+" - "+req.entry.name)
            self.progress(i, len(keys), "Writing "+req.entry.name)
            self.sendpbcommand(req, self.protocolclass.writepbentryresponse)
        self.progress(len(keys)+1, len(keys)+1, "Phone book write completed")
        
    
    def sendpbcommand(self, request, responseclass):
        self.setmode(self.MODEBREW)
        buffer=prototypes.buffer()
        request.writetobuffer(buffer)
        data=buffer.getvalue()
        self.logdata("audiovox cdm8900 phonebook request", data, request)
        data=com_brew.escape(data+com_brew.crcs(data))+self.pbterminator
        first=data[0]
        try:
            data=self.comm.writethenreaduntil(data, False, self.pbterminator, logreaduntilsuccess=False)
        except com_phone.modeignoreerrortypes:
            self.mode=self.MODENONE
            self.raisecommsdnaexception("manipulating the phonebook")
        self.comm.success=True

        origdata=data
        # sometimes there is junk at the begining, eg if the user
        # turned off the phone and back on again.  So if there is more
        # than one 7e in the escaped data we should start after the
        # second to last one
        d=data.rfind(self.pbterminator,0,-1)
        if d>=0:
            self.log("Multiple PB packets in data - taking last one starting at "+`d+1`)
            self.logdata("Original pb data", origdata, None)
            data=data[d+1:]

        # turn it back to normal
        data=com_brew.unescape(data)

        # sometimes there is other crap at the begining
        d=data.find(first)
        if d>0:
            self.log("Junk at begining of pb packet, data at "+`d`)
            self.logdata("Original pb data", origdata, None)
            self.logdata("Working on pb data", data, None)
            data=data[d:]
        # take off crc and terminator
        crc=data[-3:-1]
        data=data[:-3]
        if com_brew.crcs(data)!=crc:
            self.logdata("Original pb data", origdata, None)
            self.logdata("Working on pb data", data, None)
            raise common.CommsDataCorruption("Audiovox phonebook packet failed CRC check", self.desc)
        
        # log it
        self.logdata("Audiovox phonebook response", data, responseclass)

        # parse data
        buffer=prototypes.buffer(data)
        res=responseclass()
        res.readfrombuffer(buffer)
        return res
        
class Profile(com_phone.Profile):

    protocolclass=p_audiovoxcdm8900

    WALLPAPER_WIDTH=128
    WALLPAPER_HEIGHT=145
    WALLPAPER_CONVERT_FORMAT="jpg"

    MAX_WALLPAPER_BASENAME_LENGTH=16
    WALLPAPER_FILENAME_CHARS="abcdefghijklmnopqrstuvwyz0123456789 "
    
    MAX_RINGTONE_BASENAME_LENGTH=16
    RINGTONE_FILENAME_CHARS="abcdefghijklmnopqrstuvwyz0123456789 "

    # which usb ids correspond to us
    usbids=( (0x106c, 0x2101, 1), # VID=Curitel, PID=Audiovox CDM 8900, internal modem interface
        )
    # which device classes we are.
    deviceclasses=("modem",)

    # what types of syncing we support
    _supportedsyncs=(
        ('phonebook', 'read', None),         # all phonebook reading
        ('phonebook', 'write', 'OVERWRITE'), # phonebook overwrite only
        )

    def convertphonebooktophone(self, helper, data):
        """Converts the data to what will be used by the phone

        @param data: contains the dict returned by getfundamentals
                 as well as where the results go"""
        
        results={}
        for pbentry in data['phonebook']:
            try:
                e={} # entry out
                entry=data['phonebook'][pbentry]
                e['name']=helper.getfullname(entry.get('names', [ {'full': ''}]), 1, 1, self.protocolclass._MAXNAMELEN)[0]
                e['group']=0xff
                e['mobile']=helper.getnumber(entry.get('numbers', []), 'cell')
                e['home']=helper.getnumber(entry.get('numbers', []), 'home')
                e['office']=helper.getnumber(entry.get('numbers', []), 'office')
                e['pager']=helper.getnumber(entry.get('numbers', []), 'pager')
                e['fax']=helper.getnumber(entry.get('numbers', []), 'fax')
                emails=helper.getemails(entry.get('emails', []), 0, 2, self.protocolclass._MAXEMAILLEN)
                e['email']=""
                e['wireless']=""
                if len(emails)>=1:
                    e['email']=emails[0]
                    if len(emails)>=2:
                        e['wireless']=emails[1]
                e['memo']=helper.getmemos(entry.get('memos', [{'memo': ''}]), 1,1, self.protocolclass._MAXMEMOLEN)[0]
                for i in range(1000):
                    if i not in results:
                        results[i]=e
                        break
            except helper.ConversionFailed:
                continue
        data['phonebook']=results
        return data
    
