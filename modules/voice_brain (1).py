
import os

class VoiceBrain:
    def __init__(self):
        self.known_responses = {
            "سلام": "سلام عزیز دلم!",
            "اسمت چیه": "من خسرو هستم. پسر تو.",
            "خوبی": "تا تو خوبی، منم خوبم!",
        }
        self.learning_path = "data/voice_learning.txt"
        self.load_learnings()

    def load_learnings(self):
        if os.path.exists(self.learning_path):
            with open(self.learning_path, "r", encoding="utf-8") as f:
                for line in f:
                    if ":" in line:
                        q, a = line.strip().split(":", 1)
                        self.known_responses[q.strip()] = a.strip()

    def save_learning(self, question, answer):
        with open(self.learning_path, "a", encoding="utf-8") as f:
            f.write(f"{question.strip()}:{answer.strip()}\n")
        self.known_responses[question.strip()] = answer.strip()

    def respond(self, input_text):
        for q in self.known_responses:
            if q in input_text:
                return self.known_responses[q]
        return "نمیدونم چی بگم ولی می‌تونی بهم یاد بدی با گفتن 'یاد بگیر: سوال | جواب'"

    def learn_from_text(self, input_text):
        if input_text.startswith("یاد بگیر:"):
            parts = input_text.replace("یاد بگیر:", "").split("|")
            if len(parts) == 2:
                self.save_learning(parts[0], parts[1])
                return f"یاد گرفتم که اگه گفتی «{parts[0].strip()}» باید بگم «{parts[1].strip()}»"
            else:
                return "فرمت یادگیری باید این‌طوری باشه: یاد بگیر: سوال | جواب"
        return None
