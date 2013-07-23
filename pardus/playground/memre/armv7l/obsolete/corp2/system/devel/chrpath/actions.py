#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.autoreconf("-fi")
    crosstools.configure(cleanFlags=True)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    # FIXME: something fishy is going on, farm borks with this
    # pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))