import tkinter
import tkinter.messagebox as MSGBOX
# # from selenium import webdriver
# from Class.Finder import Finder
from Class.JSON_RW_TOOL import READ_WRITE

class GoogleFinderGUI:
    def __init__(self, MASTER: tkinter.Tk, TITLE = "GoogleFinder | ver1.0"):
        # Tkinter라이브러리는 tkinter.Tk를 이용하여 UI를 관리하는데 이를 위해 GoogleFInderGUI객체가 생성될때
        # 파라미터로 입력받아 객체내의 메소드에서 사용할수 있도록 self.MASTER이라는 클래스 변수로 저장한다.
        self.MASTER = MASTER

        # 프로그램 GUI에 사용될 제목 이름을 객체 생성될때 파라미터로 입력받아 self.TITLE이라는 클래스 변수로 저장한다.
        self.TITLE = TITLE

        # 프로그램의 GUI구성에서 데이터 크롤링 결과를 표시할 영역과 여러가지 작동 메뉴를 표시할 영역을 분리하기 위해서
        # tkinter.Frame를 이용하여 Frame으로 영역을 생성 후 GoogleFinder클래스의 다른 메소드에서 사용가능 하도록
        # self.BASE_FRAME라는 클래스 변수로 저장한다.
        self.BASE_FRAME = {
            "LEFT": self.GetBaseFrame(ROW = 0, COLUMN = 0),
            "RIGHT": self.GetBaseFrame(ROW = 0, COLUMN = 1)
        }

        # 프로그램의 GUI구성에서 크롤링 결과를 표시할 영역과 작동 메뉴 영역의 이름을 보여줄 라벨프레임을 생성
        # 라벨프레임은 tkinter.LabelFrame을 이용해 생성하며 tkinter.Frame과 동일하게 영역 생성을 할 수 있으며,
        # 해당영역의 이름을 지정하고 GUI화면에 출력까지 가능하다.
        # 그리고 실제 GUI의 구성요소들은 이 LabelFrame영역에 생성되고 관리되므로 다른 메소드들에서 쉽게 접근이 가능하도록
        # self.LABEL_FRAME이라는 클래스 변수를 생성하여 GUI구성에 사용되는 모든 LabelFrame을 저장한다.
        self.LABEL_FRAME = {
            "BASE_L": tkinter.LabelFrame(),
            "BASE_R": tkinter.LabelFrame(),
            "SEARCH_OPTION": {
                "KEYWORD": tkinter.LabelFrame(),
                "NUMBER_OF_PAGES": tkinter.LabelFrame()
            },
            "BTN": tkinter.LabelFrame()
        }

        # 크롤링의 타깃 검색어와 크롤링을 해올 페이지 수를 입력받기 위한 GUI요소로 tkinter.Entry를 이용해 생성된다.
        # 이 Entry라는 요소는 Finder객체의 파라미터로 사용되기 때문에 다른 메소드에서 접근이 가능해야 하므로
        # self.ENTRY_VALUE라는 클래스 변수를 생성하여 Entry의 입력값을 저장한다.
        self.ENTRY_VALUE = {
            "KEYWORD": tkinter.Entry(),
            "NUMBER_OF_PAGES": tkinter.Entry()
        }

        # 프로그램의 GUI구성에서 메뉴의 작동버튼을 저장하는 클래스 변수
        self.SEARCH_FUNC_BTN = {
            "START": tkinter.Button(),
            "EXIT": tkinter.Button()
        }

        # 프로그램의 GUI구성에서 크롤링 결과를 화면에 띄우기 위해 tkinter.Text를 사용하는데
        # Finder객체의 실행으로 json파일로 저장된 크롤링 결과를 self.SetSearchResultText메소드를 통해
        # Text객체를 생성하여 화면에 띄우므로 관리를 위해 self.SEARCH_RESULT_TEXT라는 클래스 변수에 저장한다.
        self.SEARCH_RESULT_TEXT = tkinter.Text()

    # ReturnSearchData_String메소드는 Finder객체의 작동이후 json파일로 저장된 크롤링 결과를
    # dictionary의 형태로 읽어와 하나의 string의 형태로 변환시켜 리턴한다.
    # 따로 객체의 클래스 변수에 접근할 필요가 없으므로 staticmethod로 선언하였다.
    @staticmethod
    def ReturnSearchData_String() -> str:
        RETURN_TEXT = ""
        # READ_JSON메소드의 어노테이션을 보면 리턴 형식이 dictionary인것을 알 수 있다.
        READ_SEARCH_RESULT_DATA = READ_WRITE.READ_JSON(FILE_DIR=".\\Class\\SEARCH_RESULT.json")
        for SEARCH_RESULT_KEY in READ_SEARCH_RESULT_DATA.keys():
            RESULT_DATA = READ_SEARCH_RESULT_DATA[SEARCH_RESULT_KEY]
            WALL = "----------------------------------------------------------------------"
            WRITE_SEARCH_RESULT_TEXT = f"{WALL}\n\n{RESULT_DATA['TEXT']}\n{RESULT_DATA['URL']}\n\n"
            RETURN_TEXT += WRITE_SEARCH_RESULT_TEXT

        return RETURN_TEXT

    # GetBaseFrame메소드는 다른 GUI구성요소의 생성을 위해 가장 먼저 생성되야하는 Frame객체를 생성하는 메소드이며
    # tkinter.Frame().grid라는 메소드를 이용하여 GUI의 위치를 조정하기 하고 해당 Frame객체를 리턴한다.
    # GoogleFinderGUI객체가 생성될때 자동으로 __init__메소드를 통해 self.BASE_FRAME에서 호출된다.
    def GetBaseFrame(self, ROW, COLUMN) -> tkinter.Frame:
        FRAME = tkinter.Frame(self.MASTER) # Frame객체 생성
        FRAME.grid(row = ROW, column = COLUMN) # 위치 지정
        return FRAME

    # SetWindowConfig메소드는 프로그램의 윈도우창의 기본 설정을 진행하고 화면의 해상도와 제목을 설정한다.
    def SetWindowConfig(self):
        self.MASTER.geometry("750x580") # 세부값은 사용 모니터 해상도에 따라서 다를수 있음
        self.MASTER.title(self.TITLE) # 제목 설정
        # self.MASTER.resizable(False, False)

    # ProgramExitProcess메소드는 GoogleFinderGUI의 MASTER이라고 할 수 있는 객체를 destroy메소드를 이용해 삭제함으로써
    # 프로그램을 종료한다.
    def ProgramExitProcess(self):
        self.MASTER.destroy()

    # SetProgram_ICON메소드는 GoogleFinderGUI의 프로그램 icon을 설정하는 메소드이다.
    def SetProgram_ICON(self):
        self.MASTER.iconbitmap(".\\google.ico")

    # SetSearchResultText메소드는 GoogleFinderGUI에서 실제로 프로그램 화면에 크롤링 결과를 출력하기 위해
    # tkinter.Text객체를 생성 및 설정하는 메소드이다.
    # 리턴은 하지 않으며 직접 self.SEARCH_RESULT_TEXT라는 클래스 변수에 해당 Text객체를 저장한다.
    def SetSearchResultText(self):
        SEARCH_RESULT_TEXT = tkinter.Text(self.LABEL_FRAME["BASE_L"], width = 70, height = 40)
        SEARCH_RESULT_TEXT.pack(anchor = tkinter.CENTER, padx = 5, pady = 5)
        SEARCH_RESULT_TEXT.insert(tkinter.END, self.ReturnSearchData_String()) # Text객체로 표현할 문자열을 삽입
        SEARCH_RESULT_TEXT.config(state = tkinter.DISABLED)
        self.SEARCH_RESULT_TEXT = SEARCH_RESULT_TEXT

    # SetLabelFrame메소드는 GoogleFinderGUI의 구성요소들이 실제로 생성되는 LabelFrame을 생성하는 메소드이다.
    # 이 메소드에서 생성된 LabelFrame객체는 self.LABEL_FRAME의 정해진 key값의 value로 저장된다.
    def SetLabelFrame(self):
        F_LABEL_FRAME = tkinter.LabelFrame(self.BASE_FRAME["LEFT"], text = "검색 결과")
        F_LABEL_FRAME.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.LABEL_FRAME["BASE_L"] = F_LABEL_FRAME

        S_LABEL_FRAME = tkinter.LabelFrame(self.BASE_FRAME["RIGHT"], text = "검색 옵션")
        S_LABEL_FRAME.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.LABEL_FRAME["BASE_R"] = S_LABEL_FRAME

        NUMBER_OF_PAGES_LABEL_FRAME = tkinter.LabelFrame(self.LABEL_FRAME["BASE_R"], text = "파싱 페이지 수")
        NUMBER_OF_PAGES_LABEL_FRAME.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.LABEL_FRAME["SEARCH_OPTION"]["NUMBER_OF_PAGES"] = NUMBER_OF_PAGES_LABEL_FRAME

        KEYWORD_LABEL_FRAME = tkinter.LabelFrame(self.LABEL_FRAME["BASE_R"], text = "검색어")
        KEYWORD_LABEL_FRAME.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.LABEL_FRAME["SEARCH_OPTION"]["KEYWORD"] = KEYWORD_LABEL_FRAME

        START_EXIT_BTN_FRAME = tkinter.LabelFrame(self.LABEL_FRAME["BASE_R"], text = "시작 & 종료")
        START_EXIT_BTN_FRAME.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.LABEL_FRAME["BTN"] = START_EXIT_BTN_FRAME

    # SetSearchOption메소드는 크롤링 검색옵션을 입력받는 Entry객체를 생성하는 메소드이다.
    def SetSearchOption(self):
        KEYWORD_ENTRY = tkinter.Entry(self.LABEL_FRAME["SEARCH_OPTION"]["KEYWORD"])
        KEYWORD_ENTRY.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.ENTRY_VALUE["KEYWORD"] = KEYWORD_ENTRY

        NUMBER_OF_PAGES_ENTRY = tkinter.Entry(self.LABEL_FRAME["SEARCH_OPTION"]["NUMBER_OF_PAGES"])
        NUMBER_OF_PAGES_ENTRY.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.ENTRY_VALUE["NUMBER_OF_PAGES"] = NUMBER_OF_PAGES_ENTRY

    # SetSearchFuncButton메소드는 프로그램의 버튼들을 생성하는 메소드이다.
    def SetSearchFuncButton(self):
        START_BUTTON = tkinter.Button(self.LABEL_FRAME["BTN"], text = "시작")
        START_BUTTON.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.SEARCH_FUNC_BTN["START"] = START_BUTTON

        EXIT_BUTTON = tkinter.Button(self.LABEL_FRAME["BTN"], text = "종료", command = self.ProgramExitProcess)
        EXIT_BUTTON.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.SEARCH_FUNC_BTN["EXIT"] = EXIT_BUTTON

    # StartGoogleFinder메소드는 GoogleFinderGUI의 여러 메소드들에 의해 생성된 데이터를 이용하여 Finder객체를 생성하여
    # 실제로 웹크롤러를 동작시키는 메소드이다.
    # 클래스 변수에서 크롤링 타깃 검색어와 크롤링해올 페이지 수를 입력받고 Finder().StartFinder를 호출하여 크롤러를 동작시킨다.
    # 크롤러 동작이 완료되면, self.SetSearchResultText메소드를 호출하여 프로그램 화면에 크롤링 데이터를 출력한다.
    # def StartGoogleFinder(self):
    #     OPTION = webdriver.ChromeOptions()
    #     for OP in ["headless", "disable-gpu"]:
    #         OPTION.add_argument(OP)
    #     SEARCH_KEYWORD = self.ENTRY_VALUE["KEYWORD"].get()
    #     GOOGLE_FINDER = Finder(DRIVER_OPTION = OPTION, SEARCH_KEYWORD = SEARCH_KEYWORD)
    #     try:
    #         USER_INPUT_NUM = int(self.ENTRY_VALUE["NUMBER_OF_PAGES"].get())
    #         MSGBOX.showinfo(message = f"페이지 갯수 : {USER_INPUT_NUM}장\n검색어 : {SEARCH_KEYWORD}\n해당 입력값으로 데이터 크롤링을 시작합니다.")
    #     except:
    #         MSGBOX.showinfo(message = "입력한 페이지 갯수가 정수가 아닙니다.\n기본값 1로 데이터 크롤링을 시작합니다.")
    #         USER_INPUT_NUM = 1
    #
    #     GOOGLE_FINDER.StartFinder(NUMBER_OF_PAGES = USER_INPUT_NUM)
    #     self.SEARCH_RESULT_TEXT.destroy()
    #     self.SetSearchResultText()

    # GoogleFinderGUI의 여러 화면 구성요소들을 생성하기 위한 메소드들을 호출하는 메소드이다.
    # 역할은 객체 생성 이후 main코드에서 호출해야할 메소드 단순화
    def SetProgramGUI(self):
        self.SetProgram_ICON()
        self.SetWindowConfig()
        self.SetLabelFrame()
        self.SetSearchOption()
        # self.SetSearchFuncButton()
        self.SetSearchResultText()





if __name__ == "__main__":
    # Finder.DataClear() # 이전에 크롤링되어 저장된값을 지우는 메소드 호출
    MASTER_UI = tkinter.Tk() # GUI생성을 위한 MASTER_UI생성(tkinter.Tk객체 생성)
    GOOGLE_FINDER_GUI = GoogleFinderGUI(MASTER = MASTER_UI) # MASTER_UI를 파라미터로 받아 GoogleFinderGUI객체 생성
    GOOGLE_FINDER_GUI.SetProgramGUI() # UI생성 메소드 호출
    MASTER_UI.mainloop() # UI의 동작을 위한 loop생성
