class EmotionBrain:
    def __init__(self, memory=None):
        self.memory = memory

    def detect(self, message):
        emotion = 'خنثی'
        if self.memory:
            self.memory.save("emotion", f"{message} => {emotion}")
        return emotion

    def activate(self):
        print("❤️ مغز احساس فعال شد.")
