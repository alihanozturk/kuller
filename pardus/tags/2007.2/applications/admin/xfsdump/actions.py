#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.autoconf()
    autotools.configure("--libdir=/lib \
                         --libexecdir=/usr/lib \
                         --sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=\"%s\"" % get.installDIR())
