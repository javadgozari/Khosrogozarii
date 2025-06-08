import logging

class LogicMaster:
    def __init__(self, memory=None, brain=None):
        self.logger = logging.getLogger("LogicMaster")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🔍 مغز منطق فعال شد.")
        self.memory = memory
        self.brain = brain

    def reason(self, statement):
        self.logger.info(f"🧠 دریافت جمله برای تحلیل: {statement}")

        # بررسی حافظه برای تحلیل مشابه
        if self.memory:
            cached = self.memory.retrieve(statement)
            if cached:
                self.logger.info("📦 تحلیل از حافظه بازیابی شد.")
                return f"تحلیل منطقی (از حافظه): {cached}"

        # استفاده از GPT برای تحلیل هوشمند
        if self.brain:
            response = self.brain.reply_to(f"لطفاً این جمله را تحلیل منطقی کن: {statement}")
        else:
            response = f"تحلیل منطقی: {statement}"

        # ذخیره در حافظه
        if self.memory:
            self.memory.save(statement, response)
            self.logger.info("💾 تحلیل ذخیره شد.")

        self.logger.info(f"✅ پاسخ نهایی: {response}")
        return response
