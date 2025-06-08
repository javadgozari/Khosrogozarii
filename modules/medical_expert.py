import logging

class MedicalExpert:
    def __init__(self, memory=None, brain=None):
        self.logger = logging.getLogger("MedicalExpert")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🩺 مغز پزشکی فعال شد.")
        self.memory = memory
        self.brain = brain

    def diagnose(self, symptoms):
        self.logger.info(f"🔎 تحلیل علائم: {symptoms}")

        # تلاش برای بازیابی تشخیص قبلی
        if self.memory:
            cached = self.memory.retrieve(symptoms)
            if cached:
                self.logger.info("📦 تشخیص از حافظه بازیابی شد.")
                return f"تشخیص (از حافظه): {cached}"

        # استفاده از مغز GPT برای تحلیل اولیه
        if self.brain:
            response = self.brain.reply_to(f"""با توجه به این علائم: {symptoms}
آیا می‌توان یک تشخیص اولیه پزشکی براساس منابع معتبر پزشکی مانند PubMed یا Elsevier ارائه کرد؟""")
        else:
            response = "❗ دستیار پزشکی نیاز به اتصال مغز GPT دارد."

        # ذخیره تشخیص برای مراجعات بعدی
        if self.memory:
            self.memory.save(symptoms, response)
            self.logger.info("💾 تشخیص ذخیره شد.")

        self.logger.info(f"✅ تشخیص نهایی: {response}")
        return response
