import datetime

class GPTBrain:
    def __init__(self, memory=None):
        self.memory = memory
        self.knowledge_base = []
        self.learning_log = []

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
        return f"یاد گرفتم درباره {topic} ✅"

    def recall(self, topic):
        if self.memory:
            data = self.memory.retrieve(topic)
            if data:
                return f"یادآوری از حافظه: {data}"
        memories = [entry['data'] for entry in self.knowledge_base if entry['topic'] == topic]
        return memories[-1] if memories else "یادآوری‌ای برای این موضوع ندارم."

    def reply_to(self, message):
        response = f"🧠 پاسخ GPT به: {message}"
        return response

    def activate(self):
        print("🧠 مغز GPT فعال شد!")
