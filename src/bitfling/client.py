### BITPIM
###
### Copyright (C) 2004 Roger Binns <rogerb@rogerbinns.com>
###
### This program is free software; you can redistribute it and/or modify
### it under the terms of the BitPim license as detailed in the LICENSE file.
###
### $Id$

"""Code if you want to be a client of BitFling"""

# Currently this file does nothing except some imports.  That
# is to help test the installer generators etc

import xmlrpcstuff

class client:
    "A BitFling client"

    # although we could just inherit straight from
    # ServerProxy, this code is here to help ensure
    # calling convention, and in the future deal with
    # backwards compatibility issues
    
    def __init__(self, url):
        "The URL should include username and password if any"
        self.server=xmlrpcstuff.ServerProxy(url)

    def getversion(self):
        return self.server.getversion()
    
