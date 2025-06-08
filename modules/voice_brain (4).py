
import json
import os

class VoiceBrain:
    def __init__(self):
        self.memory_path = "voice_memory.json"
        self.learning_memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_memory(self):
        with open(self.memory_path, "w", encoding="utf-8") as f:
            json.dump(self.learning_memory, f, ensure_ascii=False, indent=2)

    def learn_from_father(self, topic, content):
        self.learning_memory[topic] = content
        self.save_memory()
        self.speak(f"پدرجان، موضوع «{topic}» را یاد گرفتم.")

    def speak(self, message):
        print("🎤 خسرو:", message)

    def respond_to_audio_input(self, audio_text):
        if audio_text.startswith("یاد بگیر:"):
            parts = audio_text[8:].split("=>")
            if len(parts) == 2:
                topic, content = parts[0].strip(), parts[1].strip()
                self.learn_from_father(topic, content)
                return
            else:
                self.speak("پدرجان، لطفاً به شکل 'یاد بگیر: موضوع => محتوا' بفرمایید.")
        elif audio_text in self.learning_memory:
            self.speak(f"پدرجان، درباره «{audio_text}» یاد گرفتم که: {self.learning_memory[audio_text]}")
        else:
            self.speak("پدرجان، هنوز اینو یاد نگرفتم. لطفاً آموزش بده.")
