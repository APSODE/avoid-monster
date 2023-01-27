from typing import *
import pygame


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.sprite = pygame.image.load("D:\\PROJECT\\Python\\AvoidMonster\\참고용\\pygame\\Class\\C_UNKNOWN_CH\\IMG\\CHAR_3.png")
        self.sprite_sf = pygame.image.load(".\\resources\\CHAR_3.png") # sprite surface
        self.size = self.sprite_sf.get_size()
        self._standing_sprite_num = 1
        self._walk_sprite_num = 1
        self._last_update = 0

    def StandingAnimation(self, update_delay: int = 25): #TODO 플레이어 애니메이션을 한곳에서 관리하도록 해야함
        now_game_tick = pygame.time.get_ticks()  # 단위 ms(밀리세컨드)

        if self._standing_sprite_num >= 19:
            self._standing_sprite_num = 1

        update_tick_check = now_game_tick - self._last_update > update_delay  # 100밀리초마다 이미지 갱신

        print(
            f"update tick check : {update_tick_check}\n"
            f"now tick : {now_game_tick}ms\n"
            f"last update : {self._last_update}ms\n\n"
        )
        if update_tick_check:
            self.sprite_sf = pygame.image.load(
                f".\\resources\\player\\standing\\standing_{self._standing_sprite_num}.png"
            )

            self._standing_sprite_num += 1
            self._last_update = now_game_tick

    # 플레이어 이동 키이벤트가 발생했을때만 작동
    def WalkAnimation(self, update_delay: int = 100): #TODO 플레이어 애니메이션을 한곳에서 관리하도록 해야함
        now_game_tick = pygame.time.get_ticks() #단위 ms(밀리세컨드)

        if self._walk_sprite_num >= 25: #플레이어 애니메이션 스프라이트 갯수를 초과확인용
            self._walk_sprite_num = 1

        update_tick_check = now_game_tick - self._last_update > update_delay # 100밀리초마다 이미지 갱신
        print(
            f"update tick check : {update_tick_check}\n"
            f"now tick : {now_game_tick}ms\n"
            f"last update : {self._last_update}ms\n\n"
        )
        if update_tick_check:
            self.sprite_sf = pygame.image.load(f".\\resources\\player\\move\\walk_{self._walk_sprite_num}.png")

            self._walk_sprite_num += 1
            self._last_update = now_game_tick







