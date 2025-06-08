import logging

from modules.code_assistant import CodeAssistant
from modules.dream_generator import DreamGenerator
from modules.emotion_brain import EmotionBrain
from modules.emotion_detector import EmotionDetector
from modules.emotion_responder import EmotionResponder
from modules.file_brain import FileBrain
from modules.game_developer import GameDeveloper
from modules.gpt_brain import GptBrain
from modules.history_guru import HistoryGuru
from modules.legal_advisor import LegalAdvisor
from modules.life_coach import LifeCoach
from modules.logic_master import LogicMaster
from modules.math_solver import MathSolver
from modules.medical_expert import MedicalExpert
from modules.memory_brain import MemoryBrain
from modules.memory_core import MemoryCore
from modules.music_brain import MusicBrain
from modules.music_composer import MusicComposer
from modules.ocr_reader import OcrReader
from modules.persian_story_teller import PersianStoryTeller
from modules.philosophy_core import PhilosophyCore
from modules.poet_molavi import PoetMolavi
from modules.poet_sufi import PoetSufi
from modules.psychologist import Psychologist
from modules.reminder_core import ReminderCore
from modules.science_searcher import ScienceSearcher
from modules.science_translator import ScienceTranslator
from modules.search_brain import SearchBrain
from modules.self_updater import SelfUpdater
from modules.self_upgrade_brain import SelfUpgradeBrain
from modules.self_upgrade_v2 import SelfUpgradeV2
from modules.translate_brain import TranslateBrain
from modules.translator import Translator
from modules.vision_brain import VisionBrain
from modules.vision_module import VisionModule
from modules.voice_actor import VoiceActor
from modules.voice_brain import VoiceBrain
from modules.voice_changer import VoiceChanger
from modules.whisper_module import WhisperModule

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("root")
    logger.info("🚀 اجرای خسرو آغاز شد...")

    memory = MemoryCore()
    brain = GptBrain(memory=memory)
    upgrader = SelfUpgradeV2()

    brain.activate()
    upgrader.check_for_update()
    upgrader.perform_upgrade()

    logger.info("✅ مغز اصلی و سیستم ارتقا فعال شدند.")

if __name__ == "__main__":
    main()
