from typing import Dict, Optional
from enum import Enum


class DirectionEnum(Enum):
    RIGHT = ("right", 1, 0)
    LEFT = ("left", -1, 0)
    UP = ("up", 0, -1)
    DOWN = ("down", 0, 1)

    def __init__(self, direction: str, x_op: int, y_op: int):
        """
        :param direction:  방향에 대한 문자열 정보
        :param x_op:  방향에 따른 x좌표 연산에 사용되는 연산자
        :param y_op:  방향에 따른 y좌표 연산에 사용되는 연산자
        """
        self.direction_str = direction
        self.x_op = x_op
        self.y_op = y_op


class PlayerMoveData:
    def __init__(self,
                 pos_data: Optional[Dict[str, int]] = None,
                 mv_data: Optional[Dict[str, int]] = None,
                 speed: Optional[int] = None,
                 direction: Optional[DirectionEnum] = None
                 ):

        """pos_data ==> x, y를 key로 가지고 value에 int타입의 값을 가진다"""

        self._x_pos = pos_data.get("x") if pos_data is not None else 0
        self._y_pos = pos_data.get("y") if pos_data is not None else 0

        self._mv_x = mv_data.get("x") if mv_data is not None else 0
        self._mv_y = mv_data.get("y") if mv_data is not None else 0

        self._speed = speed if speed is not None else 1

        self._direction = direction if direction is not None else DirectionEnum.UP

    @property
    def X_Pos(self) -> int:
        return self._x_pos

    @X_Pos.setter
    def X_Pos(self, value: int):
        self._x_pos = value

    @property
    def Y_Pos(self) -> int:
        return self._y_pos

    @Y_Pos.setter
    def Y_Pos(self, value: int):
        self._y_pos = value

    @property
    def X_Move(self) -> int:
        return self._mv_x

    @X_Move.setter
    def X_Move(self, value: int):
        self._mv_x = value

    @property
    def Y_Move(self) -> int:
        return self._mv_y

    @Y_Move.setter
    def Y_Move(self, value: int):
        self._mv_y = value

    @property
    def Speed(self) -> int:
        return self._speed

    @Speed.setter
    def Speed(self, value: int):
        self._speed = value

    @property
    def Direction(self) -> DirectionEnum:
        return self._direction

    @Direction.setter
    def Direction(self, value: DirectionEnum):
        self._direction = value

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}