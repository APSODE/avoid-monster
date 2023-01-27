from typing import *
from src.GameFunc.monster.MonsterMoveData import MonsterMoveData
from src.GameFunc.monster.MonsterSprite import MonsterSprite


class MonsterBase:
    def __init__(self,
                 obj_name: Optional[str] = None,
                 mv_data: Optional[MonsterMoveData] = None,
                 sprite: Optional[MonsterSprite] = None,
                 status: Optional[dict] = None
                 ):

        self._object_name = obj_name if obj_name is not None else "test monster name"

        self._monster_move_data = mv_data if mv_data is not None else MonsterMoveData()
        self._sprite = sprite if sprite is not None else MonsterSprite

        if status is not None:
            self._status = status
        else:
            self._status = {
                "attack": 10,
                "defense": 10,
                "this status is test status": 0
            }

    @property
    def ObjectName(self) -> str:
        # print(f"object_name : {self._object_name}")
        return self._object_name

    @property
    def MoveData(self) -> MonsterMoveData:
        return self._monster_move_data

    @MoveData.setter
    def MoveData(self, value: MonsterMoveData):
        self._monster_move_data = value

    @property
    def Sprite(self) -> MonsterSprite:
        return self._sprite

    @Sprite.setter
    def Sprite(self, value: MonsterSprite):
        self._sprite = value

    @property
    def Status(self) -> Dict[str, int]:
        return self._status

    @Status.setter
    def Status(self, value: Dict[str, int]):
        self._status = value

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}
