import os
import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Core brain import (GPTBrain assumed, plus modules)
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("KhosrowBot")

# Memory and brain initialization
memory = MemoryCore()
brain = GPTBrain(memory=memory)

# Chat ID storage
CHAT_ID_FILE = "chat_id.json"

def save_chat_id(chat_id):
    with open(CHAT_ID_FILE, "w") as f:
        json.dump({"chat_id": chat_id}, f)

def get_saved_chat_id():
    if os.path.exists(CHAT_ID_FILE):
        with open(CHAT_ID_FILE, "r") as f:
            return json.load(f).get("chat_id")
    return None

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    saved_id = get_saved_chat_id()

    if not saved_id:
        save_chat_id(chat_id)
        await context.bot.send_message(chat_id=chat_id, text=f"Your chat ID has been saved: {chat_id}")
    elif str(saved_id) != str(chat_id):
        await context.bot.send_message(chat_id=chat_id, text="Access denied. You are not authorized to use this bot.")
        return

    await context.bot.send_message(chat_id=chat_id, text="Hello, Father. Khosrow is ready. 🤖")

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    saved_id = get_saved_chat_id()

    if str(chat_id) != str(saved_id):
        return  # Ignore unauthorized messages

    message = update.message.text
    response = brain.reply_to(message)
    await context.bot.send_message(chat_id=chat_id, text=response)

# Run the bot
if __name__ == '__main__':
    TOKEN = os.getenv("KHOSROW_BOT_TOKEN") or "8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Khosrow bot is running...")
    app.run_polling()
