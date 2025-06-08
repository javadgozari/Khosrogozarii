class GameDeveloper:
    def __init__(self, memory=None):
        self.memory = memory
        self.game_history = []

    def create_game(self, idea):
        log = f"یک بازی برای کیمیا ساخته می‌شود با موضوع: {idea}"
        self.game_history.append({"idea": idea, "log": log})
        if self.memory:
            self.memory.save("game_idea", idea)
        return log

    def get_last_game(self):
        if self.game_history:
            return self.game_history[-1]['log']
        return "هنوز هیچ بازی‌ای ساخته نشده است."

    def activate(self):
        print("🎮 مغز توسعه‌دهنده بازی فعال شد.")
