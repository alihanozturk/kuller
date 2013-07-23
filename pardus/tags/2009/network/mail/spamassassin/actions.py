#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Mail-SpamAssassin-%s" % get.srcVERSION()

def setup():
    perlmodules.configure('/usr BUILD_SPAMC="yes" ENABLE_SSL="yes" CONTACT_ADDRESS="root@localhost"')

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    perlmodules.fixLocalPod()

    pisitools.dodoc("README", "MANIFEST", "Changes")
    pisitools.dodir("/var/lib/spamd")