from googletrans import Translator as GoogleTranslator

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator()

    def translate(self, message, dest='fa'):
        try:
            translated = self.translator.translate(message, dest=dest)
            return f"🗣 ترجمه ({translated.src} → {dest}): {translated.text}"
        except Exception as e:
            return f"❌ خطا در ترجمه: {str(e)}"
