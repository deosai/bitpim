# THIS FILE IS AUTOMATICALLY GENERATED.  EDIT THE SOURCE FILE NOT THIS ONE

"""Various descriptions of data specific to LG VX9700"""

# groups     - same as VX-8700
# phonebook  - LG Phonebook v1.0 (same as VX-8550)
# schedule   - same as VX-8550
# sms        - same as VX-9700
# memos      - same as VX-8550
# call history - same as VX-9700
from p_lgvx9700 import *

# SMS index files
inbox_index     = "dload/inbox.dat"
outbox_index    = "dload/outbox.dat"
drafts_index    = "dload/drafts.dat"

# Phonebook favorites
favorites_file_name  = "pim/pbFavorite.dat"
NUMFAVORITES=10

class favorite(BaseProtogenClass):
    __fields=['pb_index', 'fav_type']

    def __init__(self, *args, **kwargs):
        dict={}
        # What was supplied to this function
        dict.update(kwargs)
        # Parent constructor
        super(favorite,self).__init__(**dict)
        if self.__class__ is favorite:
            self._update(args,dict)


    def getfields(self):
        return self.__fields


    def _update(self, args, kwargs):
        super(favorite,self)._update(args,kwargs)
        keys=kwargs.keys()
        for key in keys:
            if key in self.__fields:
                setattr(self, key, kwargs[key])
                del kwargs[key]
        # Were any unrecognized kwargs passed in?
        if __debug__:
            self._complainaboutunusedargs(favorite,kwargs)
        if len(args): raise TypeError('Unexpected arguments supplied: '+`args`)
        # Make all P fields that haven't already been constructed


    def writetobuffer(self,buf,autolog=True,logtitle="<written data>"):
        'Writes this packet to the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        try: self.__field_pb_index
        except:
            self.__field_pb_index=UINT(**{'sizeinbytes': 2,  'default': 0xffff })
        self.__field_pb_index.writetobuffer(buf)
        try: self.__field_fav_type
        except:
            self.__field_fav_type=UINT(**{'sizeinbytes': 1,  'default': 0xff })
        self.__field_fav_type.writetobuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologwrite(buf, logtitle=logtitle)


    def readfrombuffer(self,buf,autolog=True,logtitle="<read data>"):
        'Reads this packet from the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologread(buf, logtitle=logtitle)
        self.__field_pb_index=UINT(**{'sizeinbytes': 2,  'default': 0xffff })
        self.__field_pb_index.readfrombuffer(buf)
        self.__field_fav_type=UINT(**{'sizeinbytes': 1,  'default': 0xff })
        self.__field_fav_type.readfrombuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()


    def __getfield_pb_index(self):
        try: self.__field_pb_index
        except:
            self.__field_pb_index=UINT(**{'sizeinbytes': 2,  'default': 0xffff })
        return self.__field_pb_index.getvalue()

    def __setfield_pb_index(self, value):
        if isinstance(value,UINT):
            self.__field_pb_index=value
        else:
            self.__field_pb_index=UINT(value,**{'sizeinbytes': 2,  'default': 0xffff })

    def __delfield_pb_index(self): del self.__field_pb_index

    pb_index=property(__getfield_pb_index, __setfield_pb_index, __delfield_pb_index, None)

    def __getfield_fav_type(self):
        try: self.__field_fav_type
        except:
            self.__field_fav_type=UINT(**{'sizeinbytes': 1,  'default': 0xff })
        return self.__field_fav_type.getvalue()

    def __setfield_fav_type(self, value):
        if isinstance(value,UINT):
            self.__field_fav_type=value
        else:
            self.__field_fav_type=UINT(value,**{'sizeinbytes': 1,  'default': 0xff })

    def __delfield_fav_type(self): del self.__field_fav_type

    fav_type=property(__getfield_fav_type, __setfield_fav_type, __delfield_fav_type, None)

    def iscontainer(self):
        return True

    def containerelements(self):
        yield ('pb_index', self.__field_pb_index, None)
        yield ('fav_type', self.__field_fav_type, None)

    def has_pbentry(self):
        return self.pb_index != 0xffff and self.fav_type == 1




class favorites(BaseProtogenClass):
    __fields=['items']

    def __init__(self, *args, **kwargs):
        dict={}
        # What was supplied to this function
        dict.update(kwargs)
        # Parent constructor
        super(favorites,self).__init__(**dict)
        if self.__class__ is favorites:
            self._update(args,dict)


    def getfields(self):
        return self.__fields


    def _update(self, args, kwargs):
        super(favorites,self)._update(args,kwargs)
        keys=kwargs.keys()
        for key in keys:
            if key in self.__fields:
                setattr(self, key, kwargs[key])
                del kwargs[key]
        # Were any unrecognized kwargs passed in?
        if __debug__:
            self._complainaboutunusedargs(favorites,kwargs)
        if len(args):
            dict2={ 'elementclass': favorite, 'length': NUMFAVORITES }
            dict2.update(kwargs)
            kwargs=dict2
            self.__field_items=LIST(*args,**dict2)
        # Make all P fields that haven't already been constructed


    def writetobuffer(self,buf,autolog=True,logtitle="<written data>"):
        'Writes this packet to the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        try: self.__field_items
        except:
            self.__field_items=LIST(**{ 'elementclass': favorite, 'length': NUMFAVORITES })
        self.__field_items.writetobuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologwrite(buf, logtitle=logtitle)


    def readfrombuffer(self,buf,autolog=True,logtitle="<read data>"):
        'Reads this packet from the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologread(buf, logtitle=logtitle)
        self.__field_items=LIST(**{ 'elementclass': favorite, 'length': NUMFAVORITES })
        self.__field_items.readfrombuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()


    def __getfield_items(self):
        try: self.__field_items
        except:
            self.__field_items=LIST(**{ 'elementclass': favorite, 'length': NUMFAVORITES })
        return self.__field_items.getvalue()

    def __setfield_items(self, value):
        if isinstance(value,LIST):
            self.__field_items=value
        else:
            self.__field_items=LIST(value,**{ 'elementclass': favorite, 'length': NUMFAVORITES })

    def __delfield_items(self): del self.__field_items

    items=property(__getfield_items, __setfield_items, __delfield_items, None)

    def iscontainer(self):
        return True

    def containerelements(self):
        yield ('items', self.__field_items, None)




class call(BaseProtogenClass):
    __fields=['GPStime', 'unk0', 'duration', 'number', 'name', 'numberlength', 'status', 'pbnumbertype', 'unk1', 'pbentrynum', 'unk2']

    def __init__(self, *args, **kwargs):
        dict={}
        # What was supplied to this function
        dict.update(kwargs)
        # Parent constructor
        super(call,self).__init__(**dict)
        if self.__class__ is call:
            self._update(args,dict)


    def getfields(self):
        return self.__fields


    def _update(self, args, kwargs):
        super(call,self)._update(args,kwargs)
        keys=kwargs.keys()
        for key in keys:
            if key in self.__fields:
                setattr(self, key, kwargs[key])
                del kwargs[key]
        # Were any unrecognized kwargs passed in?
        if __debug__:
            self._complainaboutunusedargs(call,kwargs)
        if len(args): raise TypeError('Unexpected arguments supplied: '+`args`)
        # Make all P fields that haven't already been constructed


    def writetobuffer(self,buf,autolog=True,logtitle="<written data>"):
        'Writes this packet to the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        self.__field_GPStime.writetobuffer(buf)
        self.__field_unk0.writetobuffer(buf)
        self.__field_duration.writetobuffer(buf)
        self.__field_number.writetobuffer(buf)
        self.__field_name.writetobuffer(buf)
        self.__field_numberlength.writetobuffer(buf)
        self.__field_status.writetobuffer(buf)
        self.__field_pbnumbertype.writetobuffer(buf)
        self.__field_unk1.writetobuffer(buf)
        self.__field_pbentrynum.writetobuffer(buf)
        self.__field_unk2.writetobuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologwrite(buf, logtitle=logtitle)


    def readfrombuffer(self,buf,autolog=True,logtitle="<read data>"):
        'Reads this packet from the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologread(buf, logtitle=logtitle)
        self.__field_GPStime=GPSDATE(**{'sizeinbytes': 4})
        self.__field_GPStime.readfrombuffer(buf)
        self.__field_unk0=UINT(**{'sizeinbytes': 4})
        self.__field_unk0.readfrombuffer(buf)
        self.__field_duration=UINT(**{'sizeinbytes': 4})
        self.__field_duration.readfrombuffer(buf)
        self.__field_number=USTRING(**{'sizeinbytes': 49, 'raiseonunterminatedread': False})
        self.__field_number.readfrombuffer(buf)
        self.__field_name=USTRING(**{'sizeinbytes': 36, 'encoding': PHONE_ENCODING, 'raiseonunterminatedread': False})
        self.__field_name.readfrombuffer(buf)
        self.__field_numberlength=UINT(**{'sizeinbytes': 1})
        self.__field_numberlength.readfrombuffer(buf)
        self.__field_status=UINT(**{'sizeinbytes': 1})
        self.__field_status.readfrombuffer(buf)
        self.__field_pbnumbertype=UINT(**{'sizeinbytes': 1})
        self.__field_pbnumbertype.readfrombuffer(buf)
        self.__field_unk1=UINT(**{'sizeinbytes': 4})
        self.__field_unk1.readfrombuffer(buf)
        self.__field_pbentrynum=UINT(**{'sizeinbytes': 2})
        self.__field_pbentrynum.readfrombuffer(buf)
        self.__field_unk2=DATA(**{'sizeinbytes': 27})
        self.__field_unk2.readfrombuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()


    def __getfield_GPStime(self):
        return self.__field_GPStime.getvalue()

    def __setfield_GPStime(self, value):
        if isinstance(value,GPSDATE):
            self.__field_GPStime=value
        else:
            self.__field_GPStime=GPSDATE(value,**{'sizeinbytes': 4})

    def __delfield_GPStime(self): del self.__field_GPStime

    GPStime=property(__getfield_GPStime, __setfield_GPStime, __delfield_GPStime, None)

    def __getfield_unk0(self):
        return self.__field_unk0.getvalue()

    def __setfield_unk0(self, value):
        if isinstance(value,UINT):
            self.__field_unk0=value
        else:
            self.__field_unk0=UINT(value,**{'sizeinbytes': 4})

    def __delfield_unk0(self): del self.__field_unk0

    unk0=property(__getfield_unk0, __setfield_unk0, __delfield_unk0, None)

    def __getfield_duration(self):
        return self.__field_duration.getvalue()

    def __setfield_duration(self, value):
        if isinstance(value,UINT):
            self.__field_duration=value
        else:
            self.__field_duration=UINT(value,**{'sizeinbytes': 4})

    def __delfield_duration(self): del self.__field_duration

    duration=property(__getfield_duration, __setfield_duration, __delfield_duration, None)

    def __getfield_number(self):
        return self.__field_number.getvalue()

    def __setfield_number(self, value):
        if isinstance(value,USTRING):
            self.__field_number=value
        else:
            self.__field_number=USTRING(value,**{'sizeinbytes': 49, 'raiseonunterminatedread': False})

    def __delfield_number(self): del self.__field_number

    number=property(__getfield_number, __setfield_number, __delfield_number, None)

    def __getfield_name(self):
        return self.__field_name.getvalue()

    def __setfield_name(self, value):
        if isinstance(value,USTRING):
            self.__field_name=value
        else:
            self.__field_name=USTRING(value,**{'sizeinbytes': 36, 'encoding': PHONE_ENCODING, 'raiseonunterminatedread': False})

    def __delfield_name(self): del self.__field_name

    name=property(__getfield_name, __setfield_name, __delfield_name, None)

    def __getfield_numberlength(self):
        return self.__field_numberlength.getvalue()

    def __setfield_numberlength(self, value):
        if isinstance(value,UINT):
            self.__field_numberlength=value
        else:
            self.__field_numberlength=UINT(value,**{'sizeinbytes': 1})

    def __delfield_numberlength(self): del self.__field_numberlength

    numberlength=property(__getfield_numberlength, __setfield_numberlength, __delfield_numberlength, None)

    def __getfield_status(self):
        return self.__field_status.getvalue()

    def __setfield_status(self, value):
        if isinstance(value,UINT):
            self.__field_status=value
        else:
            self.__field_status=UINT(value,**{'sizeinbytes': 1})

    def __delfield_status(self): del self.__field_status

    status=property(__getfield_status, __setfield_status, __delfield_status, None)

    def __getfield_pbnumbertype(self):
        return self.__field_pbnumbertype.getvalue()

    def __setfield_pbnumbertype(self, value):
        if isinstance(value,UINT):
            self.__field_pbnumbertype=value
        else:
            self.__field_pbnumbertype=UINT(value,**{'sizeinbytes': 1})

    def __delfield_pbnumbertype(self): del self.__field_pbnumbertype

    pbnumbertype=property(__getfield_pbnumbertype, __setfield_pbnumbertype, __delfield_pbnumbertype, None)

    def __getfield_unk1(self):
        return self.__field_unk1.getvalue()

    def __setfield_unk1(self, value):
        if isinstance(value,UINT):
            self.__field_unk1=value
        else:
            self.__field_unk1=UINT(value,**{'sizeinbytes': 4})

    def __delfield_unk1(self): del self.__field_unk1

    unk1=property(__getfield_unk1, __setfield_unk1, __delfield_unk1, None)

    def __getfield_pbentrynum(self):
        return self.__field_pbentrynum.getvalue()

    def __setfield_pbentrynum(self, value):
        if isinstance(value,UINT):
            self.__field_pbentrynum=value
        else:
            self.__field_pbentrynum=UINT(value,**{'sizeinbytes': 2})

    def __delfield_pbentrynum(self): del self.__field_pbentrynum

    pbentrynum=property(__getfield_pbentrynum, __setfield_pbentrynum, __delfield_pbentrynum, None)

    def __getfield_unk2(self):
        return self.__field_unk2.getvalue()

    def __setfield_unk2(self, value):
        if isinstance(value,DATA):
            self.__field_unk2=value
        else:
            self.__field_unk2=DATA(value,**{'sizeinbytes': 27})

    def __delfield_unk2(self): del self.__field_unk2

    unk2=property(__getfield_unk2, __setfield_unk2, __delfield_unk2, None)

    def iscontainer(self):
        return True

    def containerelements(self):
        yield ('GPStime', self.__field_GPStime, None)
        yield ('unk0', self.__field_unk0, None)
        yield ('duration', self.__field_duration, None)
        yield ('number', self.__field_number, None)
        yield ('name', self.__field_name, None)
        yield ('numberlength', self.__field_numberlength, None)
        yield ('status', self.__field_status, None)
        yield ('pbnumbertype', self.__field_pbnumbertype, None)
        yield ('unk1', self.__field_unk1, None)
        yield ('pbentrynum', self.__field_pbentrynum, None)
        yield ('unk2', self.__field_unk2, None)




class callhistory(BaseProtogenClass):
    __fields=['numcalls', 'unk1', 'calls']

    def __init__(self, *args, **kwargs):
        dict={}
        # What was supplied to this function
        dict.update(kwargs)
        # Parent constructor
        super(callhistory,self).__init__(**dict)
        if self.__class__ is callhistory:
            self._update(args,dict)


    def getfields(self):
        return self.__fields


    def _update(self, args, kwargs):
        super(callhistory,self)._update(args,kwargs)
        keys=kwargs.keys()
        for key in keys:
            if key in self.__fields:
                setattr(self, key, kwargs[key])
                del kwargs[key]
        # Were any unrecognized kwargs passed in?
        if __debug__:
            self._complainaboutunusedargs(callhistory,kwargs)
        if len(args): raise TypeError('Unexpected arguments supplied: '+`args`)
        # Make all P fields that haven't already been constructed


    def writetobuffer(self,buf,autolog=True,logtitle="<written data>"):
        'Writes this packet to the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        self.__field_numcalls.writetobuffer(buf)
        self.__field_unk1.writetobuffer(buf)
        try: self.__field_calls
        except:
            self.__field_calls=LIST(**{'elementclass': call})
        self.__field_calls.writetobuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologwrite(buf, logtitle=logtitle)


    def readfrombuffer(self,buf,autolog=True,logtitle="<read data>"):
        'Reads this packet from the supplied buffer'
        self._bufferstartoffset=buf.getcurrentoffset()
        if autolog and self._bufferstartoffset==0: self.autologread(buf, logtitle=logtitle)
        self.__field_numcalls=UINT(**{'sizeinbytes': 4})
        self.__field_numcalls.readfrombuffer(buf)
        self.__field_unk1=UINT(**{'sizeinbytes': 1})
        self.__field_unk1.readfrombuffer(buf)
        self.__field_calls=LIST(**{'elementclass': call})
        self.__field_calls.readfrombuffer(buf)
        self._bufferendoffset=buf.getcurrentoffset()


    def __getfield_numcalls(self):
        return self.__field_numcalls.getvalue()

    def __setfield_numcalls(self, value):
        if isinstance(value,UINT):
            self.__field_numcalls=value
        else:
            self.__field_numcalls=UINT(value,**{'sizeinbytes': 4})

    def __delfield_numcalls(self): del self.__field_numcalls

    numcalls=property(__getfield_numcalls, __setfield_numcalls, __delfield_numcalls, None)

    def __getfield_unk1(self):
        return self.__field_unk1.getvalue()

    def __setfield_unk1(self, value):
        if isinstance(value,UINT):
            self.__field_unk1=value
        else:
            self.__field_unk1=UINT(value,**{'sizeinbytes': 1})

    def __delfield_unk1(self): del self.__field_unk1

    unk1=property(__getfield_unk1, __setfield_unk1, __delfield_unk1, None)

    def __getfield_calls(self):
        try: self.__field_calls
        except:
            self.__field_calls=LIST(**{'elementclass': call})
        return self.__field_calls.getvalue()

    def __setfield_calls(self, value):
        if isinstance(value,LIST):
            self.__field_calls=value
        else:
            self.__field_calls=LIST(value,**{'elementclass': call})

    def __delfield_calls(self): del self.__field_calls

    calls=property(__getfield_calls, __setfield_calls, __delfield_calls, None)

    def iscontainer(self):
        return True

    def containerelements(self):
        yield ('numcalls', self.__field_numcalls, None)
        yield ('unk1', self.__field_unk1, None)
        yield ('calls', self.__field_calls, None)




