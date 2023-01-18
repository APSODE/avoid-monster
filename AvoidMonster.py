from src.GameFunc.settings.SettingManager import SettingManager
from src.GameFunc.event.EventHandler import EventHandler
from src.GameFunc.CustomException.AvoidMonster_CE import GameQuitException
from src.GameFunc.player.TestPlayer import TestPlayer


import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) #프로젝트 루트의 절대 경로


class AvoidMonster:
    def __init__(self):
        self._work_status = True
        self._setting_manager = SettingManager(root_path = PROJECT_ROOT_PATH)
        self._screen: pygame.Surface

    def StartGame(self) -> None:
        # print(f"continue : {self._setting_manager.DisplayManager.DisplayData.ContinueInfo}")
        if self._setting_manager.DisplayManager.DisplayData.ContinueInfo is False:
            return None
        else:
            pygame.init()
            self._ApplyGameSetting()

            player = TestPlayer()
            player.MoveData.X_Pos = 250 # 테스트용 위치
            player.MoveData.Y_Pos = 250 # 테스트용 위치

            while self._work_status:
                for occurred_event in pygame.event.get():
                    try:
                        EventHandler(
                            event = occurred_event,
                            object_dict = {
                                "player": player,
                                "display": self._setting_manager.DisplayManager.DisplayData
                            }
                        )

                    except GameQuitException:
                        self._work_status = False

                self._screen.blit(self._setting_manager.DisplayManager.DisplayData.ScreenImage, (0, 0))
                self._screen.blit(player.PlayerSprite.sprite, (player.MoveData.X_Pos, player.MoveData.Y_Pos))
                pygame.display.update()

    def _ApplyGameSetting(self) -> None:
        self._screen = self._setting_manager.ApplySetting_display()
        SettingManager.ApplySetting_key()


if __name__ == '__main__':
    AM = AvoidMonster()
    AM.StartGame()
