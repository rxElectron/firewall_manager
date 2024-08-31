# firewall.py

import os

def run_command(command):
    """Run a command with sudo privileges."""
    try:
        os.system(f"sudo {command}")
    except Exception as e:
        raise RuntimeError(f"Error executing command: {str(e)}")

def open_ports(ports):
    """Open specified ports."""
    for port in ports:
        run_command(f"ufw allow {port}/tcp")
    run_command("ufw reload")

def close_ports(ports):
    """Close specified ports."""
    for port in ports:
        run_command(f"ufw deny {port}/tcp")
    run_command("ufw reload")

def block_ip(ip):
    """Block a specific IP address."""
    run_command(f"ufw deny from {ip}")
    run_command("ufw reload")

def unblock_ip(ip):
    """Unblock a specific IP address."""
    run_command(f"ufw delete deny from {ip}")
    run_command("ufw reload")

def list_rules():
    """List all UFW rules."""
    return os.popen("sudo ufw status numbered").read()

def reset_ufw():
    """Reset UFW to default settings."""
    run_command("ufw reset")
    run_command("ufw default deny incoming")
    run_command("ufw default allow outgoing")
    run_command("ufw reload")

def backup_current_rules(backup_path):
    """Backup current UFW rules to a file."""
    run_command(f"ufw status > {backup_path}")

def restore_rules(backup_path):
    """Restore UFW rules from a backup file."""
    run_command("ufw reset")
    with open(backup_path, 'r') as file:
        rules = file.readlines()
    for rule in rules:
        run_command(rule.strip())
    run_command("ufw reload")
