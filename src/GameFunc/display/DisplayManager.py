from typing import *
from src.GameFunc.display.DisplayData import DisplayData, DisplayResolution


class DisplayManager:
    def __init__(self, gui_data: Dict[str, Union[int, bool]], root_path: str):
        self._display_data_object = DisplayData(
            screen_res = DisplayResolution.HD if gui_data.get("sc_res") == "hd" else DisplayResolution.FHD,
            screen_img_dir = f"{root_path}\\resources\\1920_1080_space.jpg" #테스트용 background image
        )

    @property
    def DisplayData(self) -> DisplayData:
        return self._display_data_object



