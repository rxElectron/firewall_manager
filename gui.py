import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from firewall import *
from config_manager import *
from help import show_help
import subprocess
from threading import Thread

class ConsoleRedirector:
    """A class to create a console widget in the GUI for real-time command output."""

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=0, column=1, sticky="nsew")

        self.text_widget = tk.Text(self.frame, wrap=tk.WORD, bg='#2d2d2d', fg='white', state='disabled')
        self.text_widget.pack(expand=True, fill=tk.BOTH)
        
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(self.frame, textvariable=self.input_var)
        self.input_entry.pack(fill=tk.X)
        self.input_entry.bind("<Return>", self.execute_command)

        self.process = None

    def write(self, message):
        self.text_widget.config(state='normal')
        self.text_widget.insert(tk.END, message + "\n")
        self.text_widget.config(state='disabled')
        self.text_widget.see(tk.END)

    def execute_command(self, event):
        command = self.input_var.get()
        self.input_var.set('')
        if command:
            self.write(f"> {command}")
            self.run_command(command)

    def run_command(self, command):
        def target():
            try:
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                self.write(result.stdout)
                self.write(result.stderr)
            except Exception as e:
                self.write(f"Error: {str(e)}")
        
        thread = Thread(target=target)
        thread.start()

def create_gui():
    """Create the main GUI window."""
    root = tk.Tk()
    root.title("Firewall Manager")
    root.geometry("1020x800")
    root.configure(bg='#1c1c1c')  # Darker background for a modern look

    # Set a responsive layout using grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)  # Additional column for console
    root.grid_rowconfigure(0, weight=1)

    # Create a main frame that expands
    main_frame = ttk.Frame(root, padding="15")
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)

    # Create a style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', background='#007acc', foreground='white', font=('Helvetica', 12, 'bold'))
    style.configure('TLabel', background='#1c1c1c', foreground='#e0e0e0', font=('Helvetica', 12))
    style.configure('TEntry', fieldbackground='#3a3a3a', foreground='white', font=('Helvetica', 12))

    # Console Widget
    console = ConsoleRedirector(root)

    # UFW Status
    status_button = ttk.Button(main_frame, text="Check UFW Status", command=lambda: check_ufw_status(root, console))
    status_button.grid(row=0, column=0, pady=(10, 5), sticky="ew")

    # Open Ports
    open_button = ttk.Button(main_frame, text="Open FTP and SSH Ports", command=lambda: open_ports([21, 22]))
    open_button.grid(row=1, column=0, pady=5, sticky="ew")

    # Close Ports
    close_button = ttk.Button(main_frame, text="Close FTP and SSH Ports", command=lambda: close_ports([21, 22]))
    close_button.grid(row=2, column=0, pady=5, sticky="ew")

    # Block/Unblock IP Entry
    ip_label = ttk.Label(main_frame, text="Enter IP Address:")
    ip_label.grid(row=3, column=0, pady=(10, 5), sticky="w")

    ip_entry = ttk.Entry(main_frame)
    ip_entry.grid(row=4, column=0, pady=5, sticky="ew")

    # Block IP
    block_button = ttk.Button(main_frame, text="Block IP", command=lambda: block_ip(ip_entry.get()))
    block_button.grid(row=5, column=0, pady=5, sticky="ew")

    # Unblock IP
    unblock_button = ttk.Button(main_frame, text="Unblock IP", command=lambda: unblock_ip(ip_entry.get()))
    unblock_button.grid(row=6, column=0, pady=5, sticky="ew")

    # List UFW Rules
    list_button = ttk.Button(main_frame, text="List UFW Rules", command=lambda: display_rules(root))
    list_button.grid(row=7, column=0, pady=5, sticky="ew")

    # Reset UFW
    reset_button = ttk.Button(main_frame, text="Reset UFW", command=reset_ufw)
    reset_button.grid(row=8, column=0, pady=5, sticky="ew")

    # Save Config
    save_button = ttk.Button(main_frame, text="Save Config", command=lambda: save_current_config())
    save_button.grid(row=9, column=0, pady=5, sticky="ew")

    # Load Config
    load_button = ttk.Button(main_frame, text="Load Config", command=lambda: load_saved_config())
    load_button.grid(row=10, column=0, pady=5, sticky="ew")

    # Backup Config
    backup_button = ttk.Button(main_frame, text="Backup Current Config", command=lambda: backup_current_config())
    backup_button.grid(row=11, column=0, pady=5, sticky="ew")

    # Restore Backup
    restore_button = ttk.Button(main_frame, text="Restore Backup", command=lambda: restore_backup_prompt())
    restore_button.grid(row=12, column=0, pady=5, sticky="ew")

    # Rate Limiting
    rate_limit_button = ttk.Button(main_frame, text="Enable Rate Limiting on SSH", command=lambda: rate_limit_ssh())
    rate_limit_button.grid(row=13, column=0, pady=5, sticky="ew")

    # Help Button
    help_button = ttk.Button(main_frame, text="Help", command=show_help)
    help_button.grid(row=14, column=0, pady=(5, 10), sticky="ew")

    # Start the GUI main loop
    root.mainloop()

def display_rules(root):
    """Display current UFW rules in a new window."""
    rules = list_rules()
    rules_window = tk.Toplevel(root)
    rules_window.title("UFW Rules")
    rules_window.geometry("400x300")
    rules_window.configure(bg='#1c1c1c')

    rules_text = tk.Text(rules_window, wrap=tk.WORD, bg='#2d2d2d', fg='white')
    rules_text.insert(tk.END, rules)
    rules_text.pack(expand=True, fill=tk.BOTH)

def check_ufw_status(root, console):
    """Check and display the UFW status in the console."""
    status = os.popen("sudo ufw status").read()
    console.write(status)

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

def rate_limit_ssh():
    """Enable rate limiting for SSH."""
    run_command("ufw limit ssh")
    run_command("ufw reload")
    messagebox.showinfo("Success", "SSH rate limiting enabled.")

