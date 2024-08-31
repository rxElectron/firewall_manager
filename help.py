# help.py

import tkinter as tk
from tkinter import messagebox

def show_help():
    """Display help documentation."""
    help_text = """
Firewall Manager Help

Features:
- Open and close FTP and SSH ports.
- Block and unblock specific IP addresses.
- Save and load custom firewall configurations.
- Backup and restore UFW settings.

For Arch Linux Users:
- Ensure UFW is installed: sudo pacman -S ufw
- Enable UFW: sudo systemctl enable ufw
- Start UFW: sudo systemctl start ufw
- Check UFW status: sudo systemctl status ufw

For more information, visit: https://wiki.archlinux.org/title/UFW
"""
    messagebox.showinfo("Help", help_text)
