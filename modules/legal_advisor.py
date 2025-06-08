import logging

class LegalAdvisor:
    def __init__(self, memory=None, brain=None):
        self.logger = logging.getLogger("LegalAdvisor")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("⚖️ مغز حقوقی فعال شد.")
        self.memory = memory
        self.brain = brain

    def advise(self, question):
        self.logger.info(f"❓ سؤال حقوقی دریافت شد: {question}")
        
        # ابتدا بررسی در حافظه
        if self.memory:
            cached = self.memory.retrieve(question)
            if cached:
                self.logger.info("🧠 پاسخ از حافظه بازیابی شد.")
                return cached

        # پاسخ پایه اولیه
        response = "بر اساس قانون مدیریت خدمات کشوری، ماده ۹۲ قابل اعمال است."
        
        # در صورت وجود مغز اصلی GPT، از آن برای تحلیل استفاده کن
        if self.brain:
            self.logger.info("🔎 استفاده از GPT برای تحلیل سؤال حقوقی...")
            response = self.brain.reply_to(f"پاسخ حقوقی برای: {question}")

        # ذخیره در حافظه
        if self.memory:
            self.memory.save(question, response)
            self.logger.info("💾 پاسخ در حافظه ذخیره شد.")

        self.logger.info(f"✅ پاسخ نهایی: {response}")
        return response
