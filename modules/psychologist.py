import logging
from modules.emotion_detector import EmotionDetector
from modules.emotion_responder import EmotionResponder
from modules.memory_core import MemoryCore

class Psychologist:
    def __init__(self):
        self.logger = logging.getLogger("Psychologist")
        self.detector = EmotionDetector()
        self.responder = EmotionResponder()
        self.memory = MemoryCore()
        self.logger.info("🧠 روان‌شناس فعال شد.")

    def comfort(self, feeling, user_id="default_user"):
        detected_emotion = self.detector.detect(feeling)
        response = self.responder.respond(detected_emotion)

        # ذخیره در حافظه
        if self.memory:
            self.memory.save(user_id, f"احساس شناسایی‌شده: {detected_emotion} | پاسخ داده‌شده: {response}")
        
        # گزارش در لاگ
        self.logger.info(f"📝 احساس: {feeling} → {detected_emotion}")
        self.logger.info(f"✅ پاسخ آرامش‌بخش: {response}")
        
        return response
