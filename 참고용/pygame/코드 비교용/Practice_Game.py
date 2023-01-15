import pygame
import random
import os

disgus_img_dir = f"D:\\건보\\동기화\\Naver MYBOX\\C언어반 예습\\매크로\\디스코드 봇 만들기\\images_file\\kimki"



Images_file_list = list(os.listdir(disgus_img_dir))
Image_file_count = len(Images_file_list) 




Rnd_NUM = random.randint(0, Image_file_count)


#실행
pygame.init()

#sc = screen
sc_width = 640
sc_height = 480 

pd = pygame.display
pe = pygame.event
pi = pygame.image

clock = pygame.time.Clock()

sc = pd.set_mode((sc_width, sc_height))

pd.set_caption("김기정 남창") 
Background = pi.load(f"{disgus_img_dir}\\kimimage{Rnd_NUM}.jpg")
print(f"사용된 사진 : kimimage{Rnd_NUM}.jpg")

char = pi.load("D:\\Download\\Skeleton Sprite Pack\\Skeleton\\GIFS\\Skeleton_Walk.gif")
char_sz = char.get_rect().size
char_width = char_sz[0]
char_height = char_sz[1]

char_X_pos = (sc_width / 2) - (char_width / 2)
char_Y_pos = sc_height - char_height


to_X = 0
to_Y = 0
char_speed = 0.25

Running = True

while Running:
    #이벤트를 뽑아오는애
    for event in pe.get():
        et = event.type
        dt = clock.tick(60)

        if et == pygame.QUIT:
            Running = False

        if et == pygame.KEYDOWN:
            ek = event.key 

            if ek == pygame.K_LEFT:
                to_X -= char_speed 

            elif ek == pygame.K_RIGHT:
                to_X += char_speed

            elif ek == pygame.K_UP:
                to_Y -= char_speed
                
            elif ek == pygame.K_DOWN:
                to_Y += char_speed

        if et == pygame.KEYUP: #     ||  ==>  or && ==> and
            if ek == pygame.K_LEFT or ek == pygame.K_RIGHT:
                to_X = 0

            elif ek == pygame.K_UP or ek == pygame.K_DOWN:
                to_Y = 0

    #나온 값으로 비교하거나 실행하는애
    char_X_pos += to_X
    char_Y_pos += to_Y

    #가로 경계 처리
    if char_X_pos < 0:
        char_X_pos = 0
    elif char_X_pos > sc_width - char_width:
        char_X_pos = sc_width - char_width

    #세로 정지 처리
    if char_Y_pos < 0:
        char_Y_pos = 0
    elif char_Y_pos > sc_height - char_height:
        char_Y_pos = sc_height - char_height


    #sc.blit(Background, (0, 0))
    sc.fill((0, 0, 255))
    sc.blit(char, (char_X_pos, char_Y_pos))
    pd.update()

#종료
pygame.quit()
