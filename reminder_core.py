import datetime
import logging

class ReminderCore:
    def __init__(self):
        self.reminders = []
        self.logger = logging.getLogger("ReminderCore")

    def set_reminder(self, text, time_str):
        try:
            remind_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            self.reminders.append({"text": text, "time": remind_time})
            self.logger.info(f"🔔 یادآور ثبت شد: {text} در {remind_time}")
            return f"📝 یادآور تنظیم شد برای {remind_time}: {text}"
        except ValueError:
            return "⚠️ فرمت زمان صحیح نیست. مثال: 2025-06-08 18:30"

    def check_reminders(self, now=None):
        if now is None:
            now = datetime.datetime.now()

        due_reminders = [r for r in self.reminders if r["time"] <= now]
        for r in due_reminders:
            self.logger.info(f"⏰ یادآور فعال شد: {r['text']}")
        self.reminders = [r for r in self.reminders if r["time"] > now]

        return [f"🔔 یادآور: {r['text']}" for r in due_reminders] or ["هیچ یادآوری‌ای فعال نیست."]
