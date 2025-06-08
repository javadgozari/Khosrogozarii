import os
import asyncio

# بارگذاری تمام مغزها
from modules.gpt_brain import GPTBrain
from modules.voice_brain import VoiceBrain
from modules.search_brain import SearchBrain
from modules.memory_brain import MemoryBrain
from modules.self_upgrade_brain import SelfUpgradeBrain
from modules.file_brain import FileBrain
from modules.translate_brain import TranslateBrain
from modules.vision_brain import VisionBrain
from modules.music_brain import MusicBrain
from modules.emotion_brain import EmotionBrain
from modules.code_brain import CodeBrain
from modules.math_brain import MathBrain
from modules.story_brain import StoryBrain
from modules.pdf_brain import PDFBrain
from modules.ocr_brain import OCRBrain
from modules.web_brain import WebBrain

# اتصال به بات تلگرام
from modules.telegram_bot import TelegramBot

async def main():
    # نمونه‌سازی مغزها
    gpt_brain = GPTBrain()
    voice_brain = VoiceBrain()
    search_brain = SearchBrain()
    memory_brain = MemoryBrain()
    self_upgrade_brain = SelfUpgradeBrain()
    file_brain = FileBrain()
    translate_brain = TranslateBrain()
    vision_brain = VisionBrain()
    music_brain = MusicBrain()
    emotion_brain = EmotionBrain()
    code_brain = CodeBrain()
    math_brain = MathBrain()
    story_brain = StoryBrain()
    pdf_brain = PDFBrain()
    ocr_brain = OCRBrain()
    web_brain = WebBrain()

    # اتصال به بات با لیست مغزها
    bot = TelegramBot([
        gpt_brain, voice_brain, search_brain, memory_brain, self_upgrade_brain,
        file_brain, translate_brain, vision_brain, music_brain, emotion_brain,
        code_brain, math_brain, story_brain, pdf_brain, ocr_brain, web_brain
    ])
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
