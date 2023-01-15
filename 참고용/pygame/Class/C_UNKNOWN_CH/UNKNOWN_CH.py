
import json, pygame
from Class.FUNC.RW_JSON import READ_WRITE


CONFIG_DIR = ".\\Config\\Main_Config.json"


class PLAYER:

    def PLAYER_INFO(CHAR_NAME, IMG_DIR = None):
        try:
            READ_CHARACTER_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]
            IMG_DIR = READ_CHARACTER_DATA["IMG_DIR"]
            PLAYER_IMG = pygame.image.load(IMG_DIR)
            PLAYER_WIDTH = READ_CHARACTER_DATA["INFO"]["PLAYER_WIDTH"]
            PLAYER_HEIGHT = READ_CHARACTER_DATA["INFO"]["PLAYER_HEIGHT"]
            PLAYER_SPEED = READ_CHARACTER_DATA["INFO"]["PLAYER_SPEED"]

            
            return PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_IMG, PLAYER_SPEED

        except:
            PLAYER_IMG = pygame.image.load(IMG_DIR)
            PLAYER_SIZE = PLAYER_IMG.get_rect().size
            PLAYER_SPEED = 15
            PLAYER_WIDTH = PLAYER_SIZE[0]
            PLAYER_HEIGHT = PLAYER_SIZE[1]
            READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
            with open(CONFIG_DIR, "w", encoding = "utf-8") as WRITE_CHARACTER_PROFILE:
                READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["IMG_DIR"] = IMG_DIR
                READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_WIDTH"] = PLAYER_WIDTH
                READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_HEIGHT"] = PLAYER_HEIGHT
                READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_SPEED"] = PLAYER_SPEED
                json.dump(READ_CONFIG_DATA, WRITE_CHARACTER_PROFILE, indent = 4)
            
            return PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_IMG, PLAYER_SPEED

    def PLAYER_POS(CHAR_NAME):
        READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        SCREEN_WIDTH = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_INFO"]["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_INFO"]["SCREEN_HEIGHT"]
        PLAYER_WIDTH = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_HEIGHT"]

        PLAYER_BASIC_X_POS = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2)
        PLAYER_BASIC_Y_POS = (SCREEN_HEIGHT / 2) - (PLAYER_HEIGHT / 2)

        return PLAYER_BASIC_X_POS, PLAYER_BASIC_Y_POS

    # def PLAYER_MOVE_NEW(CHAR_NAME, NOW_EVENT, MOVE_POS_LIST):
    #     with open(CONFIG_DIR, "r", encoding = "utf-8") as READ_CONFIG_PROFILE:
    #         READ_CONFIG_DATA = json.load(READ_CONFIG_PROFILE)
    #         READ_CONFIG_PROFILE.close()
        
    #     PLAYER_SPEED = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYR_SPEED"]
    #     MOVE_X_POS

    def PLAYER_MOVE(CHAR_NAME, NOW_EVENT, MOVE_POS_LIST):
        """
        PLAYER_POS_LIST_TYPE = list
        PLAYER_POS_LIST[0] = PLAYER_X_POS
        PLAYER_POS_LIST[1] = PLAYER_Y_POS
        """
        READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)

        with open(CONFIG_DIR, "w", encoding = 'utf-8') as WRITE_CHARACTER_PROFILE:
            READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["MOVE_INFO"]["MOVE_X_POS"] = 0
            READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["MOVE_INFO"]["MOVE_Y_POS"] = 0
            json.dump(READ_CONFIG_DATA, WRITE_CHARACTER_PROFILE, indent = 4)
            
        #READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        with open(CONFIG_DIR, "r", encoding = "utf-8") as READ_CONFIG_PROFILE:
            READ_CONFIG_DATA = json.load(READ_CONFIG_PROFILE)
            READ_CONFIG_PROFILE.close()

        PLAYER_SPEED = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_SPEED"]
        MOVE_X_POS = MOVE_POS_LIST[0]
        MOVE_Y_POS = MOVE_POS_LIST[1]

        EVENT_TYPE = NOW_EVENT.type

        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                MOVE_Y_POS += PLAYER_SPEED

            elif EVENT_KEY == pygame.K_LEFT:
                MOVE_X_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS += PLAYER_SPEED

        elif EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_DOWN or pygame.K_UP:
                MOVE_Y_POS = 0

            elif EVENT_KEY == pygame.K_LEFT or pygame.K_RIGHT:
                MOVE_X_POS = 0


        with open(CONFIG_DIR, "w", encoding = 'utf-8') as WRITE_CHARACTER_PROFILE:
            READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["MOVE_INFO"]["MOVE_X_POS"] = MOVE_X_POS
            READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["MOVE_INFO"]["MOVE_Y_POS"] = MOVE_Y_POS
            json.dump(READ_CONFIG_DATA, WRITE_CHARACTER_PROFILE, indent = 4)
        #print(f"MOVE_X_POS = {MOVE_X_POS}")
        #print(f"MOVE_Y_POS = {MOVE_Y_POS}")



    
    def BOUNDARY_CHECK(CHAR_NAME, PLAYER_POS_LIST):
        """
        PLAYER_POS_LIST_TYPE = list
        PLAYER_POS_LIST[0] = MOVE_PLAYER_X_POS
        PLAYER_POS_LIST[1] = MOVE_PLAYER_Y_POS
        """

        NOW_PLAYER_X_POS = PLAYER_POS_LIST[0]
        NOW_PLAYER_Y_POS = PLAYER_POS_LIST[1]

        READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        SCREEN_WIDTH = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_INFO"]["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_INFO"]["SCREEN_HEIGHT"]

        PLAYER_WIDTH = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_HEIGHT"]
        # print(f"NOW_PLAYER_X_POS = {NOW_PLAYER_X_POS}")
        # print(f"SCREEN_WIDTH - PLAYER_WIDTH = {SCREEN_WIDTH - PLAYER_WIDTH}")
        # print(f"NOW_PLAYER_Y_POS = {NOW_PLAYER_Y_POS}")
        # print(f"SCREEN_HEIGHT - PLAYER_HEIGHT = {SCREEN_HEIGHT - PLAYER_HEIGHT}")
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

    def COLLISION_CHECK(CHAR_INFO_LIST, OBJ_INFO_LIST):
        """
        CHAR_INFO_LIST_TYPE = list
        CHAR_INFO_LIST[0] = PLAYER_IMG
        CHAR_IMFO_LIST[1] = PLAYER_POS_LIST ==> PLAYER_POS_LIST[0] = PLAYER_X_POS / PLAYER_POS_LIST[1] = PLAYER_Y_POS
        OBJECT도 동일
        """
        
        CHAR_IMG = CHAR_INFO_LIST[0]
        NOW_PLAYER_X_POS = CHAR_INFO_LIST[1][0]
        NOW_PLAYER_Y_POS = CHAR_INFO_LIST[1][1]

        OBJ_IMG = OBJ_INFO_LIST[0]
        NOW_OBJECT_X_POS = OBJ_INFO_LIST[1][0]
        NOW_OBJECT_Y_POS = OBJ_INFO_LIST[1][1]

        CHAR_IMG_RECT = CHAR_IMG.get_rect()
        CHAR_IMG_RECT.left = NOW_PLAYER_X_POS
        CHAR_IMG_RECT.top = NOW_PLAYER_Y_POS

        OBJ_IMG_RECT = OBJ_IMG.get_rect()
        OBJ_IMG_RECT.left = NOW_OBJECT_X_POS
        OBJ_IMG_RECT.top = NOW_OBJECT_Y_POS

        if CHAR_IMG_RECT.colliderect(OBJ_IMG_RECT):
            return True

