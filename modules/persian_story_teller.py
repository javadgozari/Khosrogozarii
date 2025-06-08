import requests
from modules.translator import Translator
from modules.voice_actor import VoiceActor
from modules.memory_core import MemoryCore
from modules.emotion_brain import EmotionBrain

class PersianStoryTeller:
    def __init__(self):
        self.translator = Translator()
        self.voice = VoiceActor()
        self.memory = MemoryCore()
        self.emotion = EmotionBrain()
        self.story_genres = {
            "کودکانه": "fairy tale",
            "عاشقانه": "romance",
            "ترسناک": "horror",
            "افسانه‌ای": "mythology",
            "تاریخی": "history",
            "طنز": "comedy"
        }

    def get_available_genres(self):
        return list(self.story_genres.keys())

    def fetch_story_online(self, genre_en):
        try:
            url = f"https://api.example.com/stories?genre={genre_en}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json().get("story", "داستانی پیدا نشد.")
            else:
                return "❌ خطا در دریافت داستان از منبع خارجی."
        except Exception as e:
            return f"⛔ خطا در ارتباط: {str(e)}"

    def tell_story(self, genre_fa="کودکانه", speak=True):
        genre_en = self.story_genres.get(genre_fa, "fairy tale")
        story_en = self.fetch_story_online(genre_en)
        story_fa = self.translator.translate(story_en, target_language="fa")

        emotion = self.emotion.detect(story_fa)
        self.memory.save(f"قصه {genre_fa}", story_fa)

        if speak:
            self.voice.speak(f"داستانی {genre_fa} برای تو دارم... {story_fa}")

        return f"🎙️ حالت احساسی: {emotion}\n📖 داستان: {story_fa}"
