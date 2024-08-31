# config_manager.py

import os
import shutil
from datetime import datetime

CONFIG_DIR = os.path.expanduser("~/firewall_manager/configs/")
BACKUP_DIR = os.path.expanduser("~/firewall_manager/backups/")

def ensure_directories():
    """Ensure necessary directories exist."""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

def save_config(config_name, config_data):
    """Save configuration to a file."""
    ensure_directories()
    config_path = os.path.join(CONFIG_DIR, f"{config_name}.ufw")
    with open(config_path, 'w') as file:
        file.write(config_data)
    return config_path

def load_config(config_name):
    """Load configuration from a file."""
    config_path = os.path.join(CONFIG_DIR, f"{config_name}.ufw")
    with open(config_path, 'r') as file:
        return file.read()

def backup_current_config():
    """Backup current UFW configuration."""
    ensure_directories()
    backup_path = os.path.join(BACKUP_DIR, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.ufw")
    shutil.copyfile("/etc/ufw/ufw.conf", backup_path)
    return backup_path

def restore_backup(backup_path):
    """Restore a backup configuration."""
    shutil.copyfile(backup_path, "/etc/ufw/ufw.conf")
