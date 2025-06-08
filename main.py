
import logging
from modules.self_upgrade_v2 import SelfUpgradeManager
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("root")

    logger.info("✨ هوش خسرو در حال راه‌اندازی است...")

    memory = MemoryCore()
    brain = GPTBrain(memory=memory)
    upgrader = SelfUpgradeManager()

    brain.activate()
    upgrader.check_for_updates()

    logger.info("✅ خسرو آماده گفتگو است.")

if __name__ == "__main__":
    main()
