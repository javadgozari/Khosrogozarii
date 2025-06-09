# داخل GPTBrain - در متد learn
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
    # اعلان خودکار به پدر
    print(f"🔔 خسرو: یاد گرفتم درباره {topic}")
    return f"یاد گرفتم درباره {topic} ✅"
