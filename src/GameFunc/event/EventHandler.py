from pygame.event import Event
from pygame import *
from src.GameFunc.CustomException.AvoidMonster_CE import GameQuitException
from src.GameFunc.player.PlayerManager import PlayerManager
from src.GameFunc.player.TestPlayer import TestPlayer
from src.GameFunc.player.PlayerMoveData import DirectionEnum


class MoveEvent:
    @staticmethod
    def GetMoveDirection(event_key) -> DirectionEnum:
        if event_key == K_UP:
            return DirectionEnum.UP

        elif event_key == K_DOWN:
            return DirectionEnum.DOWN

        elif event_key == K_RIGHT:
            return DirectionEnum.RIGHT

        elif event_key == K_LEFT:
            return DirectionEnum.LEFT


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

    def _HandleKeyEvent(self):
        event_key = self._event.key

        if event_key in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
            self._HandleMoveEvent(
                direction = MoveEvent.GetMoveDirection(event_key)
            )

        elif event_key in [K_q, K_w, K_e, K_r]:
            self._HandleItemUseEvent()

    def _HandleMoveEvent(self, direction: DirectionEnum):
        player_manager = PlayerManager(self._object_dict.get("player"))
        player_manager.MovePlayer(direction)


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

