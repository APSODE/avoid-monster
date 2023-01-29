from typing import *
from src.GameFunc.player.PlayerMoveData import PlayerMoveData
from src.GameFunc.player.PlayerSprite import PlayerSprite
from src.GameFunc.item.EquipmentItem import EquipmentItem


class PlayerBase:
    def __init__(self,
                 obj_name: str,
                 mv_data: Optional[PlayerMoveData] = None,
                 element: Optional[str] = None,
                 equipment: Optional[EquipmentItem] = None,
                 status: Optional[dict] = None,
                 sprite: Optional[PlayerSprite] = None
                 # skill: Optional[]
                 ):

        self._object_name = obj_name  # 객체의 이름을 저장하는 클래스 변수

        # 플레이어의 이동 정보를 담고 있는 객체를 저장하는 클래스 변수
        self._player_move_data = mv_data if mv_data is not None else PlayerMoveData()
        # 플레이어의 원소를 저장하는 클래스 변수
        self._element = element if element is not None else "test element"
        # 플레이어가 장비하고 있는 장비 아이템에 대한 정보를 담고 있는 객체를 저장하는 클래스 변수
        self._equipment = equipment if equipment is not None else EquipmentItem()
        # 플레이어의 스프라이트 정보를 담고있는 객체를 저장하는 클래스 변수
        self._sprite = sprite if sprite is not None else PlayerSprite()

        # 플레이어의 스테이터스를 저장하는 클래스 변수
        if status is not None:
            self._status = status
        else:
            self._status = {
                "attack": 10,
                "defense": 10,
                "this status is test status": 0
            }

    # 각각의 클래스 변수에 접근하기위한 Getter와 Setter
    @property
    def ObjectName(self) -> str:
        # print(f"object_name : {self._object_name}")
        return self._object_name

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

    @property
    def Sprite(self) -> PlayerSprite:
        return self._sprite

    @Sprite.setter
    def Sprite(self, value: PlayerSprite):
        self._sprite = value

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}
