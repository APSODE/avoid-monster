import tkinter
import tkinter.ttk
from typing import Dict, Type
from src.decorator.ErrorChecker import ErrorChecker


class ComponentContainer:
    def __init__(self):
        self._base_frame = {
            "default": tkinter.Frame
        }

        self._label_frame = {
            "default": tkinter.LabelFrame
        }

        self._combo_box = {
            "default": tkinter.ttk.Combobox
        }



    @property
    def BaseFrame(self) -> Dict[str, Type[tkinter.Frame]]:
        return self._base_frame

    @BaseFrame.setter
    def BaseFrame(self, value: Dict[str, Type[tkinter.Frame]]) -> None:
        """value = Dict[str, Type[tkinter.Frame]]"""
        for target_key, new_value in value.items():
            self._base_frame[target_key] = new_value

    @property
    def LabelFrame(self) -> Dict[str, Type[tkinter.LabelFrame]]:
        return self._label_frame

    @LabelFrame.setter
    def LabelFrame(self, value: Dict[str, Type[tkinter.LabelFrame]]) -> None:
        """value = Dict[str, Type[tkinter.LabelFrame]]"""
        for target_key, new_value in value.items():
            self._label_frame[target_key] = new_value

    @property
    def ComboBox(self) -> Dict[str, Type[tkinter.ttk.Combobox]]:
        return self._combo_box

    @ComboBox.setter
    def ComboBox(self, value: Dict[str, Type[tkinter.ttk.Combobox]]):
        """value = Dict[str, Type[tkinter.ttk.Combobox]]"""
        for target_key, new_value in value.items():
            self._combo_box[target_key] = new_value

    def GetAllData(self) -> dict:
        return {key.replace("_", "", 1): value for key, value in self.__dict__.items()} #dictionary comprehension


class SettingGUI:
    def __init__(self):
        self._game_title = "Avoid Moster | ver1.0"
        self._master = tkinter.Tk()
        self._component_container = ComponentContainer()


    def SettingResolution(self):
        user_screen_width = self._master.winfo_screenwidth()
        user_screen_height = self._master.winfo_screenheight()

        gui_width = 400
        gui_height = 600

        gui_x_position = (user_screen_width - gui_width) // 2
        gui_y_position = (user_screen_height - gui_height) // 2

        self._master.geometry(
            f"{gui_width}x{gui_height}"
            f"+{gui_x_position}"
            f"+{gui_y_position}"
        )

    def SettingTitle(self):
        self._master.title = self._game_title

    def CreateBaseFrame(self):
        base_up_frame = tkinter.Frame(self._master)
        base_up_frame.grid(row = 0, column = 0)
        base_down_frame = tkinter.Frame(self._master)
        base_down_frame.grid(row = 1, column = 0)

        self._component_container.BaseFrame = {
            "up": base_up_frame,
            "down": base_down_frame
        }

    def CreateLabelFrame(self):
        up_label_frame = tkinter.LabelFrame(
            self._component_container.BaseFrame.get("up"),
            text = "up label frame"
        )
        up_label_frame.grid(padx = 10, pady = 10)

        down_label_frame = tkinter.LabelFrame(
            self._component_container.BaseFrame.get("down"),
            text = "down label frame"
        )
        down_label_frame.grid(padx = 10, pady = 10)

        self._component_container.LabelFrame = {
            "up": up_label_frame,
            "down": down_label_frame
        }

    def CreateWindow(self):
        self.SettingResolution()
        self.CreateBaseFrame()
        self.CreateLabelFrame()


    def CreateGUI(self):
        self.CreateWindow()
        self._master.mainloop()


if __name__ == '__main__':
    SG = SettingGUI()
    SG.CreateGUI()