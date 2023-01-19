from src.GameFunc.player.PlayerBase import PlayerBase


class TestPlayer(PlayerBase):
    def __init__(self, object_name: str):
        super().__init__(obj_name = object_name)
