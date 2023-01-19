from src.GameFunc.settings.SettingManager import SettingManager
from src.GameFunc.display.DisplayManager import DisplayManager
from src.GameFunc.player.PlayerManager import PlayerManager
from src.SettingGUI.SettingGUI_qt import SettingGUI


class ObjectContainer:
    def __init__(self, root_path: str):
        self._display_manager = DisplayManager(gui_data = SettingGUI.Start(), root_path = root_path)
        self._setting_manager = SettingManager(dp_manager = self._display_manager)
        self._player_manager = PlayerManager()

    @property
    def DisplayManager(self) -> DisplayManager:
        return self._display_manager

    @property
    def SettingManager(self) -> SettingManager:
        return self._setting_manager

    @property
    def PlayerManager(self) -> PlayerManager:
        return self._player_manager
