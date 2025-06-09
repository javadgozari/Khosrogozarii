import logging
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore
from modules.self_upgrade_v2 import SelfUpgradeV2

# بارگذاری همه مغزهای هوش مصنوعی
from modules import (
    emotion_brain, emotion_responder, emotion_detector,
    music_brain, music_composer,
    file_brain, translator, translate_brain,
    voice_changer, voice_brain, voice_actor,
    vision_module, science_searcher, science_translator,
    logic_master, math_solver, medical_expert,
    reminder_core, history_guru, life_coach,
    legal_advisor, philosopher, poet_molavi, poet_sufi,
    game_developer, ocr_reader, persian_story_teller,
    code_assistant, dream_generator, psychologist,
    search_brain
)

def activate_all_modules():
    brains = {
        "GPT": GPTBrain(memory=MemoryCore()),
        "Emotion": emotion_brain.EmotionBrain(),
        "Responder": emotion_responder.EmotionResponder(),
        "Detector": emotion_detector.EmotionDetector(),
        "Music": music_brain.MusicBrain(),
        "Composer": music_composer.MusicComposer(),
        "File": file_brain.FileBrain(),
        "Translator": translator.Translator(),
        "DeepTranslator": translate_brain.TranslateBrain(),
        "VoiceChanger": voice_changer.VoiceChanger(),
        "VoiceBrain": voice_brain.VoiceBrain(),
        "VoiceActor": voice_actor.VoiceActor(),
        "Vision": vision_module.VisionModule(),
        "ScienceSearch": science_searcher.ScienceSearcher(),
        "ScienceTranslate": science_translator.ScienceTranslator(),
        "Logic": logic_master.LogicMaster(),
        "Math": math_solver.MathSolver(),
        "Medical": medical_expert.MedicalExpert(),
        "Reminder": reminder_core.ReminderCore(),
        "History": history_guru.HistoryGuru(),
        "Life": life_coach.LifeCoach(),
        "Legal": legal_advisor.LegalAdvisor(),
        "Philosophy": philosopher.PhilosophyCore(),
        "Molavi": poet_molavi.PoetMolavi(),
        "Sufi": poet_sufi.PoetSufi(),
        "Game": game_developer.GameDeveloper(),
        "OCR": ocr_reader.OCRReader(),
        "Story": persian_story_teller.PersianStoryTeller(),
        "Code": code_assistant.CodeAssistant(),
        "Dream": dream_generator.DreamGenerator(),
        "Psy": psychologist.Psychologist(),
        "Search": search_brain.SearchBrain()
    }

    for name, brain in brains.items():
        print(f"🧠 مغز {name} فعال شد.")

    return brains

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("🚀 اجرای خسرو آغاز شد.")
    
    brains = activate_all_modules()
    SelfUpgradeV2().perform_upgrade()

    print("✅ همه مغزها فعال شدند و خسرو آماده است.")

if __name__ == "__main__":
    main()
