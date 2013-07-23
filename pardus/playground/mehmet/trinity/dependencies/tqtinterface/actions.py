#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde

WorkDir = "dependencies/%s" % get.srcNAME()
def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure(" --bindir=/usr/bin \
                    --libdir=/usr/lib \
                    --includedir=/usr/include")

def build():
    kde.make()

def install():
    kde.install()
    # !!!
    pisitools.removeDir("en")