import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Khosrow")

# فراخوانی مغزهای فعال
from modules.gpt_brain import GPTBrain
from modules.math_solver import MathSolver
from modules.translator import Translator
from modules.poet_molavi import PoetMolavi
from modules.poet_sufi import PoetSufi
from modules.legal_advisor import LegalAdvisor
from modules.life_coach import LifeCoach
from modules.psychologist import Psychologist
from modules.history_guru import HistoryGuru
from modules.science_searcher import ScienceSearcher
from modules.science_translator import ScienceTranslator
from modules.persian_story_teller import PersianStoryTeller
from modules.emotion_responder import EmotionResponder

# حافظه مرکزی
from modules.memory_core import MemoryCore

# پیکربندی توکن بات تلگرام
TELEGRAM_TOKEN = "8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs"

# حافظه و مغز اصلی
memory = MemoryCore()
gpt_brain = GPTBrain(memory=memory)

# سایر مغزها
math_solver = MathSolver()
translator = Translator()
molavi = PoetMolavi()
sufi = PoetSufi()
legal = LegalAdvisor()
life_coach = LifeCoach()
psychologist = Psychologist()
history = HistoryGuru()
science = ScienceSearcher()
science_translator = ScienceTranslator()
story_teller = PersianStoryTeller()
emotion_responder = EmotionResponder()

# تشخیص مغز بر اساس کلمات کلیدی
def select_brain(text):
    if "ریاضی" in text or "محاسبه" in text:
        return math_solver.solve(text)
    elif "ترجمه" in text:
        return translator.translate(text)
    elif "شعر" in text and "مولوی" in text:
        return molavi.pick_poem()
    elif "شعر" in text:
        return sufi.whisper()
    elif "قانون" in text or "ماده" in text:
        return legal.advise(text)
    elif "زندگی" in text or "مشاوره" in text:
        return life_coach.advise(text)
    elif "احساس" in text or "ناراحتی" in text:
        return psychologist.comfort(text)
    elif "تاریخ" in text or "قدیم" in text:
        return history.fact()
    elif "علمی" in text:
        return science.search(text)
    elif "ساده" in text and "علمی" in text:
        return science_translator.translate(text)
    elif "قصه" in text or "داستان" in text:
        return story_teller.tell_story()
    elif "حالت" in text or "دل" in text:
        return emotion_responder.respond(text)
    else:
        return gpt_brain.reply_to(text)

# هندلر پیام
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    logger.info(f"📩 پیام دریافتی: {user_input}")
    response = select_brain(user_input)
    await update.message.reply_text(response)

# هندلر شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 سلام! من خسرو هستم. آماده‌ام کمکت کنم.")

# اجرای برنامه
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("🤖 خسرو آماده پاسخ‌گویی در تلگرام است.")
    app.run_polling()

if __name__ == "__main__":
    main()
