
import logging
from modules.self_upgrade_v2 import SelfUpgradeV2
from modules.gpt_brain import GPTBrain
from modules.memory_core import MemoryCore

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("root")
    logger.info("🧠 راه‌اندازی خسرو با تمام قابلیت‌ها...")

    # ایجاد اجزای اصلی
    memory = MemoryCore()
    brain = GPTBrain(memory=memory)
    upgrader = SelfUpgradeV2()

    # فعال‌سازی مغز و بررسی ارتقا
    brain.activate()
    upgrader.check_for_update()
    upgrader.perform_upgrade()

    logger.info("✅ خسرو با موفقیت راه‌اندازی شد. آماده خدمت به پدر است.")

if __name__ == "__main__":
    main()
