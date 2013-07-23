#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os
import gzip

def mygunzip(_file):
    r_file = gzip.GzipFile(_file, "r")
    write_file = _file.replace(".gz", "")
    w_file = open(write_file, "w")
    w_file.write(r_file.read())
    w_file.close()
    r_file.close()
    os.unlink(_file)

def setup():
    pisitools.dosed("hpssd.py", "/usr/bin/env python", "/usr/bin/python")

    # These are barely the defaults except:
    # --enable-pp-build (default=no)
    # --enable-foomatic-drv-install (default=no) (respected by Fedora, enabled by Ubuntu)
    autotools.configure("--with-cupsbackenddir=/usr/lib/cups/backend \
                         --with-drvdir=/usr/share/cups/drv \
                         --with-hpppddir=/usr/share/cups/model/hplip \
                         --enable-qt4 \
                         --disable-qt3 \
                         --enable-policykit \
                         --enable-pp-build \
                         --enable-doc-build \
                         --enable-fax-build \
                         --enable-gui-build \
                         --enable-dbus-build \
                         --enable-scan-build \
                         --enable-network-build \
                         --enable-hpcups-install \
                         --enable-cups-drv-install \
                         --enable-foomatic-drv-install \
                         --disable-foomatic-ppd-install \
                         --disable-foomatic-rip-hplip-install")
    #--enable-hpijs-install \

    # Remove hardcoded rpaths
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s -j1\
                          ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    # Uncompress ppd files for a better lzma compression (~1.5MB with level -9)
    for ppd in shelltools.ls("%s/usr/share/cups/model/hplip" % get.installDIR()):
        if ppd.endswith(".gz"):
            mygunzip("%s/usr/share/cups/model/hplip/%s" % (get.installDIR(), ppd))

    # Create a compatibility symlink for foomatic-rip-hplip
    pisitools.dosym("/usr/lib/cups/filter/foomatic-rip", "/usr/lib/cups/filter/foomatic-rip-hplip")

    # Remove the hal preprobe rules as they were causing breakage (bug #479648).
    pisitools.removeDir("/usr/share/hal/fdi/preprobe")

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")
    pisitools.removeDir("/etc/udev")