import logging
from modules.self_upgrade_v2 import SelfUpgradeV2
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.vision_module import VisionModule
from modules.voice_actor import VoiceActor
from modules.voice_changer import VoiceChanger
from modules.whisper_module import WhisperModule

# فعال‌سازی کدهای سایر مغزها
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

    memory = MemoryCore()
    brain = GPTBrain(memory=memory)
    upgrader = SelfUpgradeV2()

    brain.activate()
    upgrader.check_for_update()
    upgrader.perform_upgrade()

    logger.info("✅ مغز اصلی و سیستم ارتقا فعال شدند.")

if __name__ == "__main__":
    main()
