from src.GameFunc.settings.SettingManager import SettingManager
from src.SettingGUI.SettingGUI_qt import SettingGUI
from src.GameFunc.event.EventHandler import EventHandler
from src.GameFunc.CustomException.AvoidMonster_CE import GameQuitException
from src.GameFunc.player.TestPlayer import TestPlayer

import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) #프로젝트 루트의 절대 경로


class AvoidMonster:
    def __init__(self):
        self.gui_data = SettingGUI.Start()
        self.work_status = True

    def StartGame(self) -> None:
        if self.gui_data.get("continue") is False:
            return None
        else:
            pygame.init()
            # self._ApplyGameSetting(instance = pygame)
            screen = pygame.display.set_mode((500, 500))
            pygame.display.set_caption("Avoid Moster | ver1.0")

            player = TestPlayer()
            player.MoveData.X_Pos = 250
            player.MoveData.Y_Pos = 250

            while self.work_status:
                for occurred_event in pygame.event.get():
                    try:
                        EventHandler(
                            event = occurred_event,
                            object_dict = {
                                "player": player
                            }
                        )

                    except GameQuitException:
                        self.work_status = False

                screen.blit(player.PlayerSprite.surf, (player.MoveData.X_Pos, player.MoveData.Y_Pos))
                pygame.display.update()

    @staticmethod
    def _ApplyGameSetting(instance) -> None:
        SettingManager.ApplySetting_display(instance)

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
