
import datetime

class VoiceBrain:
    def __init__(self):
        self.memory = []
        self.last_spoken = None

    def speak(self, message):
        self.last_spoken = message
        self.log_message(f"Khosrow says: {message}")
        print(f"🎙️ {message}")

    def learn_voice(self, text, response):
        self.memory.append((text, response))
        self.log_message(f"Learned: '{text}' → '{response}'")

    def respond(self, text):
        for q, a in self.memory[::-1]:
            if q in text:
                self.speak(a)
                return
        self.speak("متوجه نشدم. لطفاً واضح‌تر بگو.")

    def log_message(self, msg):
        with open("voice_brain_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {msg}\n")
