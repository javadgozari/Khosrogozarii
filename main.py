
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from modules.gpt_brain import GPTBrain

brain = GPTBrain()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام پدر جان ❤️ خسرو در خدمت شماست.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = brain.respond(user_input)
    await update.message.reply_text(response)

if __name__ == '__main__':
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    print("🤖 خسرو آماده‌ست تا حرف بزنه...")
    app.run_polling()
