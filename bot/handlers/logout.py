from pyrogram import filters
from pyrogram.types import Message
from bot.main import app
from bot.utils.database import remove_token

@app.on_message(filters.command("logout") & filters.private)
async def logout_handler(_, message: Message):
    remove_token(message.from_user.id)
    await message.reply_text("✅ Your GitHub token has been removed. You are logged out.")
