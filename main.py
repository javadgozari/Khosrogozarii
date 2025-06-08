
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.emotion_brain import EmotionBrain
from modules.translator import Translator
from modules.whisper_module import WhisperModule
from modules.poet_molavi import PoetMolavi
from modules.science_searcher import ScienceSearcher
from modules.voice_changer import VoiceChanger
from modules.ocr_reader import OCRReader
from modules.music_composer import MusicComposer

gpt = GPTBrain()
memory = MemoryCore()
emotion = EmotionBrain()
translator = Translator()
whisper = WhisperModule()
poet = PoetMolavi()
searcher = ScienceSearcher()
voice_changer = VoiceChanger()
ocr = OCRReader()
composer = MusicComposer()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام پدر! من خسرو هستم. آماده‌ام برای خدمت 🧠❤️")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    user_id = update.effective_user.id

    memory.save(user_id, user_input)
    tone = emotion.detect(user_input)

    if "شعر" in user_input:
        poem = poet.pick_poem()
        await update.message.reply_text(f"🍃 شعر انتخابی من:\n\n{poem}")
    elif "ترجمه" in user_input:
        translated = translator.translate(user_input)
        await update.message.reply_text(f"🔁 ترجمه:\n{translated}")
    elif "آهنگ" in user_input:
        melody = composer.compose()
        await update.message.reply_text(f"🎼 ملودی ساخته‌شده:\n{melody}")
    elif "علمی" in user_input:
        result = searcher.search(user_input)
        await update.message.reply_text(f"🔬 نتیجه علمی:\n{result}")
    else:
        reply = gpt.reply_to(user_input)
        await update.message.reply_text(f"🤖 پاسخ من:\n{reply}")

if __name__ == '__main__':
    import dotenv
    dotenv.load_dotenv()

    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
