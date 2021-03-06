#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -fPIC" % crosstools.environment

    crosstools.autoreconf("-vfi")

    cache = [ "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes" ]

    pisitools.dosed("Makefile.in", r"(^AR\s*=).*", "\\1 %(AR)s" % crosstools.environment)
    # do not enable nls http://bugs.gentoo.org/121408
    crosstools.configure("--disable-nls \
                          --disable-dependency-tracking", cache=cache)

def build():
    crosstools.make("-j1")

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("flex", "/usr/bin/lex")

    pisitools.dodoc("NEWS", "README")
