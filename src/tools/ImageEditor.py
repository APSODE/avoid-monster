from typing import *
from PIL import Image as img
from PIL.Image import Image


class ImageEditor:
    def __init__(self, image_dir: str):
        self._target_image = img.open(image_dir)

    def EditSize(self, size: Tuple[int, int]) -> Image:
        return self._target_image.resize(size = size)

    def Crop(self, part_amount: Tuple[int, int]) -> List[Image]:
        rt_image_list = []

        target_image_size = self._target_image.size

        part_width = target_image_size[0] // part_amount[0]
        part_height = target_image_size[1] // part_amount[1]

        result_pos_data = {
            "x1": 0,
            "y1": 0,
            "x2": part_width,
            "y2": part_height
        }

        for _ in range(part_amount[1]): #height
            for _ in range(part_amount[0]): #width
                rt_image_list.append(
                    self._target_image.crop(
                        box = (
                            result_pos_data.get("x1"),
                            result_pos_data.get("y1"),
                            result_pos_data.get("x2"),
                            result_pos_data.get("y2")
                        )
                    )
                )

                result_pos_data["x1"] += part_width
                result_pos_data["x2"] += part_width
            result_pos_data["y1"] += part_height
            result_pos_data["y2"] += part_height

        return rt_image_list


if __name__ == '__main__':
    IE = ImageEditor(
        image_dir = "..\\..\\스프라이트\\red hood itch free Copy-Sheet.png"
    )

    # IE.EditSize(size = (100, 100)).save("xptmxm.png")
    count = 1
    for edited_image in IE.Crop(part_amount = (12, 11)):
        edited_image.save(f"..\\..\\resources\\test\\test_{count}.png")
        count += 1


