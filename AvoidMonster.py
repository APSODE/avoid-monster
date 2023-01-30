from src.GameFunc.custom_exception.AvoidMonster_CE import GameQuitException
from src.GameFunc.display.DisplayManager import DisplayManager


import os
import pygame

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 프로젝트 루트의 절대 경로


class AvoidMonster:
    def __init__(self, debug_mode: bool = False):
        # Circular Import Exception을 방지하기 위하여 ObjectContainer의 import 타임을 runtime때 호출되도록 변경
        from src.GameFunc.container.ObjectContainer import ObjectContainer
        self._work_status = True  # 게임의 작동 상태를 나타내는 클래스 변수

        # 각종 Manager를 담고있는 컨테이너 객체
        self._object_container = ObjectContainer(
            root_path = PROJECT_ROOT_PATH,
            debug_mode = debug_mode
        )
        self._screen = self._object_container.SettingManager.Screen  # 게임 화면의 Surface객체를 담고 있는 클래스 변수
        self._clock = pygame.time.Clock()  # 인게임의 시간 정보를 가지는 객체

    def StartGame(self) -> None:
        # 게임 실행시 그래픽 옵션을 선택하는 GUI에서 게임 실행 명령이 전달되었는지 확인
        if self._object_container.DisplayManager.DisplayData.ContinueInfo is False:
            return None

        else:
            pygame.init()  # pygame모듈을 초기화

            # ObjectContainer에 존재하는 PlayerManager객체에서 플레이어 객체를 가져온다.
            # 기본값은 TestPlayer이므로 실제 구동때는 캐릭터 선택을 통해 플레이어 객체를 수정해야 한다.
            player = self._object_container.PlayerManager.PlayerObject

            # 게임의 작동을 위한 반복문
            while self._work_status:
                # while 반복문이 작동하고 있으면 매번 pygame.event.get()이 호출되어 게임에서 발생된 이벤트를 가져온다.
                for occurred_event in pygame.event.get():  # for을 통해 발생된 이벤트를 occured_event에 담는다.
                    try:
                        # Circular Import Exception을 방지하기 위하여 EventHandler의 import 타임을 runtime때 호출되도록 변경
                        from src.GameFunc.event.EventHandler import EventHandler
                        # 발생된 이벤트를 핸들링하기 위해 EventHandler객체를 생성하고 생성자 메소드의 파라미터로 occured_event를 전달.
                        # 그리고 이벤트에 따른 데이터 값의 변경과 반영을 위해 ObjectContainer객체도 같이 전달한다.
                        EventHandler(
                            event = occurred_event,
                            object_container = self._object_container
                        )

                    # EventHandler에서 유저가 종료 이벤트를 발생시키면 EventHandler는 GameQuitException을 발생시킨다.
                    # 이렇게 종료이벤트가 발생하면 try-except를 통해 게임 작동 상태를 수정한다.
                    except GameQuitException:
                        self._work_status = False

                # DisplayManager클래스의 DrawObject메소드는
                # 디스플레이에 표시할 대상의 Surface객체를 가지고 있는 객체를 담고 있는 리스트를 파라미터로 받는다.
                draw_target_object = [
                    self._object_container.DisplayManager.DisplayData,
                    player
                ]
                self._object_container.DisplayManager.DrawObject(
                    target_objects = draw_target_object,
                    screen = self._screen
                )

                self._clock.tick(60)  # 60프레임

                # 변경된 사항을 실제 게임화면에 적용한다.
                pygame.display.update()


if __name__ == '__main__':
    AM = AvoidMonster(debug_mode = True)  # AvoidMonster객체 생성
    AM.StartGame()  # 게임 시작
