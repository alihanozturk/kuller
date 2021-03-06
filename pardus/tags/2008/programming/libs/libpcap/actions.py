#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-ipv6")

def build():
    autotools.make("shared")

def install():
    autotools.install()

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dolib_so("libpcap.so.%s" % get.srcVERSION())
    pisitools.dosym("libpcap.so.%s" % get.srcVERSION(), "/usr/lib/libpcap.so")

    pisitools.dodoc("CHANGES", "CREDITS", "README", "README.linux", "TODO", "doc/pcap.txt")
