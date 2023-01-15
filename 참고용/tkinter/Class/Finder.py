import os.path

from selenium import webdriver
from urllib.parse import quote_plus
import bs4
import requests
import json
import datetime
import csv


class Finder:
    def __init__(self, DRIVER_OPTION = None, SEARCH_KEYWORD = None):
        """
        :param SEARCH_KEYWORD:
        """

        if SEARCH_KEYWORD is None:
            raise ValueError("SEARCH_KEYWORD 파라미터는 비워둘 수 없습니다.")

        self.SEARCH_ENGINE = "https://www.google.co.kr"
        self.SEARCH_KEYWORD = SEARCH_KEYWORD
        if DRIVER_OPTION is None:
            self.WEBDRIVER = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe" if __name__ == "__main__" else ".\\Class\\chromedriver_win32\\chromedriver.exe")

        else:
            self.WEBDRIVER = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe" if __name__ == "__main__" else ".\\Class\\chromedriver_win32\\chromedriver.exe", options = DRIVER_OPTION)

    @staticmethod
    def WriteErrorLog(ERROR_MSG):
        DIR = f".\\ERROR_LOG\\ERROR_LOG {str(datetime.datetime.today()).split(' ')[0]}.txt"
        ERROR_LOG_FILE_EXIST_CHECK = os.path.exists(DIR)
        with open(DIR, "a" if ERROR_LOG_FILE_EXIST_CHECK is True else "w") as WRITE_FILE:
            WRITE_FILE.write(
                f"ERROR : OCCURRENCE TIME = {str(datetime.datetime.today()).split('.')[0]},\nMESSAGE = {ERROR_MSG}"
            )

    # HTTP request를 받아서 검색엔진 서버가 보낸 response를 Beautifulsoup객체로 변환해서 리턴
    @staticmethod
    def GetSiteObject_HTML(SITE_REQUEST_RESPONSE) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(SITE_REQUEST_RESPONSE.content, "html.parser")

    # Selenium으로 가져온 사이트 소스를 Beautifulsoup객체로 변환해서 리턴
    @staticmethod
    def GetSiteObject_HTML_SE(PAGE_SOURCE) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(PAGE_SOURCE, "html.parser")

    # 입력받은 Beautifulsoup객체에서 HTML의 속성을 통해 분류하여 필요한 element를 리스트로 반환 / return ==> [Beautifulsoup Object,...]
    @staticmethod
    def ReturnSearchResult(SOUP_OBJECT=None) -> list:
        if SOUP_OBJECT is None:
            raise ValueError("SOUP_OBJECT 파라미터는 비워둘 수 없습니다.")

        RETURN_DATA_LIST = []
        RESULT_ELEMENT_LIST = []
        ELEM_LIST = SOUP_OBJECT.find_all(["a", "href"])
        for INCLUDE_a_href_NUM in range(ELEM_LIST.__len__()):
            INCLUDE_a_href = ELEM_LIST[INCLUDE_a_href_NUM]
            INCLUDE_h3 = INCLUDE_a_href.find("h3")
            if INCLUDE_h3 is not None:
                RESULT_ELEMENT_LIST.append(INCLUDE_a_href)


        for ELEM_NUM in range(RESULT_ELEMENT_LIST.__len__()):
            ELEMENT = RESULT_ELEMENT_LIST[ELEM_NUM]
            RETURN_DATA = {
                "TEXT": ELEMENT.find("h3").get_text(),
                "URL": ELEMENT.find("div").get_text().split(" ")[0]
            }
            RETURN_DATA_LIST.append(RETURN_DATA)



        return RETURN_DATA_LIST


    #검색엔진 서버가 작동하고 있는지 request를 보내 확인 / return ==> bool
    def CheckingStatus_TargetSearchEngine(self) -> bool:
        return True if requests.get(url = self.SEARCH_ENGINE).status_code == 200 else False


    #검색엔진 서버에 맞는 HTTP request를 작성 / return ==> str
    def ReturnString_HTTP_REQUEST(self, PAGE_NUM: int) -> str:
        return self.SEARCH_ENGINE + "/search?q=" + quote_plus(self.SEARCH_KEYWORD) + f"&start={str(PAGE_NUM) + '0' if PAGE_NUM < 10 else str(PAGE_NUM)}"


    def StartFinder(self, NUMBER_OF_PAGES = 1) -> bool: #검색 페이지 갯수 ==> 기본값 : 1
        ERROR_COUNT = 0
        try:
            SEARCH_ENGINE_STATUS = self.CheckingStatus_TargetSearchEngine()
            print(f"SEARCH_ENGINE_STATUS = {SEARCH_ENGINE_STATUS}")
            if SEARCH_ENGINE_STATUS is True:
                RETURN_DATA = {
                }
                for CURRENT_PAGE_NUM in range(NUMBER_OF_PAGES):
                    SITE_URL = self.ReturnString_HTTP_REQUEST(PAGE_NUM = CURRENT_PAGE_NUM + 1)
                    self.WEBDRIVER.get(SITE_URL)
                    print(f"SITE_URL = {SITE_URL}")
                    print(f"PAGE_NUM = {CURRENT_PAGE_NUM}")
                    SITE_SOUP_OBJ = self.GetSiteObject_HTML_SE(self.WEBDRIVER.page_source)
                    # print(type(SITE_SOUP_OBJ))
                    RETURN_SEARCH_RESULT_DATA_LIST = self.ReturnSearchResult(SITE_SOUP_OBJ)

                    for RETURN_SEARCH_RESULT_DATA_NUM in range(RETURN_SEARCH_RESULT_DATA_LIST.__len__()):
                        RETURN_DATA[f"{CURRENT_PAGE_NUM * 10 + RETURN_SEARCH_RESULT_DATA_NUM + 1}"] = RETURN_SEARCH_RESULT_DATA_LIST[RETURN_SEARCH_RESULT_DATA_NUM]

                with open(".\\SEARCH_RESULT.json" if __name__ == "__main__" else ".\\Class\\SEARCH_RESULT.json", "w", encoding="utf-8") as WRITE_RESULT:
                    json.dump(RETURN_DATA, WRITE_RESULT, indent=4)

                with open(".\\SEARCH_RESULT.csv" if __name__ == "__main__" else ".\\Class\\SEARCH_RESULT.csv", "w", newline = "", encoding = "utf-8") as WRITE_RESULT:
                    CSV_W_OBJ = csv.writer(WRITE_RESULT)
                    # CSV_W_OBJ.writerow(RETURN_DATA.keys())
                    # CSV_W_OBJ.writerow([f"{DATA.get('TEXT')}" for DATA in RETURN_DATA.values()])
                    # CSV_W_OBJ.writerow([f"{DATA.get('URL')}" for DATA in RETURN_DATA.values()])

                    for RT_DATA_KEY in RETURN_DATA.keys():
                        CSV_W_OBJ.writerow(
                            [RT_DATA_KEY, RETURN_DATA.get(RT_DATA_KEY).get("TEXT"), RETURN_DATA.get(RT_DATA_KEY).get("URL")]
                        )




        except Exception as ERROR_MSG:
            ERROR_COUNT += 1
            self.WriteErrorLog(ERROR_MSG)

        self.WEBDRIVER.quit()

        if ERROR_COUNT == 0:
            return True
        else:
            return False

    @staticmethod
    def DataClear():
        with open(".\\SEARCH_RESULT.json" if __name__ == "__main__" else ".\\Class\\SEARCH_RESULT.json", "w", encoding="utf-8") as WRITE_RESULT:
            json.dump({"1": {"TEXT": "검색 옵션을 입력하여 주세요.", "URL": "데이터 크롤링을 시작하려면 시작 버튼을 누르세요.\n\n시작버튼을 누른 후 발생하는 응답없음은 데이터 크롤링 로딩 과정입니다.\n\n저장된 크롤링 데이터는 다음 실행시 자동으로 초기화됩니다."}}, WRITE_RESULT, indent=4)


if __name__ == "__main__":
    OPTION = webdriver.ChromeOptions()
    for OP in ["headless", "disable-gpu"]:
        OPTION.add_argument(OP)
    GOOGLE_FINDER = Finder(DRIVER_OPTION = OPTION, SEARCH_KEYWORD = "파이썬")
    GOOGLE_FINDER.StartFinder(NUMBER_OF_PAGES = 1)







