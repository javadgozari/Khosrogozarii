import json
import os
import datetime
import logging

class MemoryCore:
    def __init__(self, storage_path="memory_data.json"):
        self.storage_path = storage_path
        self.logger = logging.getLogger("MemoryCore")
        self.logger.setLevel(logging.INFO)
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)
        self.logger.info("🧠 حافظه فعال و آماده است.")

    def save(self, key, value):
        with open(self.storage_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        timestamp = datetime.datetime.now().isoformat()
        if key not in data:
            data[key] = []

        data[key].append({
            "timestamp": timestamp,
            "value": value
        })

        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        self.logger.info(f"💾 ذخیره‌سازی انجام شد: {key} -> {value}")

    def retrieve(self, key):
        if not os.path.exists(self.storage_path):
            return None

        with open(self.storage_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if key in data and data[key]:
            latest = data[key][-1]["value"]
            self.logger.info(f"📦 یادآوری: {key} -> {latest}")
            return latest

        self.logger.warning(f"🔍 موردی برای کلید '{key}' یافت نشد.")
        return None

    def recall_all(self):
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)
