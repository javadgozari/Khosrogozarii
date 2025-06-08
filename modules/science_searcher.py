import logging
import requests

class ScienceSearcher:
    def __init__(self):
        self.logger = logging.getLogger("ScienceSearcher")
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.info("🧠 مغز جستجوی علمی فعال شد.")

    def search(self, query):
        self.logger.info(f"🔍 جستجوی علمی درباره: {query}")
        try:
            # جستجو در Semantic Scholar API
            url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=1&fields=title,abstract,url"
            response = requests.get(url)
            data = response.json()

            if data.get("data"):
                paper = data["data"][0]
                title = paper.get("title", "بدون عنوان")
                abstract = paper.get("abstract", "بدون خلاصه")
                link = paper.get("url", "بدون لینک")
                return f"📄 عنوان: {title}\n📚 چکیده: {abstract}\n🔗 لینک: {link}"
            else:
                return "❗ مطلبی درباره این موضوع پیدا نشد."
        except Exception as e:
            self.logger.error(f"❌ خطا در جستجو: {str(e)}")
            return "❌ خطایی در بازیابی اطلاعات علمی رخ داد."
