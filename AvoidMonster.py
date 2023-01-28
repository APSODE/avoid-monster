from src.GameFunc.custom_exception.AvoidMonster_CE import GameQuitException


import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 프로젝트 루트의 절대 경로


class AvoidMonster:
    def __init__(self):
        # Circular Import Exception을 방지하기 위하여 ObjectContainer의 import 타임을 runtime때 호출되도록 변경
        from src.GameFunc.container.ObjectContainer import ObjectContainer
        self._work_status = True
        self._object_container = ObjectContainer(root_path = PROJECT_ROOT_PATH)
        self._screen = self._object_container.SettingManager.Screen
        self._clock = pygame.time.Clock()

    def StartGame(self) -> None:
        if self._object_container.DisplayManager.DisplayData.ContinueInfo is False:
            return None
        else:
            pygame.init()
            player = self._object_container.PlayerManager.PlayerObject

            while self._work_status:
                for occurred_event in pygame.event.get():
                    try:
                        # Circular Import Exception을 방지하기 위하여 EventHandler의 import 타임을 runtime때 호출되도록 변경
                        from src.GameFunc.event.EventHandler import EventHandler
                        EventHandler(
                            event = occurred_event,
                            object_container = self._object_container
                        )

                    except GameQuitException:
                        self._work_status = False

                draw_target_object = [
                    self._object_container.DisplayManager.DisplayData,
                    player
                ]
                self._object_container.DisplayManager.DrawObject(
                    target_objects = draw_target_object,
                    screen = self._screen
                )

                self._clock.tick(60)  # 60프레임


if __name__ == '__main__':
    AM = AvoidMonster()
    AM.StartGame()
