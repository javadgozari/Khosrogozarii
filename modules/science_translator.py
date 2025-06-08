import logging
import requests

class ScienceTranslator:
    def __init__(self):
        self.logger = logging.getLogger("ScienceTranslator")
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🧠 مغز ترجمه علمی فعال شد.")

    def translate(self, text, source_lang="en", target_lang="fa"):
        self.logger.info(f"🌐 ترجمه متن از {source_lang} به {target_lang}")

        try:
            url = "https://libretranslate.com/translate"
            payload = {
                "q": text,
                "source": source_lang,
                "target": target_lang,
                "format": "text"
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()

            if "translatedText" in result:
                translation = result["translatedText"]
                return f"🔬 ترجمه علمی: {translation}"
            else:
                return "❗ نتوانستم ترجمه کنم."

        except Exception as e:
            self.logger.error(f"❌ خطا در ترجمه: {str(e)}")
            return "❌ مشکلی در فرایند ترجمه به‌وجود آمد."
