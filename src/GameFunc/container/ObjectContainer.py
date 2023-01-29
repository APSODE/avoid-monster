from src.GameFunc.settings.SettingManager import SettingManager
from src.GameFunc.display.DisplayManager import DisplayManager
from src.GameFunc.player.PlayerManager import PlayerManager
from src.SettingGUI.SettingGUI_qt import SettingGUI


class ObjectContainer:
    def __init__(self, root_path: str):
        # Display에 대한 관리를 담당하는 Manager객체
        # DisplayManager는 게임의 디스플레이 옵션을 반영하기 위한 정보를 담고 있어야 하므로
        # Manager객체가 생성될때 GUI를 생성하는 메소드를 호출하여 디스플레이 옵션을 GUI를 통해서 전달받는다.
        self._display_manager = DisplayManager(gui_data = SettingGUI.Start(), root_path = root_path)
        # Setting에 대한 관리를 담당하는 Manager객체
        self._setting_manager = SettingManager(dp_manager = self._display_manager)
        # Player에 대한 관리를 담당하는 Manager객체
        self._player_manager = PlayerManager()

    # 각각의 Manager를 담고있는 클래스 변수에 접근하기 위한 Getter
    @property
    def DisplayManager(self) -> DisplayManager:
        return self._display_manager

    @property
    def SettingManager(self) -> SettingManager:
        return self._setting_manager

    @property
    def PlayerManager(self) -> PlayerManager:
        return self._player_manager
