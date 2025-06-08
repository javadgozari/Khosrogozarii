import random
import logging

class MusicBrain:
    def __init__(self):
        self.styles = ["سنتی", "پاپ", "کلاسیک", "محلی", "احساسی", "مدرن"]
        self.logger = logging.getLogger("MusicBrain")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.info("🎼 مغز موسیقی بارگذاری شد.")

    def generate_melody(self, mood="شاد"):
        melody = f"آهنگی با حال و هوای {mood} در سبک {random.choice(self.styles)} ساخته شد."
        self.logger.info(f"🎵 ملودی تولید شد: {melody}")
        return melody

    def suggest_instrument(self):
        instruments = ["پیانو", "گیتار", "سنتور", "کمانچه", "تار", "ویولن"]
        chosen = random.choice(instruments)
        self.logger.info(f"🎻 ساز پیشنهادی: {chosen}")
        return f"پیشنهاد می‌کنم از ساز {chosen} استفاده کنی."

    def inspire_poem(self, topic="عشق"):
        self.logger.info(f"🎙️ تولید شعر برای موضوع: {topic}")
        return f"شعری برای {topic}: در دل شب، صدای تو چون نوای آرامش است..."
