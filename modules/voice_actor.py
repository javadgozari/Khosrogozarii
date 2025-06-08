import os
import torch
from TTS.api import TTS  # Coqui TTS
import uuid

class VoiceActor:
    def __init__(self):
        self.tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=torch.cuda.is_available())
        self.voices = {
            "کhosrow": "persian-male",  # نمونه شخصی‌سازی‌شده (اگر موجود باشد)
            "maryam": "female-en",     # صدای زن انگلیسی برای تست
            "molavi": "poetic"         # صدای شاعران
        }

    def speak_like(self, name, text, output_path="voice_output.wav"):
        style = self.voices.get(name.lower(), "persian-male")
        filename = f"voice_{uuid.uuid4().hex[:8]}.wav"
        self.tts.tts_to_file(text=text, speaker=style, file_path=filename)
        return f"🎙️ صدا با لحن {name} ذخیره شد: {filename}"
