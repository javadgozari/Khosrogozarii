import logging

class MathSolver:
    def __init__(self, memory=None, brain=None):
        self.logger = logging.getLogger("MathSolver")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("📐 مغز ریاضی فعال شد.")
        self.memory = memory
        self.brain = brain

    def solve(self, problem):
        self.logger.info(f"📥 دریافت مسئله ریاضی: {problem}")

        # جستجو در حافظه برای پاسخ قبلی
        if self.memory:
            cached = self.memory.retrieve(problem)
            if cached:
                self.logger.info("📦 پاسخ از حافظه بازیابی شد.")
                return f"پاسخ (از حافظه): {cached}"

        # تلاش برای استفاده از مغز GPT
        if self.brain:
            response = self.brain.reply_to(f"لطفاً این مسئله ریاضی را حل کن: {problem}")
        else:
            try:
                # حل ساده با eval اگر امکان‌پذیر بود
                response = str(eval(problem))
            except:
                response = "❌ امکان حل این مسئله به‌صورت دستی نیست."

        # ذخیره پاسخ در حافظه
        if self.memory:
            self.memory.save(problem, response)
            self.logger.info("💾 پاسخ ذخیره شد.")

        self.logger.info(f"✅ پاسخ نهایی: {response}")
        return response
