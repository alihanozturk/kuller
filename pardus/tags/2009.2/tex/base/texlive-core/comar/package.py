#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/texmf-update")
    os.system("/usr/bin/texconfig font rw")

