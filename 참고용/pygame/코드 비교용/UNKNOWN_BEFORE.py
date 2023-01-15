from Class.UNKNOWN_OB import OBJECT
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_LEFT, K_RIGHT, K_UP
#import UNKNOWN_CH #플레이어블 캐릭터 클래스
from Class.UNKNOWN_CH import PLAYER
#from Class.UNKNOWN_BG.UNKNOWN_BG import 
from Class.EVENT_CHECK import EVENT
from Class.RW_JSON import READ_WRITE
import pygame

pygame.init()
CONFIG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Config\\Main_Config.json"
READ_CONFIG_DATA = READ_WRITE.READ_JSON(CONFIG_DIR)

BACKGROUND_IMG_DIR = READ_CONFIG_DATA["DISPLAY"]["DISPLAY_IMG_DIR"]["IMG_1"]
OBJECT_IMG_DIR = READ_CONFIG_DATA["OBJECT"]["OBJECT_IMG_DIR"]["IMG_1"]
CHAR_ING_DIR = READ_CONFIG_DATA["CHARACTER"]["CHARACTER_IMG_DIR"]["IMG_3"]
ICON_DIR = READ_CONFIG_DATA["ICON"]["ICON_IMG_DIR"]["IMG_1"]
ICON = pygame.image.load(ICON_DIR)


pd = pygame.display 

SC_WIDTH = 1280
SC_HEIGHT = 720

SCREEN = pd.set_mode((SC_WIDTH, SC_HEIGHT))
pd.set_caption("UNKNOWN")
pd.set_icon(ICON)


RUNNING = True
#=======================================플레이어 정보=======================================#
PLAYER_INFO = PLAYER.PLAYER_INFO(CHAR_ING_DIR)#캐릭터 이미지에 대한 정보를 가져옴
PLAYER_WIDTH = PLAYER_INFO[0]#캐릭터 이미지 가로
PLAYER_HEIGHT = PLAYER_INFO[1]#캐릭터 이미지 세로
PLAYER_IMG = PLAYER_INFO[2]#캐릭터 이미지(type = pygame.surface)

PLAYER_POS = PLAYER.PLAYER_POS()#플레이어의 좌표를 지정
PLAYER_X_POS = PLAYER_POS[0] #플레이어 X좌표
PLAYER_Y_POS = PLAYER_POS[1] #플레이어 Y좌표
#=======================================플레이어 정보=======================================#

#=======================================오브젝트 정보=======================================#
OBJECT_INFO = OBJECT.OBJECT_INFO(OBJECT_IMG_DIR)
OBJECT_WIDTH = OBJECT_INFO[0]
OBJECT_HEIGHT = OBJECT_INFO[1]
OBJECT_IMG = OBJECT_INFO[2]

OBJECT_POS = OBJECT.OBJECT_POS()
OBJECT_X_POS = OBJECT_POS[0]
OBJECT_Y_POS = OBJECT_POS[1]
#=======================================오브젝트 정보=======================================#



print(f"PLAYER_X_pos = {PLAYER_X_POS} / PLAYER_Y_pos = {PLAYER_Y_POS} / PLAYER_WIDTH = {PLAYER_WIDTH} / PLAYER_HEIGHT = {PLAYER_HEIGHT}")

MOVE_X_POS = 0 #이동값
MOVE_Y_POS = 0 #이동값
OB_MOVE_X_POS = 0 #이동값
OB_MOVE_Y_POS = 0 #이동값
CH_MOVE_SPEED = READ_WRITE.READ_JSON(CONFIG_DIR)["CHARACTER"]["CHARACTER_INFO"]["PLAYER_SPEED"]#

while RUNNING:
    for NOW_EVENT in pygame.event.get():

        RUNNING = EVENT.EVENT_CHECK(NOW_EVENT) #X버튼을 눌렀으면 게임을 종료함 
        #=================================오브젝트 상호작용 코드=================================#
        CHANGED_PLAYER_POS = [PLAYER_X_POS, PLAYER_Y_POS]
        CHANGED_OBJECT_POS = [OB_MOVE_X_POS,OB_MOVE_Y_POS]
        #OBJECT_MOVE_VALUE = OBJECT.PUSH_INTERACTION(CHANGED_PLAYER_POS, OBJECT_INFO, CHANGED_OBJECT_POS)
        OBJECT_MOVE_VALUE = OBJECT.OBJECT_MOVE(NOW_EVENT, OB_MOVE_X_POS, OB_MOVE_Y_POS)
        
        NOW_MOVE_OBJECT_X_POS = OBJECT_MOVE_VALUE[0]
        NOW_MOVE_OBJECT_Y_POS = OBJECT_MOVE_VALUE[1]




        #=================================오브젝트 상호작용 코드=================================#
        #=================================플레이어 이동 코드=================================#
        PLAYER_MOVE_VALUE = PLAYER.PLAYER_MOVE(NOW_EVENT, MOVE_X_POS, MOVE_Y_POS) #이벤트를 받아와서 플레이어 스프라이트의 움직임을 설정 // PLAYER_MOVE_VALUE에는 이동값이 담겨있음
        NOW_MOVE_X_POS = PLAYER_MOVE_VALUE[0]
        NOW_MOVE_Y_POS = PLAYER_MOVE_VALUE[1]
        CHAR_COLLISION_CHECK = OBJECT.COLLISION_CHECK(CHAR = PLAYER_IMG, C_POS_INFO = [PLAYER_X_POS, PLAYER_Y_POS], OBJECT = OBJECT_IMG, O_POS_INFO = [OBJECT_X_POS, OBJECT_Y_POS]) 
        #충돌 확인 / 충돌시 list형식으로 인덱스 0번 ~ 2번까지 반환 / 0번 : 충돌이면 True, 1번 ~ 2번 : CHAR_X_POS, CHAR_X_POS


        if CHAR_COLLISION_CHECK[0] == True: #만약 충돌체크 값이 True라면 밑에 구문 실행
            MOVE_X_POS = 0
            MOVE_Y_POS = 0

        elif CHAR_COLLISION_CHECK[0] == False:
            MOVE_X_POS = NOW_MOVE_X_POS
            MOVE_Y_POS = NOW_MOVE_Y_POS
        #=================================플레이어 이동 코드=================================#


        
            


        

    PLAYER_X_POS += MOVE_X_POS
    PLAYER_Y_POS += MOVE_Y_POS 

    PLAYER_POS_CHECK = PLAYER.BOUNDARY_CHECK(PLAYER_X_POS, PLAYER_Y_POS) #화면 경계 제한
    OBJECT_POS_CHECK = OBJECT.BOUNDARY_CHECK(OBJECT_X_POS, OBJECT_Y_POS)

    PLAYER_X_POS = PLAYER_POS_CHECK[0]
    PLAYER_Y_POS = PLAYER_POS_CHECK[1]

    

        


    BACKGROUND_INFO = UNKNOWN_BG.BACKGROUND_INFO.BACKGROUND_WH(BACKGROUND_IMG_DIR)#백그라운드 이미지에 대한 정보를 받아옴
    SCREEN = BACKGROUND_INFO[0] #SCREEN을 반환
    BACKGROUND = BACKGROUND_INFO[1] #백그라운드 이미지를 반환

    SCREEN.blit(BACKGROUND, (0, 0))#백그라운드를 생성
    SCREEN.blit(PLAYER_IMG, (PLAYER_X_POS, PLAYER_Y_POS))#플레이어를 생성
    #SCREEN.blit()
    pd.update()

pygame.quit()


        

        











