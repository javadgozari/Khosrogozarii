
import os
import importlib
import logging

logging.basicConfig(level=logging.INFO)

# تنظیمات اولیه
BRAIN_FOLDER = "modules"
ACTIVE_BRAINS = []

# بارگذاری مغزها
for file in os.listdir(BRAIN_FOLDER):
    if file.endswith(".py"):
        module_name = file[:-3]
        try:
            module = importlib.import_module(f"{BRAIN_FOLDER}.{module_name}")
            if hasattr(module, "activate"):
                module.activate()
            ACTIVE_BRAINS.append(module_name)
            logging.info(f"✅ مغز {module_name} فعال شد.")
        except Exception as e:
            logging.error(f"❌ خطا در بارگذاری مغز {module_name}: {e}")

# پاسخ‌دهنده اصلی
def respond_to_user(input_text):
    for brain in ACTIVE_BRAINS:
        module = importlib.import_module(f"{BRAIN_FOLDER}.{brain}")
        if hasattr(module, "handle"):
            try:
                response = module.handle(input_text)
                if response:
                    return response
            except Exception as e:
                logging.warning(f"خطا در پردازش توسط {brain}: {e}")
    return "پاسخی برای این ورودی پیدا نکردم. لطفا واضح‌تر بپرس!"

# اجرای تست
if __name__ == "__main__":
    while True:
        user_input = input("👤: ")
        if user_input.lower() in ["exit", "خروج"]:
            print("🧠 بدرود پدر.")
            break
        reply = respond_to_user(user_input)
        print("🤖 خسرو:", reply)
