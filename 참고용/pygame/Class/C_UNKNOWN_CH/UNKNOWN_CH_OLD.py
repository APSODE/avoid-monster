#from TEST import PLAYER_INFO, PLAYER_X_pos, SC_WIDTH
#순환 임포트 오류 : A파일에서 import B / B파일에서 import A를 하면 순환 임포트 오류가 발생 // 위의 경우가 이경우임

import pygame
import json
from Class.FUNC.RW_JSON import READ_WRITE

CONFIG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Config\\Main_Config.json"



class PLAYER: #PLAYER에 대한 각종 정보를 리턴 // 현재는 캐릭터의 좌표를 리턴할 예정
    


    def PLAYER_INFO(CHAR_NAME, IMG_DIR):
        
        #CHAR_IMG_DIR = "C:\\Users\\Administrator\\Desktop\\게임제작\\Char_SP\\CHAR_1.png"
        #CHAR_IMG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Char_SP\\CHAR_1.png" #학교 컴사용시 캐릭터 이미지 디렉토리
        try:
            READ_CHARACTER_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)["CHARACTER"][f"{CHAR_NAME}"]["INFO"]
            PLAYER_WIDTH = READ_CHARACTER_DATA["PLAYER_WIDTH"]
            PLAYER_HEIGHT = READ_CHARACTER_DATA["PLAYER_HEIGTH"]
            PLAYER_SPEED = READ_CHARACTER_DATA["PLAYER_SPEED"]
        except:
            pi = pygame.image
            PLAYER_IMG = pi.load(IMG_DIR)
            PLAYER_SIZE = PLAYER_IMG.get_rect().size
            PLAYER_SPEED = 15 #기본속도
            PLAYER_WIDTH = PLAYER_SIZE[0]
            PLAYER_HEIGHT = PLAYER_SIZE[1]

            WRITE_JSON_DATA = [
                {
                    "KEY": ["CHARACTER", f"{CHAR_NAME}", "INFO", "PLAYER_NAME"], "VALUE": f"{CHAR_NAME}"
                },
                {
                    "KEY": ["CHARACTER", f"{CHAR_NAME}", "INFO", "PLAYER_WIDTH"], "VALUE": PLAYER_WIDTH
                },
                {
                    "KEY": ["CHARACTER", f"{CHAR_NAME}", "INFO", "PLAYER_HEIGHT"], "VALUE": PLAYER_HEIGHT
                },
                {
                    "KEY": ["CHARACTER", f"{CHAR_NAME}", "INFO", "PLAYER_SPEED"], "VALUE": PLAYER_SPEED
                }
            ]
            READ_WRITE.WRITE_JSON(CONFIG_DIR, WRITE_JSON_DATA)

        
        




        

                  


        
        
        return PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_IMG

    def PLAYER_POS():
        
        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()

        PLAYER_WIDTH = READ_CHARACTER_DATA["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CHARACTER_DATA["PLAYER_HEIGHT"]

        PLAYER_X_POS = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2) 
        PLAYER_Y_POS = (SCREEN_HEIGHT / 2) - (PLAYER_HEIGHT / 2)

        return PLAYER_X_POS, PLAYER_Y_POS
        
    def PLAYER_MOVE(NOW_EVENT, X_POS, Y_POS):
        
        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()
        
        MOVE_X_POS = X_POS
        MOVE_Y_POS = Y_POS

        PLAYER_SPEED = READ_CHARACTER_DATA["PLAYER_SPEED"]
        EVENT_TYPE = NOW_EVENT.type

        

        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                MOVE_Y_POS += PLAYER_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS += PLAYER_SPEED
            
            elif EVENT_KEY == pygame.K_LEFT:
                MOVE_X_POS -= PLAYER_SPEED
        
        if EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = NOW_EVENT.key
            if EVENT_KEY == pygame.K_DOWN or EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS = 0
            elif EVENT_KEY == pygame.K_LEFT or EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS = 0

            
        return MOVE_X_POS, MOVE_Y_POS

    def BOUNDARY_CHECK(PLAYER_X_POS, PLAYER_Y_POS):

        NOW_PLAYER_X_POS = PLAYER_X_POS
        NOW_PLAYER_Y_POS = PLAYER_Y_POS

        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()

        PLAYER_WIDTH = READ_CHARACTER_DATA["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CHARACTER_DATA["PLAYER_HEIGHT"]

        if NOW_PLAYER_X_POS < 0:
            NOW_PLAYER_X_POS = 0

        elif NOW_PLAYER_X_POS > SCREEN_WIDTH - PLAYER_WIDTH:
            NOW_PLAYER_X_POS = SCREEN_WIDTH - PLAYER_WIDTH

        else:
            pass

        if NOW_PLAYER_Y_POS < 0:
            NOW_PLAYER_Y_POS = 0

        elif NOW_PLAYER_Y_POS > SCREEN_HEIGHT - PLAYER_HEIGHT:
            NOW_PLAYER_Y_POS = SCREEN_HEIGHT - PLAYER_HEIGHT

        else:
            pass

        return NOW_PLAYER_X_POS, NOW_PLAYER_Y_POS

