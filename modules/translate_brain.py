import logging
from transformers import pipeline
from deep_translator import GoogleTranslator
from langdetect import detect

class TranslateBrain:
    def __init__(self):
        self.logger = logging.getLogger("TranslateBrain")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.info("🧠 TranslateBrain آماده است.")
        self.offline_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fa")

    def detect_language(self, text):
        try:
            lang = detect(text)
            self.logger.info(f"📡 زبان تشخیص‌داده‌شده: {lang}")
            return lang
        except Exception as e:
            self.logger.error(f"❌ خطا در تشخیص زبان: {e}")
            return 'unknown'

    def translate_online(self, text, target_lang='fa'):
        try:
            result = GoogleTranslator(source='auto', target=target_lang).translate(text)
            self.logger.info(f"✅ ترجمه آنلاین: {result}")
            return result
        except Exception as e:
            self.logger.error(f"❌ خطا در ترجمه آنلاین: {e}")
            return "خطا در ترجمه آنلاین"

    def translate_offline(self, text, target_lang='fa'):
        try:
            if target_lang != 'fa':
                return "❌ ترجمه آفلاین فعلاً فقط به فارسی فعال است."
            result = self.offline_translator(text)[0]['translation_text']
            self.logger.info(f"✅ ترجمه آفلاین: {result}")
            return result
        except Exception as e:
            self.logger.error(f"❌ خطا در ترجمه آفلاین: {e}")
            return "خطا در ترجمه آفلاین"

    def auto_translate(self, text, target_lang='fa', method='online'):
        if method == 'offline':
            return self.translate_offline(text, target_lang=target_lang)
        else:
            return self.translate_online(text, target_lang=target_lang)
