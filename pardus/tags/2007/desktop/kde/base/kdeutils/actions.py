#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("DO_NOT_COMPILE", "kregexpeditor kedit kdessh klaptopdaemon")
    kde.configure("--without-snmp \
                   --without-xmms")

def build():
    kde.make()
    
def install():
    kde.install()

    pisitools.remove("/usr/kde/3.5/share/applications/kde/kwalletmanager.desktop")

    # Remove khexeditpart because it associates itself with application/octet-stream breaking things all around
    pisitools.remove("/usr/kde/3.5/lib/kde3/libkhexedit2part.*")
    pisitools.remove("/usr/kde/3.5/share/services/khexedit2part.desktop")
    pisitools.removeDir("/usr/kde/3.5/share/apps/khexedit2part")
