from pyrogram import filters
from pyrogram.types import Message
from bot.main import app

@app.on_message(filters.command("start") & filters.private)
async def start_handler(_, message: Message):
    await message.reply_text(
        "👋 Welcome to **GitHub Manager Bot**\n\n"
        "Upload your `.zip` file and push files to your GitHub repo with ease.\n\n"
        "🔐 Use /token to securely set your GitHub token\n"
        "📤 Upload your `.zip` file\n"
        "📂 Provide repo name and branch\n"
        "🚪 Use /logout to remove your token\n\n"
        "**Your credentials are stored securely and never misused.**"
    )
