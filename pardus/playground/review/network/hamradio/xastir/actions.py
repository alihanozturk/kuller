#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-ax25 \
                         --with-geotiff=/usr/include/libgeotiff \
                         --with-graphicsmagick \
                         --without-imagemagick")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "COPYING.LIB.LESSTIF", "ChangeLog", "DEBUG_LEVELS", "FAQ", "LICENSE", "NEWS", "README", "README.CVS", "README.Contributing", "README.Getting-Started", "README.MAPS", "UPGRADE")

    # do not include INSTALL file.
    pisitools.remove("/usr/share/doc/xastir/INSTALL")