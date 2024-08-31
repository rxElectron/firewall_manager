# 🔥 Firewall Manager

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, user-friendly GUI-based firewall management tool for Linux systems built with Python and Tkinter. Easily control incoming and outgoing traffic, save/load configurations, and manage firewall settings with ease.

## 🚀 Features

- **Open/Close FTP and SSH Ports**
- **Block/Unblock Specific IP Addresses**
- **Save and Load Custom Firewall Configurations**
- **Backup and Restore UFW Settings**
- **Responsive and Colorful GUI**
- **Detailed Help Section for Arch Linux Users**

<details>
<summary>📝 Click to expand detailed features</summary>

- Dynamic resizing and responsive design for all screen sizes.
- Save configurations to user-defined locations.
- Backup current firewall settings before making changes.
- Restore firewall settings to a previous state with one click.
- User-friendly interface with a modern, colorful design.

</details>

## 📦 Installation

Follow these steps to install and run the Firewall Manager:

### Prerequisites

- Python 3.8 or higher
- Tkinter
- UFW (Uncomplicated Firewall) installed on your Linux system

### Step-by-Step Guide

1. **Clone the Repository**:

    
    git clone https://github.com/therboy/firewall_manager.git
    cd firewall_manager
    

2. **Install Dependencies**:

    On Arch Linux:

    
    sudo pacman -S tk ufw
    

    On Ubuntu/Debian:

    
    sudo apt-get install python3-tk ufw
    

3. **Run the Application**:

    
    python3 main.py
    

## 🎮 Usage

To use the Firewall Manager, simply run the `main.py` script and follow the instructions on the GUI. You can open or close specific ports, block/unblock IP addresses, save/load configurations, and more!

<details>
<summary>🛠️ Click to expand usage examples</summary>

### Example: Block an IP Address

1. Open the application.
2. Enter the IP address you want to block in the text field.
3. Click "Block IP".

### Example: Save Current Firewall Configuration

1. Open the application.
2. Click "Save Config".
3. Choose a location to save the configuration file.

</details>

## 📚 Help

For detailed help documentation, click the "Help" button in the application. For Arch Linux users, ensure that UFW is installed and enabled:


sudo pacman -S ufw
sudo systemctl enable ufw
sudo systemctl start ufw


For more information, visit the [Arch Linux UFW Documentation](https://wiki.archlinux.org/title/UFW).

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's style and passes all tests.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

© 2024 Reza Khodarahimi - All Rights Reserved
