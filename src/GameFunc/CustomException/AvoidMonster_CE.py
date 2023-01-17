class GameQuitException(Exception):
    def __str__(self):
        return "게임 종료 이벤트 발생"
