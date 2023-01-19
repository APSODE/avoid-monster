from src.GameFunc.CustomException.AvoidMonster_CE import GameQuitException
from src.GameFunc.player.TestPlayer import TestPlayer


import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) #프로젝트 루트의 절대 경로


class AvoidMonster:
    def __init__(self):
        # Circular Import Exceprion을 방지하기 위하여 ObjectContainer의 import 타임을 runtime때 호출되도록 변경
        from src.GameFunc.container.ObjectContainer import ObjectContainer
        self._work_status = True
        self._object_container = ObjectContainer(root_path = PROJECT_ROOT_PATH)
        self._screen: pygame.Surface

    def StartGame(self) -> None:
        # print(f"continue : {self._setting_manager.DisplayManager.DisplayData.ContinueInfo}")
        if self._object_container.DisplayManager.DisplayData.ContinueInfo is False:
            return None
        else:
            pygame.init()
            self._ApplyGameSetting()

            player = TestPlayer(object_name = "test_player_object")
            player.MoveData.X_Pos = 250 # 테스트용 위치
            player.MoveData.Y_Pos = 250 # 테스트용 위치

            self._object_container.PlayerManager.AddPlayerObjectToContainer(player_object = player)
            player = self._object_container.PlayerManager.PlayerContainer.get("test_player_object")

            while self._work_status:
                for occurred_event in pygame.event.get():
                    try:
                        # Circular Import Exceprion을 방지하기 위하여 EventHandler의 import 타임을 runtime때 호출되도록 변경
                        from src.GameFunc.event.EventHandler import EventHandler
                        EventHandler(
                            event = occurred_event,
                            object_container = self._object_container
                        )

                    except GameQuitException:
                        self._work_status = False

                self._screen.blit(self._object_container.DisplayManager.DisplayData.ScreenImage, (0, 0))
                self._screen.blit(player.Sprite.sprite_sf, (player.MoveData.X_Pos, player.MoveData.Y_Pos))
                pygame.display.update()

    def _ApplyGameSetting(self) -> None:
        self._screen = self._object_container.SettingManager.ApplySetting_display()
        self._object_container.SettingManager.ApplySetting_key()


if __name__ == '__main__':
    AM = AvoidMonster()
    AM.StartGame()
