from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from modules.gpt_brain import GPTBrain  # اطمینان حاصل کن این فایل درست ایمپورت میشه

# نمونه‌سازی از مغز
brain = GPTBrain()

# دستور شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام من خسرو هستم 🤖 هر چی می‌خوای بپرس!")

# پاسخ به پیام‌های متنی
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = brain.reply_to(user_message)
    update.message.reply_text(response)

def main():
    #8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs
    updater = Updater("8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs", use_context=True)
    dp = updater.dispatcher

    # هندلرها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # شروع بات
    updater.start_polling()
    print("🤖 ربات خسرو فعال شد.")
    updater.idle()

if __name__ == "__main__":
    main()
