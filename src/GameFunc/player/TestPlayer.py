from src.GameFunc.player.PlayerBase import PlayerBase


class TestPlayer(PlayerBase):
    def __init__(self, object_name: str):
        # 상속받은 PlayerBase클래스를 초기화하기 위하여 super().__init__()을 호출한다.
        # 여기서 super()은 해당 클래스가 상속받은 super class를 의미하며
        # 따라서 super().__init__()은 super class의 생성자 메소드를 호출하는 것을 의미한다.
        super().__init__(obj_name = object_name)
