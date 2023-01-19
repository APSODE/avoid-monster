from typing import *
import pygame


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.sprite = pygame.image.load("D:\\PROJECT\\Python\\AvoidMonster\\참고용\\pygame\\Class\\C_UNKNOWN_CH\\IMG\\CHAR_3.png")
        self.sprite_sf = pygame.image.load(".\\resources\\CHAR_3.png") # sprite surface
        self.size = self.sprite_sf.get_size()
