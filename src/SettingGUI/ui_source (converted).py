# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingGUI_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 600, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalFrame = QtWidgets.QFrame(Dialog)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../resources/start_menu (edited).png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 330, 460, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 590, 460, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 360, 460, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 340, 440, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ScreenResHd = QtWidgets.QRadioButton(Dialog)
        self.ScreenResHd.setGeometry(QtCore.QRect(50, 430, 200, 16))
        self.ScreenResHd.setChecked(True)
        self.ScreenResHd.setObjectName("ScreenResHd")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.ScreenResHd)
        self.ScreenResFhd = QtWidgets.QRadioButton(Dialog)
        self.ScreenResFhd.setGeometry(QtCore.QRect(50, 470, 200, 16))
        self.ScreenResFhd.setObjectName("ScreenResFhd")
        self.buttonGroup.addButton(self.ScreenResFhd)
        self.ScreenModeWindow = QtWidgets.QRadioButton(Dialog)
        self.ScreenModeWindow.setGeometry(QtCore.QRect(340, 430, 120, 16))
        self.ScreenModeWindow.setChecked(True)
        self.ScreenModeWindow.setObjectName("ScreenModeWindow")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.ScreenModeWindow)
        self.ScreenModeFull = QtWidgets.QRadioButton(Dialog)
        self.ScreenModeFull.setGeometry(QtCore.QRect(340, 470, 120, 16))
        self.ScreenModeFull.setObjectName("ScreenModeFull")
        self.buttonGroup_2.addButton(self.ScreenModeFull)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "AvoidMonster 그래픽 설정"))
        self.ScreenResHd.setText(_translate("Dialog", "1280 X 720 ( HD 해상도 )"))
        self.ScreenResFhd.setText(_translate("Dialog", "1920 X 1080 ( FHD 해상도 )"))
        self.ScreenModeWindow.setText(_translate("Dialog", "창 모드"))
        self.ScreenModeFull.setText(_translate("Dialog", "전체화면 모드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
