import requests
from modules.translator import Translator
from modules.voice_actor import VoiceActor
from modules.memory_core import MemoryCore

class PoetSufi:
    def __init__(self):
        self.api_url = "https://ganjoor-api.dev/sufi/random"  # فرضی برای اشعار عرفانی
        self.translator = Translator()
        self.voice = VoiceActor()
        self.memory = MemoryCore()

    def fetch_poem(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("poem", "تو بیا تا جهان زنده شود...")
        except Exception:
            return "تو بیا تا جهان زنده شود..."

    def whisper(self, lang="fa", speak=True, tag="عرفانی"):
        poem = self.fetch_poem()

        if self.memory:
            self.memory.save(f"شعر {tag}", poem)

        if lang != "fa":
            poem = self.translator.translate(poem, target_language=lang)

        if speak:
            self.voice.speak(poem)

        return poem
