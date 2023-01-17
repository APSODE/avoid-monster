from typing import *
from src.GameFunc.player.PlayerMoveData import PlayerMoveData
from src.GameFunc.item.EquipmentItem import EquipmentItem



class PlayerBase:
    def __init__(self,
                 mv_data: Optional[PlayerMoveData] = None,
                 element: Optional[str] = None,
                 equipment: Optional[EquipmentItem] = None,
                 status: Optional[dict] = None
                 # skill: Optional[]
                ):

        self._player_move_data = mv_data if mv_data is not None else PlayerMoveData()
        self._element = element if element is not None else "test element"
        self._equipment = equipment if equipment is not None else EquipmentItem()

        if status is not None:
            self._status = status
        else:
            self._status = {
                "attack": 10,
                "defense": 10,
                "this status is test status": 0
            }

    @property
    def MoveData(self) -> PlayerMoveData:
        return self._player_move_data

    @MoveData.setter
    def MoveData(self, value: PlayerMoveData):
        self._player_move_data = value

    # element클래스 변수는 객체가 생성된 이후에 현재로썬 수정될 일이 없으므로 setter은 제작하지 않는다.
    @property
    def Element(self):
        return self._element

    @property
    def Equipment(self) -> EquipmentItem:
        return self._equipment

    @Equipment.setter
    def Equipment(self, value: EquipmentItem):
        self._equipment = value

    @property
    def Status(self) -> Dict[str, int]:
        return self._status

    @Status.setter
    def Status(self, value: Dict[str, int]):
        self._status = value

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}

