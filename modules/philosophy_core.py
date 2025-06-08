import requests
from modules.translator import Translator
from modules.voice_actor import VoiceActor
from modules.memory_core import MemoryCore

class PhilosophyCore:
    def __init__(self):
        self.translator = Translator()
        self.voice = VoiceActor()
        self.memory = MemoryCore()
        self.sources = [
            "https://philosophy-api.vercel.app/quote",  # نمونه API فلسفی
            "https://api.quotable.io/random?tags=philosophy"
        ]

    def fetch_philosophical_quote(self):
        for url in self.sources:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if "content" in data:
                        return data["content"]
                    elif "quote" in data:
                        return data["quote"]
            except Exception as e:
                continue
        return "💭 فلسفه‌ای یافت نشد، دوباره تلاش کن."

    def reflect(self, speak=True):
        quote_en = self.fetch_philosophical_quote()
        quote_fa = self.translator.translate(quote_en, target_language="fa")
        self.memory.save("تفکر فلسفی", quote_fa)

        if speak:
            self.voice.speak("🧘 تأمل امروز: " + quote_fa)

        return quote_fa
