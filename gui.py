# gui.py

import tkinter as tk
from tkinter import messagebox, filedialog
from firewall import *
from config_manager import *

def create_gui():
    """Create the main GUI window."""
    root = tk.Tk()
    root.title("Firewall Manager")

    # Open Ports
    open_button = tk.Button(root, text="Open FTP and SSH Ports", command=lambda: open_ports([21, 22]))
    open_button.pack(pady=5)

    # Close Ports
    close_button = tk.Button(root, text="Close FTP and SSH Ports", command=lambda: close_ports([21, 22]))
    close_button.pack(pady=5)

    # Block/Unblock IP Entry
    ip_label = tk.Label(root, text="Enter IP Address:")
    ip_label.pack(pady=5)
    ip_entry = tk.Entry(root)
    ip_entry.pack(pady=5)

    # Block IP
    block_button = tk.Button(root, text="Block IP", command=lambda: block_ip(ip_entry.get()))
    block_button.pack(pady=5)

    # Unblock IP
    unblock_button = tk.Button(root, text="Unblock IP", command=lambda: unblock_ip(ip_entry.get()))
    unblock_button.pack(pady=5)

    # List UFW Rules
    list_button = tk.Button(root, text="List UFW Rules", command=lambda: display_rules(root))
    list_button.pack(pady=5)

    # Reset UFW
    reset_button = tk.Button(root, text="Reset UFW", command=reset_ufw)
    reset_button.pack(pady=5)

    # Save Config
    save_button = tk.Button(root, text="Save Config", command=lambda: save_current_config())
    save_button.pack(pady=5)

    # Load Config
    load_button = tk.Button(root, text="Load Config", command=lambda: load_saved_config())
    load_button.pack(pady=5)

    # Backup Config
    backup_button = tk.Button(root, text="Backup Current Config", command=lambda: backup_current_config())
    backup_button.pack(pady=5)

    # Restore Backup
    restore_button = tk.Button(root, text="Restore Backup", command=lambda: restore_backup_prompt())
    restore_button.pack(pady=5)

    # Start the GUI main loop
    root.mainloop()

def display_rules(root):
    """Display current UFW rules in a new window."""
    rules = list_rules()
    rules_window = tk.Toplevel(root)
    rules_window.title("UFW Rules")
    rules_text = tk.Text(rules_window, wrap=tk.WORD)
    rules_text.insert(tk.END, rules)
    rules_text.pack(expand=True, fill=tk.BOTH)

def save_current_config():
    """Save current UFW rules to a configuration file."""
    config_name = filedialog.asksaveasfilename(initialdir=CONFIG_DIR, title="Save Config As", defaultextension=".ufw")
    if config_name:
        rules = list_rules()
        save_config(config_name, rules)
        messagebox.showinfo("Success", "Configuration saved successfully.")

def load_saved_config():
    """Load a saved configuration file."""
    config_path = filedialog.askopenfilename(initialdir=CONFIG_DIR, title="Load Config", filetypes=(("UFW Config Files", "*.ufw"), ("All Files", "*.*")))
    if config_path:
        config_data = load_config(config_path)
        restore_rules(config_data)
        messagebox.showinfo("Success", "Configuration loaded successfully.")

def restore_backup_prompt():
    """Prompt the user to select a backup file to restore."""
    backup_path = filedialog.askopenfilename(initialdir=BACKUP_DIR, title="Select Backup to Restore", filetypes=(("UFW Backup Files", "*.ufw"), ("All Files", "*.*")))
    if backup_path:
        restore_backup(backup_path)
        messagebox.showinfo("Success", "Backup restored successfully.")
