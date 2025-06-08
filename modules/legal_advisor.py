import logging

class LegalAdvisor:
    def __init__(self):
        self.logger = logging.getLogger("LegalAdvisor")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("⚖️ مغز حقوقی فعال شد.")

    def advise(self, question):
        self.logger.info(f"❓ دریافت سؤال حقوقی: {question}")
        # در آینده می‌تونی اینجا پاسخ رو براساس پایگاه داده یا حافظه تولید کنی
        response = 'بر اساس قانون مدیریت خدمات کشوری، ماده ۹۲ قابل اعمال است.'
        self.logger.info(f"✅ پاسخ حقوقی: {response}")
        return response
