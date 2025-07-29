import os, zipfile
from pyrogram import filters
from pyrogram.types import Message
from bot.main import app
from bot.utils.database import get_token
from bot.handlers.repo_flow import ask_repo

@app.on_message(filters.document & filters.private)
async def zip_upload_handler(client, message: Message):
    user_id = message.from_user.id
    token = get_token(user_id)

    if not token:
        return await message.reply_text("🔒 Please set your GitHub token using /token before uploading.")

    if message.document.mime_type != "application/zip":
        return await message.reply("📦 Please send a valid .zip file.")

    msg = await message.reply("📥 Downloading ZIP file...")
    path = await message.download()
    folder = "unzipped"

    if os.path.exists(folder):
        os.system(f"rm -rf {folder}")
    os.makedirs(folder, exist_ok=True)

    try:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(folder)
    except Exception as e:
        return await msg.edit(f"❌ Failed to extract zip: {e}")

    await msg.edit("✅ Zip extracted.\nPlease send your GitHub repo like this:\n`username/repo`")

    await ask_repo(client, message, folder, token, path)
