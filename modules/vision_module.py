from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class VisionModule:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def describe_image(self, image_path):
        try:
            image = Image.open(image_path).convert('RGB')
            inputs = self.processor(image, return_tensors="pt")
            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            return caption
        except Exception as e:
            return f"❌ خطا در توصیف تصویر: {str(e)}"
