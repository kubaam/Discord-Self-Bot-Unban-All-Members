
# 🛠 Discord Self-Bot: Unban All Members 🚫

## 🔥 Overview

This script automates the process of unbanning all members in servers where you have **administrator** or **ban_members** permissions! 🧑‍💻 Once the bot is running, it will display all eligible servers and ask for confirmation before proceeding to unban the members. It's designed to work with **discord.py-self** and removes any conflicting libraries automatically! 🔥

⚠️ **Important**: This bot requires your **Discord token** to function.

## 🛠 Features

- **Unban All Members**: Unbans all users in servers where you have admin or unban permissions 🆓.
- **Automatic Setup**: Removes conflicting Discord libraries and installs **discord.py-self** 📦.
- **Token Secure Input**: Get your Discord token securely without echoing 📲.
- **Error Handling**: Handles errors gracefully to prevent interruptions 🚫.

## 📦 Requirements

To run this script, you need to install **discord.py-self** and ensure no conflicting Discord libraries are present. This script will uninstall any conflicting libraries automatically.

### Install `discord.py-self`:

```bash
pip install discord.py-self
```

This will be installed automatically by the script, but you can manually install it before running.

## ⚙️ Setup

1. Clone or download the script file.
2. **No manual configuration required** – the script will handle library management and installation.
3. When prompted, **enter your Discord token** securely. The script will not echo your token back for privacy.

## 🏃‍♂️ How to Run

Simply run the script:

```bash
python discord_unban_bot.py
```

### Steps Followed by the Script:
1. **Uninstall Conflicting Libraries**: Automatically removes any conflicting Discord libraries (like `discord.py`, `nextcord`, etc.) 🧹.
2. **Install `discord.py-self`**: Installs the correct library for the bot to run 🔄.
3. **Token Input**: Securely ask for your Discord token 🔑.
4. **Select a Server**: Displays a list of servers where you have **unban** permissions and lets you select which one to unban all members from 🖥️.
5. **Unban Process**: After confirmation, unbans all banned users from the selected server ⚡.

### Example Output:

```bash
Uninstalling conflicting libraries...
Uninstalled discord.py
Installed discord.py-self
Enter your Discord token (will not echo):
Logged in as YourBotName
Servers where you have unban permissions:
1. Example Server (ID: 123456789)
2. Another Server (ID: 987654321)

Enter the number of the server to unban all members: 1
Are you sure you want to unban ALL members in Example Server? (y/n): y
Starting unban process...
Found 20 banned users. Unbanning...
Unbanned User1#1234
Unbanned User2#5678
...
Unban process completed.
```

## 🚨 Important Notes

- **Disclaimer**: Using self-bots violates [Discord's Terms of Service](https://discord.com/terms), and misuse could lead to account suspension or bans. **Use this tool responsibly and at your own risk.** ⚠️
- Ensure you have **admin or unban permissions** in the servers you want to unban members from 🔑.

---

🚫 **Happy Unbanning!** ⚡
