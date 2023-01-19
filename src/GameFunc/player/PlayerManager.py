from typing import *
from src.decorator.ErrorChecker import ErrorChecker
from src.GameFunc.player.PlayerMoveData import DirectionEnum
from src.GameFunc.player.PlayerBase import PlayerBase
from src.GameFunc.player.TestPlayer import TestPlayer
from src.GameFunc.display.DisplayData import DisplayData, DisplayResolution


class PlayerManager:
    def __init__(self):
        self._player_container = {

        }

    def AddPlayerObjectToContainer(self, player_object: PlayerBase):
        self._player_container[player_object.ObjectName] = player_object

    @property
    def PlayerContainer(self) -> Dict[str, PlayerBase]:
        return self._player_container

    @staticmethod
    def MovePlayer(player_object: Optional[TestPlayer], direction: DirectionEnum, display_res: DisplayResolution):
        # player의 이동후 좌표 = <player의 speed> * <player의 이동방향에 따른 x,y좌표 연산자(-1, 0, 1)> + <player의 현재 좌표>
        player_speed = player_object.MoveData.Speed

        player_mv_x = player_speed * direction.x_op
        player_mv_y = player_speed * direction.y_op

        player_x_pos = player_object.MoveData.X_Pos
        player_y_pos = player_object.MoveData.Y_Pos

        x_pos_check = 0 <= player_x_pos + player_mv_x <= display_res.width - player_object.Sprite.size[0] # 스크린 사이즈 경계 침범 체크
        y_pos_check = 0 <= player_y_pos + player_mv_y <= display_res.height - player_object.Sprite.size[1] # 스크린 사이즈 경계 침범 체크

        if x_pos_check and y_pos_check:
            player_object.MoveData.X_Move = player_speed * direction.x_op
            player_object.MoveData.Y_Move = player_speed * direction.y_op

            player_object.MoveData.X_Pos += player_object.MoveData.X_Move
            player_object.MoveData.Y_Pos += player_object.MoveData.Y_Move
            player_object.MoveData.Direction = direction

            # print(f"player x pos : {self._player_object.MoveData.X_Pos}")
            # print(f"player y pos : {self._player_object.MoveData.Y_Pos}")
