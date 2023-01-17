from PyQt5.QtWidgets import *
from PyQt5 import uic
from typing import Dict, Union
import sys
import os



qt_designer_class = uic.loadUiType(uifile = f"{os.path.dirname(os.path.abspath(__file__))}\\SettingGUI_qt.ui")[0]

class SettingGUI(QDialog, qt_designer_class):
    def __init__(self):
        self._setting_data = {
            "sc_mode": "window", #default value
            "sc_res": "hd", #default value
            "continue": False
        }
        super().__init__()
        self.setupUi(self)

        # self.OkButton.clicked.connect(self._ContinueCheck)
        # self.CancleButton.clicked.connect(self._ContinueCheck)
        self.OkCancleButtonBox.accepted.connect(self._ContinueCheck_Accept)
        self.OkCancleButtonBox.rejected.connect(self._ContinueCheck_Reject)

        self.ScreenModeFull.clicked.connect(self._GraphicSetting_ScreenMode)
        self.ScreenModeWindow.clicked.connect(self._GraphicSetting_ScreenMode)

        self.ScreenResHd.clicked.connect(self._GraphicSetting_ScreenRes)
        self.ScreenResFhd.clicked.connect(self._GraphicSetting_ScreenRes)

    def _GraphicSetting_ScreenMode(self):
        if self.ScreenModeFull.isChecked():
            self._setting_data["sc_mode"] = "full"

        elif self.ScreenModeWindow.isChecked():
            self._setting_data["sc_mode"] = "window"

    def _GraphicSetting_ScreenRes(self):
        if self.ScreenResHd.isChecked():
            self._setting_data["sc_res"] = "hd"

        elif self.ScreenResFhd.isChecked():
            self._setting_data["sc_res"] = "fhd"

    def _ContinueCheck_Accept(self):
        self._setting_data["continue"] = True

    def _ContinueCheck_Reject(self):
        self._setting_data["continue"] = False


    def CheckData(self):
        for key, value in self._setting_data.items():
            print(f"{key} : {value}")

    def GetData(self) -> Dict[str, Union[str, bool]]:
        return self._setting_data

    @staticmethod
    def Start() -> Dict[str, Union[str, bool]]:
        app = QApplication(sys.argv)
        my_window = SettingGUI()
        my_window.show()
        app.exec_()
        my_window.CheckData()
        return my_window.GetData()

if __name__ == '__main__':
    pass
    # app = QApplication(sys.argv)
    # my_window = SettingGUI()
    # my_window.show()
    # app.exec_()
    # my_window.CheckData()


