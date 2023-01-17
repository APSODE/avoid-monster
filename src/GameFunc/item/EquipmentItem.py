from src.GameFunc.item.ItemBase import ItemBase
from src.GameFunc.item.ItemTypeEnum import ItemTypeEnum, EquipTypeEnum
from typing import *


class EquipmentItem(ItemBase):
    def __init__(self,
                 name: Optional[str] = None,
                 status: Optional[Dict[str, int]] = None,
                 item_type: Optional[ItemTypeEnum] = None,
                 equipment_type: Optional[EquipTypeEnum] = None
                 ):

        super(EquipmentItem, self).__init__(
            name = name,
            status = status,
            item_type = item_type
        )

        if equipment_type is not None:
            self._equipment_type = equipment_type
        else:
            self._equipment_type = EquipTypeEnum.TEST_EQUIPMENT

    @property
    def EquipmentType(self) -> EquipTypeEnum:
        return self._equipment_type

    def __repr__(self):
        return f"\n====== <EquipmentItem Object Data> ======\n" \
               f"name : {self._name}\n" \
               f"status : {self._status}\n" \
               f"item type : {self._item_type}\n" \
               f"equipment type : {self._equipment_type}\n" \
               f"\n"

if __name__ == '__main__':
    EI_OBJ = EquipmentItem()
    print(EI_OBJ)
    print(EI_OBJ.GetAllData())
