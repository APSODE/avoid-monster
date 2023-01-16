from PIL import Image
from src.decorator.ErrorChecker import ErrorChecker
from typing import Tuple

class ImageEditor:
    @staticmethod
    def EditSize(file_dir: str, size: Tuple[int, int]) -> Image:
        target_image = Image.open(file_dir)
        return target_image.resize(size = size)






if __name__ == '__main__':
    edited_image = ImageEditor.EditSize(
        file_dir = "..\\..\\resources\\start_menu.png",
        size = (480, 320)
    )
    edited_image.save("..\\..\\resources\\start_menu (edited).png")

