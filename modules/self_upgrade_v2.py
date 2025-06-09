# داخل SelfUpgradeV2 - در متد perform_upgrade
def perform_upgrade(self):
    try:
        self.logger.info("⚙️ اجرای ارتقای خودکار (نسخه %s)...", self.version)
        # اعلان ارتقا
        print("🔔 خسرو: نسخه جدیدم نصب شد. الان قوی‌ترم! 💪")
    except Exception as e:
        self.logger.error("❌ خطا در ارتقا: %s", e)
