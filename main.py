import os
import subprocess
import sys
import discord
from discord.ext import commands
import asyncio

# Function to uninstall all conflicting Discord libraries
def uninstall_conflicting_libraries():
    libraries = ["discord.py", "nextcord", "py-cord", "discord"]
    for lib in libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", lib])
            print(f"Uninstalled {lib}")
        except Exception as e:
            print(f"Failed to uninstall {lib}: {e}")

# Function to install discord.py-self
def install_discord_py_self():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py-self"])
        print("Installed discord.py-self")
    except Exception as e:
        print(f"Failed to install discord.py-self: {e}")
        sys.exit(1)

# Function to get the Discord token securely
def get_token():
    token = input("Enter your Discord token (will not echo): ")
    if not token:
        print("Token is required to proceed.")
        sys.exit(1)
    return token

# Main bot logic
def main():
    # Uninstall conflicting libraries
    print("Uninstalling conflicting libraries...")
    uninstall_conflicting_libraries()

    # Install discord.py-self
    print("Installing discord.py-self...")
    install_discord_py_self()

    # Get Discord token
    TOKEN = get_token()

    # Initialize bot
    bot = commands.Bot(command_prefix="!", self_bot=True)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

        # List servers where the user has admin or unban permissions
        eligible_servers = []
        for guild in bot.guilds:
            member = guild.get_member(bot.user.id)
            if member and (member.guild_permissions.administrator or member.guild_permissions.ban_members):
                eligible_servers.append(guild)

        if not eligible_servers:
            print("No servers found where you have unban permissions.")
            await bot.close()
            return

        # Display eligible servers
        print("\nServers where you have unban permissions:")
        for i, server in enumerate(eligible_servers, 1):
            print(f"{i}. {server.name} (ID: {server.id})")

        # Get user selection
        try:
            choice = int(input("\nEnter the number of the server to unban all members: ")) - 1
            selected_guild = eligible_servers[choice]
        except (ValueError, IndexError):
            print("Invalid selection.")
            await bot.close()
            return

        # Confirm unban action
        confirm = input(f"Are you sure you want to unban ALL members in {selected_guild.name}? (y/n): ")
        if confirm.lower() != "y":
            print("Unban process cancelled.")
            await bot.close()
            return

        # Unban all members
        print("Starting unban process...")
        try:
            banned_users = await selected_guild.bans()
            if not banned_users:
                print("No banned users found.")
                await bot.close()
                return

            print(f"Found {len(banned_users)} banned users. Unbanning...")
            for ban_entry in banned_users:
                user = ban_entry.user
                try:
                    await selected_guild.unban(user)
                    print(f"Unbanned {user.name}#{user.discriminator}")
                    await asyncio.sleep(1)  # Avoid rate limits
                except Exception as e:
                    print(f"Failed to unban {user.name}: {e}")

            print("Unban process completed.")
        except Exception as e:
            print(f"An error occurred: {e}")

        await bot.close()

    # Run the bot
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error running bot: {e}")

if __name__ == "__main__":
    main()