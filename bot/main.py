# ---------------------------------------------------------
# GitHub Manager Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the GitHub Manager Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import os
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("GitHubManagerBot", bot_token=BOT_TOKEN)

# Import handlers
from bot.handlers import start, token, logout, upload, repo_flow

app.run()
