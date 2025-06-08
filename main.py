import logging

# مغزهای اصلی
from modules.self_upgrade_v2 import SelfUpgradeV2
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.vision_module import VisionModule
from modules.voice_actor import VoiceActor
from modules.voice_changer import VoiceChanger
from modules.whisper_module import WhisperModule

# مغزهای تخصصی
from modules.psychologist import Psychologist
from modules.philosophy_core import PhilosophyCore
from modules.science_searcher import ScienceSearcher
from modules.science_translator import ScienceTranslator
from modules.translator import Translator
from modules.math_solver import MathSolver
from modules.medical_expert import MedicalExpert
from modules.poet_molavi import PoetMolavi
from modules.poet_sufi import PoetSufi
from modules.persian_story_teller import PersianStoryTeller
from modules.legal_advisor import LegalAdvisor
from modules.life_coach import LifeCoach
from modules.logic_master import LogicMaster
from modules.history_guru import HistoryGuru
from modules.music_composer import MusicComposer
from modules.ocr_reader import OCRReader
from modules.emotion_brain import EmotionBrain
from modules.emotion_responder import EmotionResponder
from modules.emotion_detector import EmotionDetector
from modules.game_developer import GameDeveloper
from modules.reminder_core import ReminderCore
from modules.voice_brain import VoiceBrain

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("Khosrow")
    logger.info("🚀 اجرای خسرو آغاز شد...")

    # حافظه
    memory = MemoryCore()

    # مغز مرکزی
    brain = GPTBrain(memory=memory)

    # فعال‌سازی سایر ماژول‌ها (صرفاً شبیه‌سازی فعال‌سازی)
    vision = VisionModule()
    voice_actor = VoiceActor()
    voice_changer = VoiceChanger()
    whisper = WhisperModule()
    psychologist = Psychologist()
    philosopher = PhilosophyCore()
    science_searcher = ScienceSearcher()
    science_translator = ScienceTranslator()
    translator = Translator()
    math_solver = MathSolver()
    medical = MedicalExpert()
    poet1 = PoetMolavi()
    poet2 = PoetSufi()
    storyteller = PersianStoryTeller()
    legal = LegalAdvisor()
    coach = LifeCoach()
    logic = LogicMaster()
    history = HistoryGuru()
    music = MusicComposer()
    ocr = OCRReader()
    emotion = EmotionBrain()
    responder = EmotionResponder()
    detector = EmotionDetector()
    game_dev = GameDeveloper()
    reminder = ReminderCore()
    voice_brain = VoiceBrain()

    # ارتقا خودکار
    upgrader = SelfUpgradeV2()
    upgrader.check_for_update()
    upgrader.perform_upgrade()

    # فعال‌سازی مغز
    brain.activate()
    logger.info("✅ مغز GPT فعال شد.")
    logger.info("✅ تمامی مغزها بارگذاری شدند.")

if __name__ == "__main__":
    main()
