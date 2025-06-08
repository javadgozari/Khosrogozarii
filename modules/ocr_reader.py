import telebot
from telebot import types
from googletrans import Translator, LANGUAGES
import pytesseract
from PIL import Image
import os

API_TOKEN = 'توکن رباتت رو اینجا بذار'
bot = telebot.TeleBot(API_TOKEN)
translator = Translator()

last_extracted_text = None

# OCR کردن عکس
def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path), lang='eng+fas')

# دریافت تصویر
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_path = "received.jpg"
    with open(image_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    global last_extracted_text
    last_extracted_text = extract_text_from_image(image_path)

    bot.send_message(message.chat.id, f"📝 متن استخراج‌شده:\n\n{last_extracted_text}\n\nبرای ترجمه، دستور /translate را بزنید.")

# دریافت دستور ترجمه
@bot.message_handler(commands=['translate'])
def show_language_options(message):
    markup = types.InlineKeyboardMarkup()
    row = []
    count = 0
    for code, name in LANGUAGES.items():
        button = types.InlineKeyboardButton(name.title(), callback_data=f"lang_{code}")
        row.append(button)
        count += 1
        if count % 3 == 0:
            markup.row(*row)
            row = []
    if row:
        markup.row(*row)
    bot.send_message(message.chat.id, "🌐 لطفاً زبان مقصد را انتخاب کنید:", reply_markup=markup)

# انجام ترجمه
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def handle_language_selection(call):
    dest_lang = call.data.split('_')[1]
    global last_extracted_text
    if not last_extracted_text:
        bot.answer_callback_query(call.id, "❗ هیچ متنی برای ترجمه موجود نیست.")
        return
    translated = translator.translate(last_extracted_text, dest=dest_lang)
    bot.send_message(call.message.chat.id, f"🌐 ترجمه به {LANGUAGES[dest_lang].title()}:\n\n{translated.text}")

# شروع ربات
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! 👋\nعکس بفرست تا متنشو بخونم، بعد می‌تونی ترجمه‌ش کنی.")

print("🤖 ربات آماده است...")
bot.polling()
