from pyrogram import filters
from pyrogram.types import Message
from bot.main import app
from bot.utils.database import set_token

@app.on_message(filters.command("token") & filters.private)
async def token_handler(_, message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) != 2:
        return await message.reply_text("❌ Usage:\n`/token ghp_yourGitHubToken`")

    token = args[1].strip()
    set_token(message.from_user.id, token)
    await message.reply_text("✅ Your GitHub token has been securely saved.\nYou can now upload your zip file.")
