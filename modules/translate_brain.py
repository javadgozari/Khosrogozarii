import requests
import logging

class TranslateBrain:
    def __init__(self):
        self.logger = logging.getLogger("TranslateBrain")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
            self.logger.addHandler(handler)

        self.supported_languages = {
            'en': 'English',
            'fa': 'Persian',
            'ar': 'Arabic',
            'fr': 'French',
            'de': 'German',
            'es': 'Spanish'
        }

    def translate_online(self, text, source_lang='auto', target_lang='fa'):
        try:
            url = "https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": f"{source_lang}|{target_lang}"
            }
            response = requests.get(url, params=params)
            result = response.json()
            translated = result['responseData']['translatedText']
            self.logger.info(f"Online Translation Success: {text} → {translated}")
            return translated
        except Exception as e:
            self.logger.error(f"Online translation failed: {e}")
            return "❌ خطا در ترجمه آنلاین"

    def translate_offline(self, text, source_lang='en', target_lang='fa'):
        try:
            import argostranslate.package, argostranslate.translate
            installed_languages = argostranslate.translate.get_installed_languages()
            from_lang = next((lang for lang in installed_languages if lang.code == source_lang), None)
            to_lang = next((lang for lang in installed_languages if lang.code == target_lang), None)

            if not from_lang or not to_lang:
                return "❗ زبان‌های موردنظر برای ترجمه آفلاین نصب نشده‌اند."

            translation = from_lang.get_translation(to_lang)
            result = translation.translate(text)
            self.logger.info(f"Offline Translation Success: {text} → {result}")
            return result
        except Exception as e:
            self.logger.error(f"Offline translation failed: {e}")
            return "❌ خطا در ترجمه آفلاین"

    def auto_translate(self, text, target_lang='fa', method='online'):
        if method ==
