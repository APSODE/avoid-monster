from typing import *
from pygame.event import Event
from pygame import *
from src.GameFunc.CustomException.AvoidMonster_CE import GameQuitException
from src.GameFunc.player.PlayerManager import PlayerManager
from src.GameFunc.player.TestPlayer import TestPlayer
from src.GameFunc.player.PlayerMoveData import DirectionEnum


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
    def __init__(self, event: Event, object_dict: dict):
        self._event = event
        self._event_type = event.type
        self._object_dict = object_dict

        self._CheckEvent()

    def _CheckEvent(self):
        if self._event_type in [KEYDOWN, KEYUP]:
            self._HandleKeyEvent()

        elif self._event_type == QUIT:
            raise GameQuitException()

    @staticmethod
    def _KeyNumberChanger(k_value: int) -> Optional[int]:
        if k_value == 82:
            return K_UP
        elif k_value == 81:
            return K_DOWN
        elif k_value == 79:
            return K_RIGHT
        elif k_value == 80:
            return K_LEFT
        else:
            return None



    def _HandleKeyEvent(self):
        pressed = key.get_pressed() #동시 입력 대비를 위한 키바인딩

        # 실제 입력이 있었던 키만 따로 리스트 속에 담음
        event_key = [self._KeyNumberChanger(k_value = k) for k,v in enumerate(pressed) if v]

        # print(MoveEvent.GetMoveDirection(event_key))
        if event_key != [] and None not in event_key: # 생성된 event_key 리스트가 비어있는지 확인
            if event_key < [K_UP, K_DOWN, K_RIGHT, K_LEFT]: # 리스트 부분집합 여부로 동시 키입력 확인
                # print("작동")
                self._HandleMoveEvent(
                    direction = MoveEvent.GetMoveDirection(event_key)
                )


            elif event_key in {K_q, K_w, K_e, K_r}:
                self._HandleItemUseEvent()

    def _HandleMoveEvent(self, direction: DirectionEnum):
        player_manager = PlayerManager(self._object_dict.get("player"))
        player_manager.MovePlayer(
            direction = direction,
            display_res = self._object_dict.get("display").ScreenRes
        )


    def _HandleItemUseEvent(self):
        pass

    def _HandleQuitEvent(self) -> bool:
        return True

    # @staticmethod
    # def KeyEvent(game_event, event_type):
    #     """
    #     :param game_instance: AvoidMonster.py의 게임 인스턴스를 전달받는 파라미터
    #     :param game_event: AvoidMonster.py의 게임 인스턴스 안에서 발생하는 이벤트
    #     :return:
    #     """
    #     event_type = game_event.type
    #
    #     if event_type == game_instance.KEYDOWN:
    #         event_key = game_event.key
    #
    #         if event_key in [game_instance.K_UP, game_instance.K_DOWN, game_instance.K_RIGHT, game_instance.K_LEFT]:
    #             if
    #
    #

