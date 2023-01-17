from src.GameFunc.player.PlayerBase import PlayerBase
import pygame


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


class TestPlayer(PlayerBase):
    def __init__(self):
        super().__init__()
        self._player_sprite = PlayerSprite()
        
    @property
    def PlayerSprite(self):
        return self._player_sprite


