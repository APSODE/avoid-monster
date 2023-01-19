from src.GameFunc.settings.SettingDataObject import SettingDataObject
from src.GameFunc.display.DisplayManager import DisplayManager
from src.SettingGUI.SettingGUI_qt import SettingGUI
import pygame

class SettingManager:
    def __init__(self, dp_manager: DisplayManager):
        self._display_manager = dp_manager


    @property
    def DisplayManager(self) -> DisplayManager:
        return self._display_manager

    def ApplySetting_display(self, setting_data: SettingDataObject = None) -> pygame.Surface:
        screen_res = (
            self._display_manager.DisplayData.ScreenRes.width,
            self._display_manager.DisplayData.ScreenRes.height
        )
        display_surface = pygame.display.set_mode(screen_res)
        print(f"screen resolution : {screen_res}")
        pygame.display.set_caption("Avoid Moster | ver1.0")
        return display_surface

    @staticmethod
    def ApplySetting_key():
        pygame.key.set_repeat(5, 5)

