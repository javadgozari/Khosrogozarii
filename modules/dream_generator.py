class DreamGenerator:
    def __init__(self, memory=None):
        self.memory = memory

    def generate(self):
        idea = 'یک ایده جدید: رباتی که نقاشی می‌کشد!'
        if self.memory:
            self.memory.save("dream", idea)
        return idea

    def activate(self):
        print("💡 مغز تولید رویا فعال شد.")
