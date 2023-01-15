from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_LEFT, K_RIGHT, K_UP
import UNKNOWN_CH #플레이어블 캐릭터 클래스
import 
import pygame

pygame.init()


pd = pygame.display 

SC_WIDTH = 1280
SC_HEIGHT = 720

SCREEN = pd.set_mode((SC_WIDTH, SC_HEIGHT))
pd.set_caption("김기정 병신")


RUNNING = True
PLAYER_POS = UNKNOWN_CH.PLAYER.PLAYER_INFO(SCREEN_WIDTH = 1280, SCREEN_HEIGHT = 720)
OBJECT_POS = UNKNOWN_OB
PLAYER_X_pos = PLAYER_POS[0]
PLAYER_Y_pos = PLAYER_POS[1]

print(f"PLAYER_X_pos = {PLAYER_X_pos} / PLAYER_Y_pos = {PLAYER_Y_pos}")

MOVE_X_pos = 0 
MOVE_X_pos = 0
CH_MOVE_SPEED = 0.15

while RUNNING:
    for EVENT in pygame.event.get():
        EVENT_TYPE = EVENT.type
        

        if EVENT_TYPE == pygame.QUIT():
            RUNNING = False

        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = EVENT.key
        
            if EVENT_KEY == pygame.K_UP:
                MOVE_Y_pos += CH_MOVE_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                MOVE_Y_pos -= CH_MOVE_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_pos += CH_MOVE_SPEED
            
            elif EVENT_KEY == pygame.K_LEFT:
                MOVE_X_pos += CH_MOVE_SPEED

        if EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = EVENT.key
            if EVENT_KEY == pygame.K_DOWN or EVENT_KEY == pygame.K_UP:
                MOVE_Y_pos = 0
            elif EVENT_KEY == pygame.K_LEFT or EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_pos = 0

        SCREEN.blit()

        









TEST_VALUE = UNKNOWN.PLAYER.PLAYER_POS()

