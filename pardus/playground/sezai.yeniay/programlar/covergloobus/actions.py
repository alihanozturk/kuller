#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()
    
def build():
    autotools.make()
    shelltools.cd("po")
    shelltools.system("msgfmt -cv -o tr.gmo tr.po")

def install():
    autotools.install()
    pisitools.dodoc("README","COPYING","INSTALL")