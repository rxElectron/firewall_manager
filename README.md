# 🔥 Firewall Manager

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-green?style=for-the-badge&logo=linux&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

A modern, user-friendly GUI-based firewall management tool for Linux systems built with Python and Tkinter. Easily control incoming and outgoing traffic, save/load configurations, and manage firewall settings with ease.

## 🚀 Features

- **Open/Close FTP and SSH Ports**: Easily manage FTP (port 21) and SSH (port 22) access.
- **Block/Unblock Specific IP Addresses**: Secure your system by blocking unwanted IPs.
- **Save and Load Custom Firewall Configurations**: Create reusable configurations for different network setups.
- **Backup and Restore UFW Settings**: Safeguard your settings with easy backup and restore functionality.
- **Responsive and Colorful GUI**: Modern, intuitive, and adaptive interface.
- **Detailed Help Section for Arch Linux Users**: Step-by-step guidance tailored for Arch Linux.

<details>
<summary>📝 <strong>Click to expand detailed features</strong></summary>

- **Dynamic Resizing and Responsive Design**: Adjusts seamlessly to different screen sizes and resolutions.
- **User-Defined Configuration Locations**: Save configurations anywhere you prefer.
- **Automatic Backups**: Backup current firewall settings before any changes are made.
- **One-Click Restore**: Revert to previous firewall settings instantly.
- **Modern, Colorful Design**: Engaging interface with vibrant colors and easy-to-read fonts.

</details>

## 📦 Installation

Follow these steps to install and run the Firewall Manager:

### Prerequisites

- **Python 3.8** or higher
- **Tkinter** (Python's standard GUI toolkit)
- **UFW (Uncomplicated Firewall)** installed on your Linux system

### Step-by-Step Guide

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/therboy/firewall_manager.git
    cd firewall_manager
    ```

2. **Install Dependencies**:

    On **Arch Linux**:

    ```bash
    sudo pacman -S tk ufw
    ```

    On **Ubuntu/Debian**:

    ```bash
    sudo apt-get install python3-tk ufw
    ```

3. **Run the Application**:

    ```bash
    python3 main.py
    ```

## 🎮 Usage

To use the Firewall Manager, simply run the `main.py` script and follow the instructions on the GUI. The application allows you to manage firewall settings like opening or closing ports, blocking/unblocking IP addresses, saving/loading configurations, and more!

<details>
<summary>🛠️ <strong>Click to expand usage examples</strong></summary>

### Example: Block an IP Address

1. Open the application.
2. Enter the IP address you want to block in the text field.
3. Click "Block IP".

### Example: Save Current Firewall Configuration

1. Open the application.
2. Click "Save Config".
3. Choose a location to save the configuration file.

### Example: Restore a Backup

1. Open the application.
2. Click "Restore Backup".
3. Select the backup file you want to restore from.

</details>

## 📚 Help

For detailed help documentation, click the "Help" button in the application. For Arch Linux users, make sure that UFW is installed and enabled:

```bash
sudo pacman -S ufw
sudo systemctl enable ufw
sudo systemctl start ufw
```

For more information, visit the [Arch Linux UFW Documentation](https://wiki.archlinux.org/title/UFW).

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure your code follows the project's style guidelines and passes all tests.

### Steps to Contribute

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix:
   
    ```bash
    git checkout -b feature-branch
    ```

3. **Commit your changes** with a descriptive commit message:

    ```bash
    git commit -m 'Add new feature'
    ```

4. **Push your branch** to GitHub:

    ```bash
    git push origin feature-branch
    ```

5. **Open a pull request** on GitHub and provide a detailed description of your changes.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

© 2024 Reza Khodarahimi - All Rights Reserved
