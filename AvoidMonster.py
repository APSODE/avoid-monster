from src.GameFunc.settings.SettingManager import SettingManager

import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) #프로젝트 루트의 절대 경로

class AvoidMonster:
    def __init__(self):
        self.game_instance = pygame
        self.work_status = True

    def StartGame(self) -> None:
        self.game_instance.init()
        self._ApplyGameSetting()

        while self.work_status:
            pass

    def _ApplyGameSetting(self) -> None:
        SettingManager.ApplySetting_display(instance = self.game_instance)

    # @staticmethod
    # def StartGame() -> None:
    #     game_instance = pygame
    #     game_instance.init()
    #     SettingManager.ApplySetting_display(
    #         instance = game_instance
    #     )
    #
    #     while True:
    #         game_instance.event.get()


if __name__ == '__main__':
    AM = AvoidMonster()
    AM.StartGame()
