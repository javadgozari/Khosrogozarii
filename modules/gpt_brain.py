
import datetime

class GPTBrain
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
        self.learning_log.append(f"Learned about {topic} at {entry['timestamp']}")
        return f"I've learned about {topic}."

    def recall(self, topic):
        memories = [entry['data'] for entry in self.knowledge_base if entry['topic'] == topic]
        if memories:
            return f"Here's what I know about {topic}:\n" + "\n".join(memories)
        else:
            return f"I don't have knowledge about {topic} yet."

    def respond(self, input_text):
        # Naive keyword-based response logic for example purposes
        if "what do you know about" in input_text.lower():
            topic = input_text.lower().split("about")[-1].strip()
            return self.recall(topic)
        elif "learn" in input_text.lower():
            parts = input_text.lower().split("learn")
            if len(parts) > 1:
                topic_data = parts[1].strip().split(":")
                if len(topic_data) == 2:
                    topic = topic_data[0].strip()
                    data = topic_data[1].strip()
                    return self.learn(topic, data)
        return "I'm still learning. Could you teach me more?"

    def get_learning_log(self):
        return "\n".join(self.learning_log)
