from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.self_upgrade_v2 import SelfUpgradeV2
from modules.vision_module import VisionModule
from modules.voice_actor import VoiceActor
from modules.voice_changer import VoiceChanger
from modules.whisper_module import WhisperModule
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
from modules.file_brain import FileBrain
from modules.search_brain import SearchBrain
from modules.memory_brain import MemoryBrain
from modules.translate_brain import TranslateBrain
from modules.self_upgrade_brain import SelfUpgradeBrain
from modules.music_brain import MusicBrain

def run():
    print("🤖 خسرو با تمام مغزها در حال راه‌اندازی است...")

    memory = MemoryCore()
    brain = GPTBrain(memory=memory)
    upgrader = SelfUpgradeV2()

    brain.activate()
    upgrader.check_for_update()
    upgrader.perform_upgrade()

    print("✅ خسرو با موفقیت فعال شد.")
