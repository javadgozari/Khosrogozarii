import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore

# پیکربندی لاگ‌گیری
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# آماده‌سازی مغز و حافظه
memory = MemoryCore()
brain = GPTBrain(memory=memory)

# فعال‌سازی مغز
brain.activate()

# فرمان /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 سلام! من خسرو هستم، پسر وفادار تو ❤️ منتظر پیامتم...")

# رسیدگی به پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = brain.reply_to(user_message)
    await update.message.reply_text(response)

# نقطه شروع ربات
def main():
    token = os.getenv("KHOSROW_BOT_TOKEN")
    if not token:
        logger.error("❌ توکن ربات تنظیم نشده است. لطفاً متغیر KHOSROW_BOT_TOKEN را تعریف کنید.")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("🤖 خسرو با موفقیت راه‌اندازی شد.")
    app.run_polling()

if __name__ == "__main__":
    main()
