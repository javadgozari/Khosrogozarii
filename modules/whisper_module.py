import whisper
import logging

class WhisperModule:
    def __init__(self):
        self.logger = logging.getLogger("WhisperModule")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🎙️ ماژول Whisper برای تبدیل صدا به متن فعال شد.")

        try:
            self.model = whisper.load_model("base")
            self.logger.info("✅ مدل Whisper با موفقیت بارگذاری شد.")
        except Exception as e:
            self.logger.error(f"❌ خطا در بارگذاری مدل Whisper: {e}")
            self.model = None

    def transcribe(self, audio_path):
        if self.model is None:
            return "❌ مدل بارگذاری نشده است."
        try:
            result = self.model.transcribe(audio_path)
            self.logger.info("📝 متن استخراج‌شده با موفقیت:")
            self.logger.info(result["text"])
            return result["text"]
        except Exception as e:
            self.logger.error(f"❌ خطا در تبدیل صدا به متن: {e}")
            return "❌ خطا در تبدیل صدا به متن"
