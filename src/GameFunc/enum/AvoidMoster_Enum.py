from enum import Enum


class DirectionEnum(Enum):
    RIGHT = ("right", 1, 0, 0)  # (name, x_operator, y_operator)
    LEFT = ("left", -1, 0, 0)
    UP = ("up", 0, -1, 90)
    DOWN = ("down", 0, 1, 270)
    UP_RIGHT = ("up_right", 1, -1, 45)
    UP_LEFT = ("up_left", -1, -1, 315)
    DOWN_RIGHT = ("down_right", 1, 1, 315)
    DOWN_LEFT = ("down_left", -1, 1, 45)
    NONE = ("none_direction", 0, 0, 0)

    def __init__(self, direction: str, x_op: int, y_op: int, rt_ag: int):
        """
        :param direction:  방향에 대한 문자열 정보
        :param x_op:  방향에 따른 x좌표 연산에 사용되는 연산자
        :param y_op:  방향에 따른 y좌표 연산에 사용되는 연산자
        :param rt_ag:  방향에 따른 스프라이트 회전 각도
        """
        self.direction_str = direction
        self.x_op = x_op
        self.y_op = y_op
        self.rt_ag = rt_ag

