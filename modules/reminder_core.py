import datetime
import logging
from modules.memory_core import MemoryCore

class ReminderCore:
    def __init__(self):
        self.logger = logging.getLogger("ReminderCore")
        self.reminders = []
        self.memory = MemoryCore()
        self.logger.info("⏰ هسته یادآوری فعال شد.")

    def set_reminder(self, text, user_id="default_user"):
        timestamp = datetime.datetime.now().isoformat()
        entry = {
            "text": text,
            "timestamp": timestamp
        }
        self.reminders.append(entry)
        self.logger.info(f"📌 یادآور ثبت شد: {text} در {timestamp}")
        
        # ذخیره در حافظه
        if self.memory:
            self.memory.save(user_id, f"یادآور: {text} | زمان ثبت: {timestamp}")

        return f"⏰ یادآور تنظیم شد: {text}"

    def list_reminders(self):
        if not self.reminders:
            return "یادآوری‌ای تنظیم نشده است."
        return "\n".join([f"- {r['text']} ({r['timestamp']})" for r in self.reminders])
