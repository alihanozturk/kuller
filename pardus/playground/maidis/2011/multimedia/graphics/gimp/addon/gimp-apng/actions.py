#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure()

def build():
    autotools.make()

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "src/file-apng")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "HACKING", "NEWS", "README", "TODO")