import tkinter
import tkinter.ttk
from PIL import ImageTk, Image
from typing import Dict, Type



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

        self._button = {
            "default": tkinter.Button
        }

        self._canvas = {
            "default": tkinter.Canvas
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

    @property
    def Button(self) -> Dict[str, Type[tkinter.Button]]:
        return self._button

    @Button.setter
    def Button(self, value: Dict[str, Type[tkinter.Button]]):
        """value = Dict[str, Type[tkinter.button]]"""
        for target_key, new_value in value.items():
            self._button[target_key] = new_value

    @property
    def Canvas(self) -> Dict[str, Type[tkinter.Canvas]]:
        return self._canvas

    @Canvas.setter
    def Canvas(self, value: Dict[str, Type[tkinter.Canvas]]):
        """value = Dict[str, Type[tkinter.Canvas]]"""
        for target_key, new_value in value.items():
            self._button[target_key] = new_value

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
        self._master.resizable(False, False)

    def SettingTitle(self):
        self._master.title = self._game_title

    def CreateBaseFrame(self):
        image_frame = tkinter.Frame(self._master)
        image_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        setting_frame = tkinter.Frame(self._master)
        setting_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

        button_frame_out = tkinter.Frame(self._master)
        button_frame_out.grid(row = 2, column = 0, padx = 10, pady = 10)

        button_frame_in = tkinter.Frame(button_frame_out)
        button_frame_in.pack()

        self._component_container.BaseFrame = {
            "game_image": image_frame,
            "game_setting": setting_frame,
            "button_out": button_frame_out,
            "button_in": button_frame_in
        }

    def CreateLabelFrame(self):
        setting_label_frame = tkinter.LabelFrame(
            self._component_container.BaseFrame.get("game_setting"),
            text = "game setting label frame"
        )
        setting_label_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        self._component_container.LabelFrame = {
            "game_setting": setting_label_frame
        }

    def CreateCanvasFrame(self):
        image_canvas_frame = tkinter.Canvas(self._component_container.BaseFrame.get("game_image"),
                                            width = 400, height = 300)
        image_canvas_frame.pack()

        self._component_container.Canvas = {
            "start_menu_image": image_canvas_frame
        }

    def CreateImage(self):
        image_file = Image.open(f"..\\..\\resources\\start_menu.jpg")
        start_menu_image = ImageTk.PhotoImage(image_file.resize((400, 300)))
        # start_menu_image = tkinter.PhotoImage(file = f"..\\..\\resources\\start_menu.png")
        canvas = self._component_container.Canvas.get("start_menu_image")
        canvas.create_image()
        # start_menu_label = tkinter.Label(self._component_container.BaseFrame.get("game_image"), image = start_menu_image)
        # start_menu_label.pack()



    def CreateButton(self):
        test_btn = tkinter.Button(self._component_container.BaseFrame.get('button_in'), text = "테스트 버튼")
        # test_btn.place(x = 10, y = 10)
        test_btn.grid(row = 0, column = 0, padx = 10, pady = 10)

    def CreateWindow(self):
        self.SettingResolution()
        self.CreateBaseFrame()
        self.CreateLabelFrame()
        self.CreateImage()
        self.CreateButton()



    def CreateGUI(self):
        self.CreateWindow()

        self._master.mainloop()


if __name__ == '__main__':
    SG = SettingGUI()
    SG.CreateGUI()
