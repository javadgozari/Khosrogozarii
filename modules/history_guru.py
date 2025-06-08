import logging

class HistoryGuru:
    def __init__(self):
        self.logger = logging.getLogger("HistoryGuru")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("📜 مغز تاریخ فعال شد.")

    def fact(self):
        fact_text = 'کوروش بزرگ نخستین منشور حقوق بشر را نوشت.'
        self.logger.info(f"📚 داده تاریخی ارائه شد: {fact_text}")
        return fact_text
