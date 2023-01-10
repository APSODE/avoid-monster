from enum import Enum


class ItemTypeEnum(Enum):
    EQUIPMENT = "equipment" #장비아이템
    TEST_ITEM = "test item" #테스트아이템 (아이템 타입의 기본값으로 사용 예정)

class EquipTypeEnum(Enum):
    SWORD = "sword" # 검
    SPEAR = "spear" # 창
    BOW = "bow" # 활
    SHIELD = "shield" # 방패

    TEST_EQUIPMENT = "test equipment type"