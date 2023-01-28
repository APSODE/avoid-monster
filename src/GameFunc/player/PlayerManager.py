from typing import *
from src.decorator.ErrorChecker import ErrorChecker
from src.GameFunc.enum.AvoidMoster_Enum import DirectionEnum
from src.GameFunc.player.PlayerBase import PlayerBase
from src.GameFunc.player.TestPlayer import TestPlayer
from src.GameFunc.display.DisplayData import DisplayData, DisplayResolution


class PlayerManager:
    def __init__(self, player_object: Optional[PlayerBase] = None):
        self._player_object = player_object if player_object is not None else TestPlayer(object_name = "test player")

    @property
    def PlayerObject(self) -> PlayerBase:
        return self._player_object

    @staticmethod
    def MovePlayer(player_object: Optional[PlayerBase], direction: DirectionEnum, display_res: DisplayResolution):
        # player의 이동후 좌표 = <player의 speed> * <player의 이동방향에 따른 x,y좌표 연산자(-1, 0, 1)> + <player의 현재 좌표>
        player_speed = player_object.MoveData.Speed

        player_mv_x = player_speed * direction.x_op
        player_mv_y = player_speed * direction.y_op

        player_x_pos = player_object.MoveData.X_Pos
        player_y_pos = player_object.MoveData.Y_Pos

        # 스크린 사이즈 경계 침범 체크
        x_pos_check = 0 <= player_x_pos + player_mv_x <= display_res.width - player_object.Sprite.size[0]
        y_pos_check = 0 <= player_y_pos + player_mv_y <= display_res.height - player_object.Sprite.size[1]

        if x_pos_check and y_pos_check:
            player_object.Sprite.WalkAnimation() #TODO 플레이어 애니메이션을 한곳에서 관리하도록 해야함
            player_object.MoveData.X_Move = player_speed * direction.x_op
            player_object.MoveData.Y_Move = player_speed * direction.y_op

            player_object.MoveData.X_Pos += player_object.MoveData.X_Move
            player_object.MoveData.Y_Pos += player_object.MoveData.Y_Move
            player_object.MoveData.Direction = direction

            # print(f"player x pos : {self._player_object.MoveData.X_Pos}")
            # print(f"player y pos : {self._player_object.MoveData.Y_Pos}")
