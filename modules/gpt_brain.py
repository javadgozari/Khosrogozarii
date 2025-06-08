import datetime
import logging

class GPTBrain:
    def __init__(self, memory=None):
        self.memory = memory
        self.knowledge_base = []
        self.learning_log = []
        self.logger = logging.getLogger("GPTBrain")
        self.logger.info("🧠 مغز GPT ساخته شد.")

    def learn(self, topic, data):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "topic": topic,
            "data": data
        }
        self.knowledge_base.append(entry)
        self.learning_log.append(f"یادگرفتم درباره {topic}: {data}")
        if self.memory:
            self.memory.save(topic, data)
            self.logger.info(f"🧠 ذخیره در حافظه: {topic}")
        return f"یاد گرفتم درباره {topic} ✅"

    def recall(self, topic):
        if self.memory:
            data = self.memory.retrieve(topic)
            if data:
                return f"یادآوری از حافظه: {data}"
        memories = [entry['data'] for entry in self.knowledge_base if entry['topic'] == topic]
        return memories[-1] if memories else "❗ یادآوری‌ای برای این موضوع ندارم."

    def reply_to(self, message):
        response = f"🧠 پاسخ GPT به: {message}"
        return response

    def activate(self):
        self.logger.info("✅ GPTBrain فعال شد.")
        print("🧠 مغز GPT فعال شد!")
