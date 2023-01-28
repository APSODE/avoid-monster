from typing import *
from src.GameFunc.display.DisplayData import DisplayData, DisplayResolution
from src.GameFunc.player.PlayerBase import PlayerBase


import pygame

DOT = TypeVar("DOT", PlayerBase, DisplayData)


class DisplayManager:
    def __init__(self, gui_data: Dict[str, Union[int, bool]], root_path: str):
        self._display_data_object = DisplayData(
            screen_res = DisplayResolution.HD if gui_data.get("sc_res") == "hd" else DisplayResolution.FHD,
            screen_img_dir = f"{root_path}\\resources\\1920_1080_space.jpg",  # test background image
            cont = gui_data.get("continue")
        )

    @property
    def DisplayData(self) -> DisplayData:
        return self._display_data_object

    def DrawObject(self, screen: pygame.Surface, target_objects: List[DOT]):
        for target_object in target_objects:
            if isinstance(target_object, PlayerBase):
                target_object.Sprite.UpdateSprite(move_data = target_object.MoveData)
                screen.blit(
                    target_object.Sprite.sprite_sf,
                    (
                        target_object.MoveData.X_Pos,
                        target_object.MoveData.Y_Pos
                    )
                )
                if target_object.MoveData.MovingStatus:
                    target_object.MoveData.MovingStatus = False

            elif isinstance(target_object, DisplayData):
                screen.blit(target_object.ScreenImage, (0, 0))

        pygame.display.update()
