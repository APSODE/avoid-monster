from src.item.ItemBase import ItemBase
from src.item.ItemTypeEnum import ItemTypeEnum, EquipTypeEnum
from typing import Dict


class EquipmentItem(ItemBase):
    def __init__(self,
                 name: str = None,
                 status: Dict[str, int] = None,
                 item_type: ItemTypeEnum = None,
                 equipment_type: EquipTypeEnum = None
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
