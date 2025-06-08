import datetime
import json
import os

class VoiceBrain:
    def __init__(self, memory_file="voice_memory.json", tts=None, emotion_module=None):
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.last_spoken = None
        self.tts = tts  # تابع تبدیل متن به گفتار
        self.emotion_module = emotion_module  # مثلاً اتصال به EmotionResponder

    def speak(self, message):
        self.last_spoken = message
        self.log_message(f"Khosrow says: {message}")
        print(f"🎙️ {message}")
        if self.tts:
            self.tts(message)

    def learn_voice(self, text, response):
        self.memory.append({"input": text, "output": response})
        self.save_memory()
        self.log_message(f"Learned: '{text}' → '{response}'")

    def respond(self, text):
        for item in reversed(self.memory):
            if item["input"] in text:
                response = item["output"]
                if self.emotion_module:
                    response += " " + self.emotion_module.respond("عادی")
                self.speak(response)
                return
        self.speak("متوجه نشدم. لطفاً واضح‌تر بگو.")

    def log_message(self, msg):
        with open("voice_brain_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {msg}\n")

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)
