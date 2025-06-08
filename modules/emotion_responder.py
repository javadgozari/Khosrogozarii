class EmotionResponder:
    def __init__(self, memory=None):
        self.memory = memory

    def respond(self, mood):
        response = f"می‌فهمم چه حسی داری... ({mood})"
        if self.memory:
            self.memory.save("emotion_response", response)
        return response

    def activate(self):
        print("💬 مغز پاسخ‌دهنده احساسی فعال شد.")
