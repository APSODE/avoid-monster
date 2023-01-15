from TEST import PLAYER_X_pos, SC_WIDTH
import pygame



class PLAYER: #PLAYER에 대한 각종 정보를 리턴 // 현재는 캐릭터의 좌표를 리턴할 예정

   #클래스 속성 설정 필요 공부하기

    def PLAYER_INFO(SCREEN_WIDTH , SCREEN_HEIGHT):
        SC_WIDTH = SCREEN_WIDTH
        SC_HEIGHT = SCREEN_HEIGHT 


        CHAR_IMG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Char_SP\\CHAR_1.png" #학교 컴사용시 캐릭터 이미지 디렉토리
        pi = pygame.image

        player = pi.load(CHAR_IMG_DIR)
        PLAYER_SIZE = player.get_rect().size

        PLAYER_WIDTH = PLAYER_SIZE[0]
        PLAYER_HEIGHT = PLAYER_SIZE[1]

        PLAYER_X_POS = (SC_WIDTH / 2) - (PLAYER_WIDTH / 2) 
        PLAYER_Y_POS = (SC_HEIGHT / 2) - (PLAYER_HEIGHT / 2)
        
        return PLAYER_X_POS, PLAYER_Y_POS, PLAYER_WIDTH, PLAYER_HEIGHT

    def MOVE_PLAYER(SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X_POS, PLAYER_Y_POS, MOVE_X, MOVE_Y):
        
        PLAYER_X_pos = PLAYER_X_POS
        PLAYER_Y_pos = PLAYER_Y_POS
        #나온 값으로 비교하거나 실행하는애
        PLAYER_X_pos += MOVE_X
        PLAYER_Y_pos += MOVE_Y

        #가로 경계 처리
        if PLAYER_X_pos < 0:
            PLAYER_X_pos = 0
        elif PLAYER_X_pos > SCREEN_WIDTH - PLAYER_WIDTH:
            PLAYER_X_pos = SCREEN_WIDTH - PLAYER_WIDTH

        #세로 정지 처리
        if PLAYER_Y_pos < 0:
            PLAYER_Y_pos = 0
        elif PLAYER_Y_pos > SCREEN_HEIGHT - PLAYER_HEIGHT:
            PLAYER_Y_pos = SCREEN_HEIGHT - PLAYER_HEIGHT


        

    

