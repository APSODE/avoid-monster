

import pygame
from Class.RW_JSON import READ_WRITE
import json
CONFIG_DIR = ".\\Config"

class OBJECT:
    
    def OBJECT_INFO(IMG_DIR):    
        #CHAR_IMG_DIR = "C:\\Users\\Administrator\\Desktop\\게임제작\\Char_SP\\CHAR_1.png"
        #CHAR_IMG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Char_SP\\CHAR_1.png" #학교 컴사용시 캐릭터 이미지 디렉토리
        pi = pygame.image
        OBJECT_IMG = pi.load(IMG_DIR)
        OBJECT_SIZE = OBJECT_IMG.get_rect().size

        OBJECT_WIDTH = OBJECT_SIZE[0]
        OBJECT_HEIGHT = OBJECT_SIZE[1]

        with open(f"{CONFIG_DIR}\\object_config.json", "r", encoding = "utf-8") as READ_OBJECT_PROFILE:
            READ_OBJECT_DATA = json.load(READ_OBJECT_PROFILE)
            READ_OBJECT_PROFILE.close()

        with open(f"{CONFIG_DIR}\\object_config.json", "w", encoding = "utf-8") as WRITE_OBJECT_PROFILE:
            READ_OBJECT_DATA["OBJECT_WIDTH"] = OBJECT_WIDTH
            READ_OBJECT_DATA["OBJECT_HEIGHT"] = OBJECT_HEIGHT

            json.dump(READ_OBJECT_DATA, WRITE_OBJECT_PROFILE, indent = 4)            


        
        
        return OBJECT_WIDTH, OBJECT_HEIGHT, OBJECT_IMG

    def OBJECT_POS():
        
        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\object_config.json", "r", encoding = "utf-8") as READ_OBJECT_PROFILE:
            READ_OBJECT_DATA = json.load(READ_OBJECT_PROFILE)
            READ_OBJECT_PROFILE.close()

        OBJECT_WIDTH = READ_OBJECT_DATA["OBJECT_WIDTH"]
        OBJECT_HEIGHT = READ_OBJECT_DATA["OBJECT_HEIGHT"]

        OBJECT_X_POS = (SCREEN_WIDTH / 2) - (OBJECT_WIDTH / 2) 
        OBJECT_Y_POS = (SCREEN_HEIGHT / 2) - (OBJECT_HEIGHT / 2)

        return OBJECT_X_POS, OBJECT_Y_POS
        
    """
    def PUSH_INTERACTION(PLAYER_POS, OBJECT_INFO, OBJECT_POS):
        
        
        OBJECT_WIDTH = OBJECT_INFO[0]
        OBJECT_HEIGHT = OBJECT_INFO[1]


        PLAYER_X_POS = PLAYER_POS[0]
        PLAYER_Y_POS = PLAYER_POS[1]
        OBJECT_X_POS = OBJECT_POS[0]
        OBJECT_Y_POS = OBJECT_POS[1]

        if PLAYER_X_POS == OBJECT_X_POS or PLAYER_X_POS == (OBJECT_X_POS - OBJECT_WIDTH):
            with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_PLAYER_PROFILE:
                READ_PLAYER_DATA = json.load(READ_PLAYER_PROFILE)
                READ_PLAYER_PROFILE.close()

            PLAYER_SPEED = READ_PLAYER_DATA["PLAYER_SPEED"]
            OBJECT_X_POS += PLAYER_SPEED

        if PLAYER_Y_POS == OBJECT_Y_POS or PLAYER_Y_POS == (OBJECT_Y_POS - OBJECT_HEIGHT):
            with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_PLAYER_PROFILE:
                READ_PLAYER_DATA = json.load(READ_PLAYER_PROFILE)
                READ_PLAYER_PROFILE.close()

            PLAYER_SPEED = READ_PLAYER_DATA["PLAYER_SPEED"]
            OBJECT_Y_POS += PLAYER_SPEED

        return OBJECT_X_POS, OBJECT_Y_POS
    """

    def COLLISION_CHECK(CHAR, C_POS_INFO, OBJECT, O_POS_INFO):
        """
        type(POS_INFO) == list\n
        X_POS == POS_INFO[0]\n
        Y_POS == POS_INFO[1]\n

        리턴
        --------
        CHECK = OBJECT.COLLISION_CHECK(CHAR, POS_INFO)\n
        type(CHECK) == tuple\n
        type(CHECK[0]) == bool\n
        type(CHECK[1]) == char_x_pos\n
        type(CHECK[2]) == char_y_pos\n
        """
        CHAR_X_POS = C_POS_INFO[0]
        CHAR_Y_POS = C_POS_INFO[1]
        CHAR_RECT = CHAR.get_rect()
        CHAR_RECT.left = CHAR_X_POS
        CHAR_RECT.top = CHAR_Y_POS
        #OBJ_IMG_DIR = READ_WRITE.READ_JSON(f"{CONFIG_DIR}\\object_config.json")["OBJECT_IMG_DIR"]["OBJ_1"]
        #OBJECT_RECT = OBJECT.OBJECT_INFO(OBJ_IMG_DIR)[2].get_rect()

        OBJECT_X_POS = O_POS_INFO[0]
        OBJECT_Y_POS = O_POS_INFO[1]
        OBJECT_RECT = OBJECT.get_rect()
        OBJECT_RECT.left = OBJECT_X_POS
        OBJECT_RECT.top = OBJECT_Y_POS
        
        


        if CHAR_RECT.colliderect(OBJECT_RECT):
            return [True]
        else:
            return [False]





    def OBJECT_MOVE(NOW_EVENT, X_POS, Y_POS):
        
        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_OBJECT_PROFILE:
            READ_OBJECT_DATA = json.load(READ_OBJECT_PROFILE)
            READ_OBJECT_PROFILE.close()
        
        MOVE_X_POS = X_POS
        MOVE_Y_POS = Y_POS

        OBJECT_SPEED = READ_OBJECT_DATA["PLAYER_SPEED"]
        EVENT_TYPE = NOW_EVENT.type

        

        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS -= OBJECT_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                MOVE_Y_POS += OBJECT_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS += OBJECT_SPEED
            
            elif EVENT_KEY == pygame.K_LEFT:
                MOVE_X_POS -= OBJECT_SPEED
        
        if EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = NOW_EVENT.key
            if EVENT_KEY == pygame.K_DOWN or EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS = 0
            elif EVENT_KEY == pygame.K_LEFT or EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS = 0

            
        return MOVE_X_POS, MOVE_Y_POS

    def BOUNDARY_CHECK(OBJECT_X_POS, OBJECT_Y_POS):
        

        NOW_OBJECT_X_POS = OBJECT_X_POS
        NOW_OBJECT_Y_POS = OBJECT_Y_POS

        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\object_config.json", "r", encoding = "utf-8") as READ_OBJECT_PROFILE:
            READ_OBJECT_DATA = json.load(READ_OBJECT_PROFILE)
            READ_OBJECT_PROFILE.close()

        OBJECT_WIDTH = READ_OBJECT_DATA["OBJECT_WIDTH"]
        OBJECT_HEIGHT = READ_OBJECT_DATA["OBJECT_HEIGHT"]

        if NOW_OBJECT_X_POS < 0:
            NOW_OBJECT_X_POS = 0

        elif NOW_OBJECT_X_POS > SCREEN_WIDTH - OBJECT_WIDTH:
            NOW_OBJECT_X_POS = SCREEN_WIDTH - OBJECT_WIDTH

        else:
            pass

        if NOW_OBJECT_Y_POS < 0:
            NOW_OBJECT_Y_POS = 0

        elif NOW_OBJECT_Y_POS > SCREEN_HEIGHT - OBJECT_HEIGHT:
            NOW_OBJECT_Y_POS = SCREEN_HEIGHT - OBJECT_HEIGHT

        else:
            pass

        return NOW_OBJECT_X_POS, NOW_OBJECT_Y_POS
