from src.GameFunc.settings.SettingDataObject import SettingDataObject
from src.GameFunc.display.DisplayManager import DisplayManager
from typing import *

import pygame


class SettingManager:
    def __init__(self, dp_manager: DisplayManager):
        # Display의 정보를 게임화면에 반영하기 위해 DisplayData객체에 접근할 필요가 있으므로
        # DisplayManager객체를 생성자 메소드의 파라미터로 DisplayManager객체를 전달받는다.
        self._display_manager = dp_manager
        # 실제 게임화면의 Surface객체를 담고있는 클래스 변수
        self._screen = self.ApplySetting_display()
        # 게임에서 키입력 신호의 주기를 지정
        self.ApplySetting_key()

    # 각각의 클래스 변수에 접근하기 위한 Getter.
    @property
    def DisplayManager(self) -> DisplayManager:
        return self._display_manager

    @property
    def Screen(self) -> pygame.Surface:
        return self._screen

    # 게임 실행시 전달 받은 디스플레이 옵션을 적용하고 적용된 디스플레이의 Surface객체를 리턴한다.
    def ApplySetting_display(self, setting_data: SettingDataObject = None) -> pygame.Surface:
        screen_res = (
            self._display_manager.DisplayData.ScreenRes.width,
            self._display_manager.DisplayData.ScreenRes.height
        )
        display_surface = pygame.display.set_mode(screen_res)
        print(f"screen resolution : {screen_res}")
        pygame.display.set_caption("Avoid Moster | ver1.0")
        return display_surface

    # 키입력의 딜레이와 간격을 지정한다.
    @staticmethod
    def ApplySetting_key():
        pygame.key.set_repeat(5, 5)

