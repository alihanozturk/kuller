#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/doc/%s/source/" % get.srcTAG(),"doc/source/*")
    pisitools.insinto("/usr/share/doc/%s/demo/" % get.srcTAG(),"demo/*")

    pisitools.dodoc("README", "LICENSE", "CHANGES", "doc/*")
