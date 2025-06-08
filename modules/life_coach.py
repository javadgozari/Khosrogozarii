import logging

class LifeCoach:
    def __init__(self, memory=None, brain=None):
        self.logger = logging.getLogger("LifeCoach")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🌿 مغز مربی زندگی فعال شد.")
        self.memory = memory
        self.brain = brain

    def advise(self, situation):
        self.logger.info(f"💬 وضعیت دریافت‌شده: {situation}")

        # بررسی حافظه
        if self.memory:
            cached = self.memory.retrieve(situation)
            if cached:
                self.logger.info("🧠 پاسخ از حافظه دریافت شد.")
                return cached

        # تولید پاسخ با GPT
        response = "گاهی بهترین راه، صبر کردنه 🌱"
        if self.brain:
            self.logger.info("🧠 استفاده از GPT برای تحلیل وضعیت...")
            response = self.brain.reply_to(f"چه توصیه‌ای داری برای این موقعیت: {situation}")

        # ذخیره پاسخ در حافظه
        if self.memory:
            self.memory.save(situation, response)
            self.logger.info("💾 پاسخ در حافظه ذخیره شد.")

        self.logger.info(f"✅ پاسخ نهایی مربی زندگی: {response}")
        return response
