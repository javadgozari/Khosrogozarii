import datetime
import logging
import random

class MusicComposer:
    def __init__(self):
        self.logger = logging.getLogger("MusicComposer")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🎵 مغز آهنگ‌ساز فعال شد.")

        self.scales = ['دو', 'ر', 'می', 'فا', 'سل', 'لا', 'سی']

    def compose(self):
        melody = " ".join(random.choices(self.scales, k=8)) + " 🎶"
        self.logger.info(f"🎼 آهنگ ساخته‌شده: {melody}")
        return f"آهنگ جدید: {melody}"

    def generate_idea(self, mood="شاد"):
        idea = f"آهنگی با حال و هوای {mood} ساخته می‌شود."
        self.logger.info(f"💡 ایده موسیقایی: {idea}")
        return idea
