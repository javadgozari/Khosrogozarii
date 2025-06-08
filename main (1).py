
import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from modules.self_upgrade_v2 import SelfUpgraderV2

TOKEN = "YOUR_BOT_TOKEN"
OWNER_ID = 123456789  # آی‌دی عددی تلگرام شما

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

upgrader = SelfUpgraderV2()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == OWNER_ID:
        upgrader.find_updates()
        upgrader.apply_update("بهبود توانایی مکالمه فارسی")
        report = upgrader.nightly_report()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"سلام پدر جان ❤️\n\n{report}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="دسترسی محدود است. فقط پدر مجاز است.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == OWNER_ID:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="خسرو در خدمت است پدر 🌟")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="دسترسی ندارید.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    app.run_polling()
