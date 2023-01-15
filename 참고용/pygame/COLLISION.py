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
        
        CHAR_IMG = CHAR_INFO_LIST[0] #pygame.image.load(IMG_DIR)을 사용해 IMG 정보를 가져온다.
        NOW_PLAYER_X_POS = CHAR_INFO_LIST[1][0] #현재 플레이어 이미지의 X좌표 
        NOW_PLAYER_Y_POS = CHAR_INFO_LIST[1][1] #현재 플레이어 이미지의 Y좌표

        OBJ_IMG = OBJ_INFO_LIST[0] #pygame.image.load(IMG_DIR)을 사용해 IMG 정보를 가져온다.
        NOW_OBJECT_X_POS = OBJ_INFO_LIST[1][0] #현재 오브젝트 이미지의 X좌표
        NOW_OBJECT_Y_POS = OBJ_INFO_LIST[1][1] #현재 오브젝트 이미지의 Y좌표

        CHAR_IMG_RECT = CHAR_IMG.get_rect() #IMG정보의 rect값을 가져오는 함수
        CHAR_IMG_RECT.left = NOW_PLAYER_X_POS #IMG정보의 rect값의 left값에 현재 플레이어 이미지의 X좌표를 저장
        CHAR_IMG_RECT.top = NOW_PLAYER_Y_POS #IMG정보의 rect값의 top값에 현재 플레이어 이미지의 Y좌표를 저장

        OBJ_IMG_RECT = OBJ_IMG.get_rect() #IMG정보의 rect값을 가져오는 함수
        OBJ_IMG_RECT.left = NOW_OBJECT_X_POS #IMG정보의 rect값의 left값에 현재 오브젝트 이미지의 X좌표를 저장
        OBJ_IMG_RECT.top = NOW_OBJECT_Y_POS #IMG정보의 rect값의 top값에 현재 오브젝트 이미지의 Y좌표를 저장

        if CHAR_IMG_RECT.colliderect(OBJ_IMG_RECT): #만약 플레이어의 rect정보가 오브젝트의 rect정보와 충돌한다면, True를 반환
            #CHAR_IMG_RECT.colliderect(OBJ_IMG_RECT) ==> return : bool
            #이때 충돌을 감지하는 코드로 사용가능하므로 충돌이벤트가 True라면 어떤 이벤트를 실행할지를 지정가능
            return True




