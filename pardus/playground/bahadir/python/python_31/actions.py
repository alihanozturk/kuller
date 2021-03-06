#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Python-%s" % get.srcVERSION()

def setup():
    shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    # FIXME: caglar10ur
    pisitools.remove("/usr/bin/2to3")
    pisitools.removeDir("/usr/lib/python3.1/idlelib")
    pisitools.remove("/usr/lib/python3.1/lib-dynload/_tkinter.so")

    pisitools.dodoc("LICENSE", "README")
