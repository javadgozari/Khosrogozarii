
import telebot
from brains.voice_brain import process_voice
from brains.gpt_brain import ask_gpt
import os

TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

print("🤖 Khosrow is alive and listening...")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    try:
        response = ask_gpt(message.text)
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"❌ خطا در پردازش متن: {e}")

@bot.message_handler(content_types=['voice', 'audio'])
def handle_voice(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = f"temp/{file_info.file_path.split('/')[-1]}"
        os.makedirs("temp", exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        text = process_voice(file_path)
        response = ask_gpt(text)
        bot.reply_to(message, response)
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"❌ خطا در پردازش صدا: {e}")

bot.polling()
