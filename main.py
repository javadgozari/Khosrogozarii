import logging
from modules.self_upgrade_v2 import SelfUpgradeManager
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.vision_module import VisionModule
from modules.voice_actor import VoiceActor
from modules.voice_changer import VoiceChanger
from modules.whisper_module import WhisperModule

# اضافه کردن سایر مغزها
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

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("root")
    logger.info("🚀 اجرای خسرو آغاز شد...")

    # فعال‌سازی حافظه و مغز اصلی
    memory = MemoryCore()
    brain = GPTBrain(memory=memory)
    upgrader = SelfUpgradeManager()

    # فعال‌سازی مغزهای فرعی و عملکردها
    psychologist = Psychologist()
    philosopher = PhilosophyCore()
    scientist = ScienceSearcher()
    translator = Translator()
    math = MathSolver()
    doctor = MedicalExpert()
    poet_molavi = PoetMolavi()
    poet_sufi = PoetSufi()
    storyteller = PersianStoryTeller()
    lawyer = LegalAdvisor()
    coach = LifeCoach()
    logic = LogicMaster()
    history = HistoryGuru()
    music = MusicComposer()
    ocr = OCRReader()
    emotion_brain = EmotionBrain()
    emotion_talker = EmotionResponder()
    emotion_detector = EmotionDetector()
    game = GameDeveloper()
    reminder = ReminderCore()
    vision = VisionModule()
    speaker = VoiceActor()
    voice_mod = VoiceChanger()
    whisper = WhisperModule()

    # فعال‌سازی مغزها
    brain.activate()
    upgrader.check_for_updates()

    logger.info("🧠 خسرو اکنون کاملاً فعال و متصل به اینترنت، دوربین و میکروفن است.")

if __name__ == "__main__":
    main()
