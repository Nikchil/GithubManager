from pyrogram import filters
from pyrogram.types import Message
from bot.main import app
from bot.utils.github_uploader import upload_to_github

async def ask_repo(client, message, folder, token, zip_path):
    @app.on_message(filters.text & filters.private)
    async def get_repo(_, msg: Message):
        repo = msg.text.strip()
        await msg.reply("🌿 Now send branch name (or type `main`):")

        @app.on_message(filters.text & filters.private)
        async def get_branch(_, branch_msg: Message):
            branch = branch_msg.text.strip()
            branch = branch if branch else "main"
            await branch_msg.reply("🚀 Uploading to GitHub...")

            result = upload_to_github(
                user_token=token,
                repo_name=repo,
                branch=branch,
                folder_path=folder
            )

            if result:
                await branch_msg.reply("✅ Upload successful!")
            else:
                await branch_msg.reply("⚠️ Upload failed. Check token/repo/branch.")

            os.remove(zip_path)
            os.system(f"rm -rf {folder}")
