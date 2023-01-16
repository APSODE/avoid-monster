from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

qt_designer_class = uic.loadUiType("SettingGUI_qt.ui")[0]


class SettingGUI(QDialog, qt_designer_class):

    def __init__(self):
        self._setting_data = {
            "sc_mode": "window", #default value
            "sc_res": "hd" #default value
        }
        super().__init__()
        self.setupUi(self)

        self.screen_mode_full: QRadioButton
        self.screen_mode_window: QRadioButton
        self.screen_res_hd: QRadioButton
        self.screen_res_fhd: QRadioButton
        self.setting_ok_btn: QPushButton
        self.setting_cancle_btn: QPushButton

        # self.screen_mode_full = self.

        self.ScreenModeFull.clicked.connect(self.GraphicSetting_ScreenMode)
        self.ScreenModeWindow.clicked.connect(self.GraphicSetting_ScreenMode)

        self.ScreenResHd.clicked.connect(self.GraphicSetting_ScreenRes)
        self.ScreenResFhd.clicked.connect(self.GraphicSetting_ScreenRes)

        # self.setting_ok_btn = self.


    def GraphicSetting_ScreenMode(self):
        if self.ScreenModeFull.isChecked():
            self._setting_data["sc_mode"] = "full"

        elif self.ScreenModeWindow.isChecked():
            self._setting_data["sc_mode"] = "window"

    def GraphicSetting_ScreenRes(self):
        if self.ScreenResHd.isChecked():
            self._setting_data["sc_res"] = "hd"

        elif self.ScreenResFhd.isChecked():
            self._setting_data["sc_res"] = "fhd"

    def CheckData(self):
        for key, value in self._setting_data.items():
            print(f"{key} : {value}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = SettingGUI()
    my_window.show()
    app.exec_()
    my_window.CheckData()


