import json


class READ_WRITE:
    @staticmethod
    def READ_JSON(FILE_DIR: str) -> dict:
        """FILE_DIR에는 데이터를 읽어올 JSON데이터 파일 디렉토리를 입력해주세요.

        리턴
        --------
        READ_JSON(FILE_DIR = :func:`JSON_DIR`)\n
        ==> READ_USER_DATA[:func:`"KEY"`]
        """

        with open(f"{FILE_DIR}", "r", encoding="utf-8") as READ_USER_PROFILE:
            READ_USER_DATA = json.load(READ_USER_PROFILE)
            READ_USER_PROFILE.close()

        return READ_USER_DATA