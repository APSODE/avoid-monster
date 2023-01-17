from typing import *
from src.GameFunc.item.ItemTypeEnum import ItemTypeEnum

class ItemBase:
    def __init__(self,
                 name: Optional[str] = None,
                 status: Optional[Dict[str, int]] = None,
                 item_type: Optional[ItemTypeEnum] = None):

        self._name = name if name is not None else "test item"

        if status is not None:
            self._status = status
        else:
            self._status = {
                "at_point": 100, #  at ==> attack || 공격력
                "df_point": 100, #  df ==> defense || 방어력
                "this_status_is_test_status": 0
            }

        self._item_type = item_type if item_type is not None else ItemTypeEnum.TEST_ITEM

    @property
    def Name(self) -> str:
        return self._name

    @property
    def Status(self) -> Dict[str, int]:
        return self._status

    @property
    def ItemType(self) -> ItemTypeEnum:
        return self._item_type

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()}
