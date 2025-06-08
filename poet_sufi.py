import random
import logging

class PoetSufi:
    def __init__(self, memory=None):
        self.memory = memory
        self.logger = logging.getLogger("PoetSufi")
        self.poems = [
            "تو بیا تا جهان زنده شود... مولانا",
            "در این سرای بی‌کسی، کسی به در نمی‌زند... هوشنگ ابتهاج",
            "تو مرا جان و جهانی، چه کنم جان و جهان را؟ – سعدی",
            "یارب! چه خوش صبوحی بود آن شراب اول... حافظ",
            "دلم گرفته ای دوست! هوای گریه با من... فروغ"
        ]

    def whisper(self, mood=None):
        selected_poem = random.choice(self.poems)
        self.logger.info(f"🌀 شعر نجوا شد: {selected_poem}")

        if self.memory and mood:
            self.memory.save("sufi_poetry_log", f"حالت: {mood} → {selected_poem}")

        return f"✨ {selected_poem}"

    def add_poem(self, new_poem):
        self.poems.append(new_poem)
        self.logger.info(f"🎙️ شعر جدید اضافه شد: {new_poem}")
        return "✅ شعر به دفتر اشعار صوفی افزوده شد."

    def get_all_poems(self):
        return "\n".join(self.poems)
