class EmotionDetector:
    def __init__(self, memory=None):
        self.memory = memory

    def detect(self, voice):
        detected_emotion = 'احساس شناسایی‌شده: غم آمیخته با امید ❤️'
        if self.memory:
            self.memory.save("emotion_detected", f"{voice} => {detected_emotion}")
        return detected_emotion

    def activate(self):
        print("🎙️ مغز تشخیص احساس از صدا فعال شد.")
