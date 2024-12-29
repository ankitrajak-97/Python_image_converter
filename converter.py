from pillow_heif import register_heif_opener
from PIL import Image
import os
register_heif_opener()

class ImageConverter:
    def __init__(self, input_path: str, output_path: str, quality: int = 95):
       
        self.input_path = input_path
        self.output_path = output_path
        self.quality = quality

    def convert(self):
        
        try:
            image = Image.open(self.input_path)
            output_dir = os.path.dirname(self.output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            image.save(self.output_path, "JPEG", quality=self.quality)
            print(f"Conversion successful! JPEG saved at: {self.output_path} with quality {self.quality}")
        except Exception as e:
            print(f"Error during conversion: {e}")
