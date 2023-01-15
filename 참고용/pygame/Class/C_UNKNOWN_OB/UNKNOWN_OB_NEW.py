import pygame
from Class.RW_JSON import READ_WRITE
import json

CONFIG_DIR = ".\\Config\\Main_Config.json"

class ITEM_OBJECT:
    def OBJECT_INFO(OBJ_NAME, IMG_DIR = None):
        try:
            READ_OBJECT_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)["OBJECT"][f"{OBJ_NAME}"]
            IMG_DIR = READ_OBJECT_DATA["IMG_DIR"]
            OBJECT_IMG = pygame.image.load(IMG_DIR)

            OBJECT_WIDTH = READ_OBJECT_DATA["OBJECT_INFO"]["OBJECT_WIDTH"]
            OBJECT_HEIGHT = READ_OBJECT_DATA["OBJECT_INFO"]["OBJECT_HEIGHT"]
            OBJECT_SPEED = READ_OBJECT_DATA["OBJECT_INFO"]["OBJECT_SPEED"]

            return OBJECT_WIDTH, OBJECT_HEIGHT, OBJECT_IMG, OBJECT_SPEED
        
        except:
            READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
            OBJECT_IMG = pygame.image.load(IMG_DIR)
            OBJECT_SIZE = OBJECT_IMG.get_rect().size

            OBJECT_WIDTH = OBJECT_SIZE[0]
            OBJECT_HEIGHT = OBJECT_SIZE[1]
            OBJECT_SPEED = 15

            with open(CONFIG_DIR, "w", encoding = "utf-8") as WRITE_OBJECT_PROFILE:
                READ_CONFIG_DATA["OBJECT"][f"{OBJ_NAME}"]["OBJECT_INFO"]["OBJECT_WIDTH"] = OBJECT_WIDTH
                READ_CONFIG_DATA["OBJECT"][f"{OBJ_NAME}"]["OBJECT_INFO"]["OBJECT_HEIGHT"] = OBJECT_HEIGHT
                READ_CONFIG_DATA["OBJECT"][f"{OBJ_NAME}"]["OBJECT_INFO"]["OBJECT_SPEED"] = OBJECT_SPEED
                json.dump(READ_CONFIG_DATA, WRITE_OBJECT_PROFILE, indent = 4)
            
            return OBJECT_WIDTH, OBJECT_HEIGHT, OBJECT_IMG, OBJECT_SPEED
    
class ATTACK_OBJECT:
    def DISCHARGE():
        WEAPON_LIST = []

    def BOUNDARY_CHECK(WEAPON_NAME, WEAPON_POS_LIST):
        NOW_WEAPON_X_POS = WEAPON_POS_LIST[0]
        NOW_WEAPON_Y_POS = WEAPON_POS_LIST[1]

        
        