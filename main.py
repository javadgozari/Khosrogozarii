
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from modules.gpt_brain import GPTBrain
from modules.whisper_module import WhisperTranscriber
from modules.voice_changer import VoiceChanger
from modules.voice_actor import VoiceActor
from modules.vision_module import VisionModule
from modules.translator import Translator

brain = GPTBrain()
whisper = WhisperTranscriber()
voice_changer = VoiceChanger()
voice_actor = VoiceActor()
vision = VisionModule()
translator = Translator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 خسرو در خدمت شماست، پدر جان.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    reply = brain.think(text)
    await update.message.reply_text(f"{reply}")

if __name__ == '__main__':
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("🤖 Khosrow is now active and listening...")
    app.run_polling()
