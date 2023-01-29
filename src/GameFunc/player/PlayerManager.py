from typing import *
from src.GameFunc.enum.AvoidMoster_Enum import DirectionEnum
from src.GameFunc.player.PlayerBase import PlayerBase
from src.GameFunc.player.TestPlayer import TestPlayer
from src.GameFunc.display.DisplayData import DisplayResolution


class PlayerManager:
    def __init__(self, player_object: Optional[PlayerBase] = None):
        # PlayerManager객체가 관리를 담당하는 Player객체를 저장하는 클래스 변수
        self._player_object = player_object if player_object is not None else TestPlayer(object_name = "test player")

    # 클래스 변수에 접근하기 위한 Getter
    # 해당 클래스 변수는 처음 PlayerManager객체가 생성될때만 저장할 Player객체의 지정이 가능해야하므로
    # Getter메소드만 제작하고 Setter메소드는 제작하지 않는다.
    @property
    def PlayerObject(self) -> PlayerBase:
        return self._player_object

    # 플레이어의 이동을 구현하기 위하여 Player객체에 담겨있는 PlayerMoveData객체의 값을 수정한다.
    @staticmethod
    def MovePlayer(player_object: Optional[PlayerBase], direction: DirectionEnum, display_res: DisplayResolution):
        # player의 이동후 좌표 = <player의 speed> * <player의 이동방향에 따른 x,y좌표 연산자(-1, 0, 1)> + <player의 현재 좌표>

        # 플레이어의 속도
        player_speed = player_object.MoveData.Speed

        # 플레이어의 X, Y의 이동량
        player_mv_x = player_speed * direction.x_op
        player_mv_y = player_speed * direction.y_op

        # 플레이어의 현재 X, Y좌표
        player_x_pos = player_object.MoveData.X_Pos
        player_y_pos = player_object.MoveData.Y_Pos

        # 스크린 사이즈 경계 침범 체크
        x_pos_check = 0 <= player_x_pos + player_mv_x <= display_res.width - player_object.Sprite.size[0]
        y_pos_check = 0 <= player_y_pos + player_mv_y <= display_res.height - player_object.Sprite.size[1]

        # 스크린 경계를 침범하지 않는 경우에 플레이어의 이동 정보를 반영한다.
        if x_pos_check and y_pos_check:
            player_object.MoveData.MovingStatus = True
            player_object.MoveData.X_Move = player_speed * direction.x_op
            player_object.MoveData.Y_Move = player_speed * direction.y_op

            player_object.MoveData.X_Pos += player_object.MoveData.X_Move
            player_object.MoveData.Y_Pos += player_object.MoveData.Y_Move
            player_object.MoveData.Direction = direction
