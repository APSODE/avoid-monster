from typing import *
from enum import Enum
import pygame


class DisplayResolution(Enum):
    FHD = ("fhd", 1920, 1080)
    HD = ("hd", 1280, 720)

    def __init__(self, description: str, width: int, height: int):
        self.description = description
        self.width = width
        self.height = height


class DisplayData:
    def __init__(self,
                 screen_res: Optional[DisplayResolution],
                 screen_img_dir: Optional[str],
                 cont: bool = False
                 ):
        self._screen_res = screen_res
        self._continue = cont
        self._screen_img = pygame.image.load(screen_img_dir)

    @property
    def ScreenRes(self) -> DisplayResolution:
        return self._screen_res

    @property
    def ContinueInfo(self) -> bool:
        return self._continue

    @property
    def ScreenImage(self) -> pygame.Surface:
        # print(type(self._screen_img))
        return self._screen_img


if __name__ == '__main__':
    # DD = DisplayData(
    #     screen_res = {
    #         "w": 100,
    #         "h": 100
    #     },
    #     screen_img_dir = "..\\..\\..\\resources\\1920_1080_space.jpg"
    # )
    pass
