### BITPIM
###
### Copyright (C) 2003 Stephen Wood <sawecw@users.sf.net>
###
### This software is under the Artistic license.
### Please see the accompanying LICENSE file
###
### $Id$

"""Talk to the Sanyo SCP-4900 cell phone"""

# my modules
import common
import p_sanyo4900
import com_brew
import com_phone
import com_sanyo
import prototypes


class Phone(com_phone.Phone,com_brew.BrewProtocol,com_sanyo.SanyoPhonebook):
    "Talk to the Sanyo SCP-4900 cell phone"
    desc="SCP-4900"

    protocolclass=p_sanyo4900
    serialsname='scp4900'
    
    def __init__(self, logtarget, commport):
        com_sanyo.SanyoPhonebook.__init__(self, logtarget, commport)
        self.log("Attempting to contact phone")
        self.mode=self.MODENONE


class Profile(com_sanyo.Profile):

    serialsname='scp4900'

    def __init__(self):
        com_sanyo.Profile.__init__(self)
