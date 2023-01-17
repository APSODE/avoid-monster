from typing import *
from pygame.event import Event
from src.GameFunc.player.PlayerMoveData import PlayerMoveData, DirectionEnum
from src.GameFunc.player.PlayerBase import PlayerBase


class PlayerManager:
    def __init__(self, player_object: Optional[PlayerBase]):
        self._player_object = player_object

    def MovePlayer(self, direction: DirectionEnum):
        # player의 이동후 좌표 = <player의 speed> * <player의 이동방향에 따른 x,y좌표 연산자(-1, 0, 1)> + <player의 현재 좌표>
        player_speed = self._player_object.MoveData.Speed

        self._player_object.MoveData.X_Move = player_speed * direction.x_op
        self._player_object.MoveData.Y_Move = player_speed * direction.y_op

        self._player_object.MoveData.X_Pos += self._player_object.MoveData.X_Move
        self._player_object.MoveData.Y_Pos += self._player_object.MoveData.Y_Move
        self._player_object.MoveData.Direction = direction
        print(f"player x pos : {self._player_object.MoveData.X_Pos}")
        print(f"player y pos : {self._player_object.MoveData.Y_Pos}")






