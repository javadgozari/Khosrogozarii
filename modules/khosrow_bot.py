from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore

# 🔐 توکن ربات تلگرام شما
TOKEN = "8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs"

# 🧠 فعال‌سازی مغز و حافظه
memory = MemoryCore()
brain = GPTBrain(memory=memory)

# 🎬 دستور شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من خسرو هستم 🤖 آماده‌ام که بهت کمک کنم.")

# 💬 پاسخ به پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = brain.reply_to(user_message)
    await update.message.reply_text(response)

# 🚀 اجرای ربات
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ربات خسرو با موفقیت اجرا شد.")
    app.run_polling()

if __name__ == "__main__":
    main()
