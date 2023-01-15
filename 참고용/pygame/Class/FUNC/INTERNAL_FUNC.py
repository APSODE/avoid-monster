import json, pygame, sys, os, time, datetime
from Class.FUNC.RW_JSON import READ_WRITE

class INTERNAL_FUNC:
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
