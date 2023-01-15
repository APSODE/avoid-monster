import pygame
import json
pygame.init() # 초기화
CONFIG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Config"


class BACKGROUND_INFO:
    def BACKGROUND_WH(IMG_DIR):
        
        with open(f"{CONFIG_DIR}\\display_config.json") as READ_CONFIG_PROFILE:
            READ_CONFIG_DATA = json.load(READ_CONFIG_PROFILE)
            READ_CONFIG_PROFILE.close()
            
        SCREEN_WIDTH = READ_CONFIG_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_CONFIG_DATA["SCREEN_HEIGHT"] 
        
        pd = pygame.display
        pi = pygame.image
        
        SCREEN = pd.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        BACKGROUND = pi.load(IMG_DIR)

        return SCREEN, BACKGROUND
        




"""
class BACKGROUND:
    


    # 화면 크기 설정
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    pygame.display.set_caption("Unknown") # 게임이름

    # 배경 이미지 불러오기
    background = pygame.image.load("C:/Users/Admin/Desktop/1조_project/pygame_basic/background.png")

    # 스프라이트 불러오기
    character = pygame.image.load("C:/Users/Admin/Desktop/1조_project/pygame_basic/block.png")
    character_size = character.get_rect().size # 이미지의 크기를 구해옴
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = (screen_height / 2) - (character_height / 2) # 화면 세로의 가장 아래에 해당하는 곳에 위치

    # 이벤트 루프
    running = True # 게임 진행중인가?
    while running:
        for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
                running = False # 게임 진행중아님

            screen.blit(background, (0, 0)) # 배경그리기

            screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

            pygame.display.update() # 게임화면을 다시 그리기
            """

