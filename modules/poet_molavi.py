import requests
from modules.translator import Translator
from modules.voice_actor import VoiceActor
from modules.memory_core import MemoryCore

class PoetMolavi:
    def __init__(self):
        self.api_url = "https://ganjoor-api.dev/molavi/random"  # فرضی برای شعر مولانا
        self.translator = Translator()
        self.voice = VoiceActor()
        self.memory = MemoryCore()

    def fetch_poem(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("poem", "بی‌تو به سر نمی‌شود...")
        except Exception:
            return "بی‌تو به سر نمی‌شود..."

    def pick_poem(self, lang="fa", speak=True):
        original_poem = self.fetch_poem()
        translated = original_poem

        if lang != "fa":
            translated = self.translator.translate(original_poem, target_language=lang)

        self.memory.save("شعر مولانا", original_poem)

        if speak:
            self.voice.speak(original_poem)

        return translated
