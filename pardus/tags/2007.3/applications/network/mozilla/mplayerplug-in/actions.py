#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mplayerplug-in"

def setup():
    autotools.configure("--enable-gtk2 \
                         --enable-dvx \
                         --enable-gmp \
                         --enable-rm \
                         --enable-qt \
                         --enable-wmp")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/nsbrowser/plugins/", "*.so")
    pisitools.insinto("/usr/lib/nsbrowser/plugins/", "*.xpt")

    pisitools.insinto("/etc", "mplayerplug-in.conf")
    pisitools.insinto("/etc", "mplayerplug-in.types")

    pisitools.dodoc("ChangeLog", "README", "DOCS/tech/*.txt")

    shelltools.cd("po/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

