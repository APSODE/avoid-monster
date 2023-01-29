from typing import *
from pygame.event import Event
from pygame import *
from src.GameFunc.custom_exception.AvoidMonster_CE import GameQuitException
from src.GameFunc.container.ObjectContainer import ObjectContainer
from src.GameFunc.enum.AvoidMoster_Enum import DirectionEnum


class MoveEvent:
    @staticmethod
    def GetMoveDirection(event_key) -> DirectionEnum:
        if event_key.__len__() == 1:
            if event_key == [K_UP]:
                return DirectionEnum.UP

            elif event_key == [K_DOWN]:
                return DirectionEnum.DOWN

            elif event_key == [K_RIGHT]:
                return DirectionEnum.RIGHT

            elif event_key == [K_LEFT]:
                return DirectionEnum.LEFT

        elif event_key.__len__() == 2:
            if event_key in [[K_UP, K_RIGHT], [K_RIGHT, K_UP]]:
                return DirectionEnum.UP_RIGHT

            elif event_key in [[K_UP, K_LEFT], [K_LEFT, K_UP]]:
                return DirectionEnum.UP_LEFT

            elif event_key in [[K_DOWN, K_RIGHT], [K_RIGHT, K_DOWN]]:
                return DirectionEnum.DOWN_RIGHT

            elif event_key in [[K_DOWN, K_LEFT], [K_LEFT, K_DOWN]]:
                return DirectionEnum.DOWN_LEFT

            elif event_key in [[K_RIGHT, K_LEFT], [K_LEFT, K_RIGHT], [K_UP, K_DOWN], [K_DOWN, K_UP]]:
                return DirectionEnum.NONE

        elif event_key.__len__() >= 3:
            return DirectionEnum.NONE


class EventHandler:
    def __init__(self, event: Event, object_container: ObjectContainer):
        self._event = event  # 핸들링 대상 이벤트가 담겨있는 클래스 변수
        self._event_type = event.type  # 핸들링 대상 이벤트의 이벤트 타입
        self._object_container = object_container  # 데이터 값의 변경과 반영을 위해 전달받은 ObjectContainer 객체

        # 생성자 메소드 속에서 EventHandler._CheckEvent()를 호출하므로
        # EventHandler객체가 생성될때 자동으로 EventHandler._CheckEvent()가 호출된다.
        self._CheckEvent()

    # 발생된 이벤트의 타입을 분류하는 메소드
    def _CheckEvent(self):
        # 발생된 이벤트의 타입이 [KEYDOWN, KEYUP]에 포함된 이벤트 타입이면 _HandleKeyEvent호출
        if self._event_type in [KEYDOWN, KEYUP]:
            self._HandleKeyEvent()

        # 발생된 이벤트의 타입이 종료 이벤트이면 GameQuitException 생성
        elif self._event_type == QUIT:
            raise GameQuitException()

    # pressed에서 전달받은 키의 int값은 이벤트에서 사용되는 키의 int값과 다르므로 변환을 필요하다.
    # 따라서 이 메소드는 전달받은 키의 int값을 이벤트에서 사용할 수 있는 int값으로 변환을 해준다.
    @staticmethod
    def _KeyNumberChanger(k_value: int) -> Optional[int]:
        if k_value == 82:
            return K_UP  # 이러한 키의 변수는 선언부에 int형으로 선언되어 있다.
        elif k_value == 81:
            return K_DOWN
        elif k_value == 79:
            return K_RIGHT
        elif k_value == 80:
            return K_LEFT
        else:
            return None  # undefined key input

    # 키에 대한 이벤트가 발생하면 해당 메소드가 호출된다.
    def _HandleKeyEvent(self):
        pressed = key.get_pressed()  # 동시 입력 대비를 위한 키바인딩

        # 실제 입력이 있었던 키만 따로 리스트 속에 담음
        event_key = [self._KeyNumberChanger(k_value = k) for k, v in enumerate(pressed) if v]

        # print(MoveEvent.GetMoveDirection(event_key))
        if event_key != [] and None not in event_key:  # 생성된 event_key 리스트가 비어있는지 확인
            if event_key < [K_UP, K_DOWN, K_RIGHT, K_LEFT]:  # 리스트 부분집합 여부로 동시 키입력 확인
                # 입력된 키가 위, 아래, 오른쪽, 왼쪽 방향키일 경우 플레이어의 움직임에 대한 명령이 전달된것 이므로
                # EventHandler._HandleMoveEvent()메소드를 호출하여 움직임에 대한 기능을 수행한다.
                self._HandleMoveEvent(
                    direction = MoveEvent.GetMoveDirection(event_key)
                )

            elif event_key in [K_q, K_w, K_e, K_r]:  # 아이템 사용 이벤트 이지만 아직 미완성 상태
                self._HandleItemUseEvent()  # 아이템 사용 이벤트 이지만 아직 미완성 상태

    # 플레이어의 움직임에 대한 키 입력이 들어오면 호출되는 메소드
    def _HandleMoveEvent(self, direction: DirectionEnum):
        player_manager = self._object_container.PlayerManager
        player_manager.MovePlayer(
            player_object = self._object_container.PlayerManager.PlayerObject,
            direction = direction,
            display_res = self._object_container.DisplayManager.DisplayData.ScreenRes
        )

    def _HandleItemUseEvent(self):
        pass

    def _HandleQuitEvent(self) -> bool:
        return True
