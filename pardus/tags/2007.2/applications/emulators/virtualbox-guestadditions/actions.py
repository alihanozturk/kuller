#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="."
NoStrip="/"

def install():
    pisitools.insinto("/usr/share/VirtualBox/additions","VBoxGuestAdditions_%s.iso" % get.srcVERSION(), "VBoxGuestAdditions.iso")