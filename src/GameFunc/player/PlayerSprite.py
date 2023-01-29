from typing import *
import pygame

from src.GameFunc.player.PlayerMoveData import PlayerMoveData


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_sf = pygame.image.load(".\\resources\\CHAR_3.png")  # sprite surface
        self.size = self.sprite_sf.get_size()
        self._sprite_num_data = {
            "s": 1,  # 멈춰있는 상태의 스프라이트 이미지 번호
            "w": 1,  # 움직이는 상태의 스프라이트 이미지 번호
            "s_M": 18,  # 멈춰있는 상태의 스프라이트 이미지의 최대 번호
            "w_M": 24  # 움직이는 상태의 스프라이트 이미지의 최대 번호
        }
        self._last_update_tick = 0
        self._update_delay = 25
        self._resources_dir = ".\\resources\\player\\"

    def _SpriteUpdateTimeCheck(self, now_tick: int) -> bool:
        return now_tick - self._last_update_tick > self._update_delay

    def UpdateSprite(self, move_data: PlayerMoveData, update_delay: int = 25):  # 25ms(단위 : 밀리세컨드)
        if self._update_delay != update_delay:
            self._update_delay = update_delay

        if move_data.MovingStatus:  #움직임 여부 확인
            current_sprite_num_key = "w"
            max_sprite_num_key = "w_M"
            resource_dir = self._resources_dir + "move\\walk_"

        else:
            current_sprite_num_key = "s"
            max_sprite_num_key = "s_M"
            resource_dir = self._resources_dir + "standing\\standing_"

        if self._sprite_num_data.get(current_sprite_num_key) > self._sprite_num_data.get(max_sprite_num_key):
            self._sprite_num_data[current_sprite_num_key] = 1

        now_game_tick = pygame.time.get_ticks()

        if self._SpriteUpdateTimeCheck(now_tick = now_game_tick):
            resource_dir += f"{self._sprite_num_data.get(current_sprite_num_key)}.png"
            current_sprite_image = pygame.image.load(resource_dir)
            self.sprite_sf = pygame.transform.flip(
                surface = current_sprite_image,
                flip_x = False if move_data.X_Move > 0 else True,
                flip_y = False
            )

            self._sprite_num_data[current_sprite_num_key] += 1
            self._last_update_tick = now_game_tick

