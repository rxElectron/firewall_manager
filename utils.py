# utils.py

import os
import platform

def ensure_dir_exists(directory):
    """Ensure a directory exists, create it if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def is_arch_linux():
    """Check if the system is running Arch Linux."""
    return platform.system() == "Linux" and os.path.exists("/etc/arch-release")
