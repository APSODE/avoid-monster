
from Class.C_UNKNOWN_BG.UNKNOWN_BG import BACKGROUND_INFO
from Class.C_UNKNOWN_CH.UNKNOWN_CH import PLAYER
#from Class.UNKNOWN_OB.UNKNOWN_OB import OBJECT
from Class.FUNC.RW_JSON import READ_WRITE
from Class.FUNC.EVENT_CHECK import EVENT
import pygame

class M_INTERNAL_FUNC:
    def GET_IMG_RECT(PYGAME_IMG):
        IMG_RECT = PYGAME_IMG.get_rect()
        return IMG_RECT


pygame.init()
CONFIG_DIR = ".\\Config\\Main_Config.json"

READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR) #Main_Config의 설정 값을 읽어옴



#CONFIG 양식을 변경하여서, JSON데이터를 불러오는 구문에서 JSON데이터 & 키 값 다시 설정
#==================================사용할 이미지의 디렉토리 가져오기==================================#
BACKGROUND_IMG_DIR = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_IMG_DIR"]
#OBJECT_IMG_DIR = READ_CONFIG_DATA["OBJECT"]["OBJECT_1"]["OBJECT_IMG_DIR"]
#CHAR_ING_DIR = READ_CONFIG_DATA["CHARACTER"]["CHARACTER_IMG_DIR"]["IMG_3"]
ICON_DIR = READ_CONFIG_DATA["ICON"]["ICON_IMG_DIR"]["IMG_1"]
#==================================사용할 이미지의 디렉토리 가져오기==================================#


#==================================프로그램 표시 정보 기본 설정==================================#
ICON = pygame.image.load(ICON_DIR)
pygame.display.set_icon(ICON)
pygame.display.set_caption("UNKNOWN")
#==================================프로그램 아이콘 이미지 불러오기==================================#


#==================================화면 너비 설정(해상도 설정)==================================#
DISPLAY_INFO = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_1"]["DISPLAY_INFO"]
SCREEN_WIDTH = DISPLAY_INFO["SCREEN_WIDTH"]
SCREEN_HEIGHT = DISPLAY_INFO["SCREEN_HEIGHT"]

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# C_SCREEN_WIDTH = pygame.display.Info().current_w
# C_SCREEN_HEIGHT = pygame.display.Info().current_h
# print(f"C_SCREEN_WIDTH = {C_SCREEN_WIDTH}")
# print(f"C_SCREEN_HEIGHT = {C_SCREEN_HEIGHT}")
#pygame.display.toggle_fullscreen()
#==================================화면 너비 설정(해상도 설정)==================================#


#==================================작동 상태 설정(작동 : True / 종료 : Fasle)==================================#
RUNNING = True
#==================================작동 상태 설정(작동 : True / 종료 : Fasle)==================================#


#==================================플레이어 정보 가져오기==================================#
#CHAR_NAME = "CHAR_1"
#CHAR_IMG_DIR = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["IMG_DIR"]
CHAR_NAME = "E_CHAR_1"
CHAR_IMG_DIR = f".\\Class\\C_UNKNOWN_CH\\IMG\\{CHAR_NAME}.png"
#print(CHAR_NAME)
PLAYER_INFO = PLAYER.PLAYER_INFO(CHAR_NAME, CHAR_IMG_DIR) #플레이어의 이미지에 대한 정보를 list의 형태로 가져옴
PLAYER_WIDTH = PLAYER_INFO[0] #플레이어 이미지의 가로 길이
PLAYER_HEIGHT = PLAYER_INFO[1] #플레이어 이미지의 세로 길이
PLAYER_IMG = PLAYER_INFO[2] #플레이어 이미지 정보
PLAYER_RECT = PLAYER_INFO[3] #플레이어의 Rect정보


PLAYER_POS = PLAYER.PLAYER_POS(CHAR_NAME) #플레이어의 초기 좌표 가져오기
PLAYER_X_POS = PLAYER_POS[0] #플레이어의 기본 X 좌표
PLAYER_Y_POS = PLAYER_POS[1] #플레이어의 기본 Y 좌표
#==================================플레이어 정보 가져오기==================================#

#좌표 테스트 용 오브젝트
T_CHAR_NAME = "CHAR_3"
T_CHAR_IMG_DIR = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{T_CHAR_NAME}"]["IMG_DIR"]
T_PLAYER_INFO = PLAYER.PLAYER_INFO(T_CHAR_NAME, T_CHAR_IMG_DIR)
T_PLAYER_WIDTH = T_PLAYER_INFO[0]
T_PLAYER_HEIGHT = T_PLAYER_INFO[1]
T_PLAYER_IMG = T_PLAYER_INFO[2]

T_PLAYER_X_POS = 0
T_PLAYER_Y_POS = 0
T_PLAYER_POS = [T_PLAYER_X_POS, T_PLAYER_Y_POS]


#==================================오브젝트 정보 가져오기==================================#
# OBJECT_INFO = OBJECT.OBJECT_INFO(OBJECT_IMG_DIR) #오브젝트의 이미지에 대한 정보를 list 형태로 가져옴
# OBJECT_WIDTH = OBJECT_INFO[0] #오브젝트의 가로 길이
# OBJECT_HEIGTH = OBJECT_INFO[1] #오브젝트의 세로 길이
# OBJECT_IMG = OBJECT_INFO[2] #오브젝트의 이미지 정보

# OBJECT_POS = OBJECT.OBJECT_POS() #오브젝트의 초기 좌표 가져오기
# OBJECT_X_POS = OBJECT_POS[0] #오브젝트의 X 죄표
# OBJECT_Y_POS = OBJECT_POS[1] #오브젝트의 Y 죄표
#==================================오브젝트 정보 가져오기==================================#


#==================================좌표 이동값==================================#
CH_MOVE_X_POS = 0 #플레이어 이동값 (X좌표)
CH_MOVE_Y_POS = 0 #플레이어 이동값 (Y죄표)
MOVE_POS_LIST = [CH_MOVE_X_POS, CH_MOVE_Y_POS]

OB_MOVE_X_POS = 0 #오브젝트 이동값 (X죄표)
OB_MOVE_Y_POS = 0 #오브젝트 이동값 (Y죄표)
#==================================좌표 이동값==================================#


while RUNNING: #RUNNING의 상태에 따라 무한반복문이 (실행/종료)
    
    pygame.time.Clock().tick(60000) #오브젝트의 움직임이 끊긴다 싶으면 증가 시킬 것
    for NOW_EVENT in pygame.event.get(): #NOW_EVENT에 게임에서 발생하는 모든 이벤트가 들어간다.
        #==================================종료 이벤트 구분==================================#
        RUNNING = EVENT.CLOSE_EVENT_CHECK(NOW_EVENT) #현재 발생한 EVENT가 종료이벤트라면 ==> RUNNING = Fasle
        #==================================종료 이벤트 구분==================================#

 
        #==================================플레이어 이동==================================#
        # NOW_MOVE_POS_LIST = PLAYER.PLAYER_MOVE(CHAR_NAME, NOW_EVENT, MOVE_POS_LIST)
        # CH_MOVE_X_POS = NOW_MOVE_POS_LIST[0]
        # CH_MOVE_Y_POS = NOW_MOVE_POS_LIST[1]
        # PLAYER.PLAYER_MOVE(CHAR_NAME, NOW_EVENT, MOVE_POS_LIST)
        # READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)
        # NOW_MOVE_PLAYER_POS_LIST = READ_CONFIG_DATA["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["MOVE_INFO"]
        # for MOVE_POS in NOW_MOVE_PLAYER_POS_LIST:
        #     if MOVE_POS == "MOVE_X_POS":
        #         CH_MOVE_X_POS = NOW_MOVE_PLAYER_POS_LIST[MOVE_POS]
        #     elif MOVE_POS == "MOVE_X_POS":
        #         CH_MOVE_Y_POS = NOW_MOVE_PLAYER_POS_LIST[MOVE_POS]

        # CH_MOVE_X_POS = NOW_MOVE_PLAYER_POS_LIST[0]
        # CH_MOVE_Y_POS = NOW_MOVE_PLAYER_POS_LIST[1]
        # print(f"CH_MOVE_X_POS = {CH_MOVE_X_POS}")
        # print(f"CH_MOVE_Y_POS = {CH_MOVE_Y_POS}")
        #=================================================작동 확인=================================================#
        EVENT_TYPE = NOW_EVENT.type
        PLAYER_SPEED = READ_WRITE.READ_JSON(CONFIG_DIR)["CHARACTER"]["PLAYER"][f"{CHAR_NAME}"]["INFO"]["PLAYER_SPEED"]
        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_UP:
                CH_MOVE_Y_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                CH_MOVE_Y_POS += PLAYER_SPEED

            elif EVENT_KEY == pygame.K_LEFT:
                CH_MOVE_X_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                CH_MOVE_X_POS += PLAYER_SPEED

            elif EVENT_KEY == pygame.K_g or EVENT_KEY == pygame.K_KP_0: #K_g = G키 / K_KP_0 = 숫자패드 0키 // 공격 키 (G키 : 플레이어 1 / 0키 : 플레이어 2)
                if EVENT_KEY == pygame.K_g: #플레이어 1
                    pass
                
                elif EVENT_KEY == pygame.K_KP_0: #플레이어 2
                    pass

        elif EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_DOWN or EVENT_KEY == pygame.K_UP:
                CH_MOVE_Y_POS = 0

            elif EVENT_KEY == pygame.K_LEFT or EVENT_KEY == pygame.K_RIGHT:
                CH_MOVE_X_POS = 0
        #=================================================작동 확인=================================================#
        #NOW_PLAYER_POS_LIST = [(PLAYER_X_POS + MOVE_PLAYER_POS_LIST[0]), (PLAYER_Y_POS + MOVE_PLAYER_POS_LIST[1])]

        
        #PLAYER_POS_LIST = [PLAYER_X_POS, PLAYER_Y_POS]

        #OBJECT_POS_LIST = [OBJECT_X_POS, OBJECT_Y_POS]

        #OBJECT_MOVE_VALUE = OBJECT.OBJECT_MOVE(NOW_EVENT, OB_MOVE_X_POS, OB_MOVE_Y_POS)
    PLAYER_X_POS += CH_MOVE_X_POS
    PLAYER_Y_POS += CH_MOVE_Y_POS
    NOW_PLAYER_POS_LIST = [PLAYER_X_POS, PLAYER_Y_POS]

    BOUNDARY_CHECK_POS_LIST = PLAYER.BOUNDARY_CHECK(CHAR_NAME, NOW_PLAYER_POS_LIST)
    VERIFIED_PLAYER_X_POS = BOUNDARY_CHECK_POS_LIST[0]
    VERIFIED_PLAYER_Y_POS = BOUNDARY_CHECK_POS_LIST[1]
    PLAYER_X_POS = VERIFIED_PLAYER_X_POS
    PLAYER_Y_POS = VERIFIED_PLAYER_Y_POS


    BACKGROUND_INFO_LIST = BACKGROUND_INFO.BACKGROUND_WH(BACKGROUND_IMG_DIR)
    SCREEN = BACKGROUND_INFO_LIST[0]
    BACKGROUND = BACKGROUND_INFO_LIST[1]

    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(T_PLAYER_IMG, T_PLAYER_POS)
    #pygame.transform.rotate(PLAYER_IMG, 90)
    #SCREEN.blit(PLAYER_IMG, (PLAYER_X_POS, PLAYER_Y_POS))
    SCREEN.blit(pygame.transform.rotate(PLAYER_IMG, -90), (PLAYER_X_POS, PLAYER_Y_POS))
    
    pygame.display.update()


pygame.quit()