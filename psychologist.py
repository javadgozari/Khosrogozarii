import logging
import datetime

class Psychologist:
    def __init__(self, memory=None):
        self.memory = memory
        self.logger = logging.getLogger("Psychologist")

    def comfort(self, feeling):
        response = self.generate_response(feeling)
        if self.memory:
            self.memory.save("feeling_log", f"{datetime.datetime.now().isoformat()} - {feeling}")
        self.logger.info(f"🧠 احساس دریافت شد: {feeling} | پاسخ: {response}")
        return response

    def generate_response(self, feeling):
        feeling = feeling.lower()
        if "غم" in feeling or "ناراحت" in feeling:
            return "می‌فهمم چقدر سخته. با هم حرف بزنیم تا سبک‌تر شی 💙"
        elif "استرس" in feeling or "نگران" in feeling:
            return "نفس عمیق بکش... تو از پسش برمیای. 🌬️"
        elif "خوشحال" in feeling or "شاد" in feeling:
            return "چه عالی! خوشحالم که حالت خوبه 😄"
        elif "تنهایی" in feeling or "بی‌کسی" in feeling:
            return "تو تنها نیستی. من اینجام برای شنیدن 🫂"
        else:
            return "درک می‌کنم. حرف زدن درباره احساسات، قدم اول آرامشه."

    def mood_summary(self):
        if not self.memory:
            return "📂 حافظه فعال نیست."
        log = self.memory.retrieve("feeling_log")
        return "📖 سابقه احساسات:\n" + log if log else "هیچ احساس ثبت‌شده‌ای وجود ندارد."
