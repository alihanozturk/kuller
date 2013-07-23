#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"

    if os.path.exists(enabledPackage) and file(enabledPackage).read() == "nvidia-drivers":
        call("nvidia_drivers", "Xorg.Driver", "enable")