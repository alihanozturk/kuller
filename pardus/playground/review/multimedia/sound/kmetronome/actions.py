#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.unlinkDir("drumstick")
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/kmetronome.png", "/usr/share/pixmaps/kmetronome.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")