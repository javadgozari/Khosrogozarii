from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import torch

class VisionBrain:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def describe_image(self, image_url):
        try:
            image = Image.open(requests.get(image_url, stream=True).raw).convert('RGB')
            inputs = self.processor(image, return_tensors="pt")
            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            return caption
        except Exception as e:
            return f"❌ خطا در پردازش تصویر: {str(e)}"
