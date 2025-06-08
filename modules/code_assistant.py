class CodeAssistant:
    def __init__(self, memory=None):
        self.memory = memory

    def help(self, query):
        suggestion = 'پیشنهاد کد پایتون: print("سلام")'
        if self.memory:
            self.memory.save("code_help", f"درخواست: {query} => پاسخ: {suggestion}")
        return suggestion

    def activate(self):
        print("🤖 دستیار کدنویسی فعال شد.")
