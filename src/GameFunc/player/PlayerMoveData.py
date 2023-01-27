from typing import *
from src.GameFunc.enum.AvoidMoster_Enum import DirectionEnum


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

        self._speed = speed if speed is not None else 1  # 테스트를 위해 속도 수정  ||  1(기존) -> 10(수정후)

        self._direction = direction if direction is not None else DirectionEnum.NONE

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
