from src.GameFunc.player.PlayerBase import PlayerBase
import pygame


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.sprite = pygame.image.load("D:\\PROJECT\\Python\\AvoidMonster\\참고용\\pygame\\Class\\C_UNKNOWN_CH\\IMG\\CHAR_3.png")
        self.sprite = pygame.image.load(".\\resources\\CHAR_3.png")


class TestPlayer(PlayerBase):
    def __init__(self):
        super().__init__()
        self._player_sprite = PlayerSprite()
        
    @property
    def PlayerSprite(self):
        return self._player_sprite


