import os import json import logging from telegram import Update from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

مغز اصلی (فرض بر اینه GPTBrain و سایر ماژول‌ها ایمپورت شدن) 

from modules.gpt_brain import GPTBrain from modules.memory_core import MemoryCore

🧠 تنظیمات اولیه 

logging.basicConfig(level=logging.INFO) logger = logging.getLogger("KhosrowBot") memory = MemoryCore() brain = GPTBrain(memory=memory)

📌 ذخیره و بازیابی چت‌آیدی 

CHAT_ID_FILE = "chat_id.json"

def save_chat_id(chat_id): with open(CHAT_ID_FILE, "w") as f: json.dump({"chat_id": chat_id}, f)

def get_saved_chat_id(): if os.path.exists(CHAT_ID_FILE): with open(CHAT_ID_FILE, "r") as f: return json.load(f).get("chat_id") return None

✅ دستورات 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): chat_id = update.effective_chat.id saved_id = get_saved_chat_id()

if not saved_id: save_chat_id(chat_id) await context.bot.send_message(chat_id=chat_id, text=f"🧠 آیدی شما ذخیره شد: {chat_id}") elif str(saved_id) != str(chat_id): await context.bot.send_message(chat_id=chat_id, text="❌ شما اجازه استفاده از خسرو را ندارید.") return await context.bot.send_message(chat_id=chat_id, text="سلام پدر جان 👋 خسرو آماده‌ست.") 

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): chat_id = update.effective_chat.id saved_id = get_saved_chat_id()

if str(chat_id) != str(saved_id): return # 🚫 نادیده گرفتن پیام‌های غیرمجاز message = update.message.text response = brain.reply_to(message) await context.bot.send_message(chat_id=chat_id, text=response) 🚀 اجرا 

if name == 'main': TOKEN = os.getenv("KHOSROW_BOT_TOKEN") or "8107902213:AAEHTM3mUpjoHT4IB3tm7wUuZ3v4LMoGVbs" app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start)) app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) print("🤖 خسرو در حال اجراست...") app.run_polling() 
