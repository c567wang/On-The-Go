import pygame
from pygame.sprite import Sprite

class Stone(Sprite):
    
    def __init__(self, screen, settings, posx, posy, marker):
        """set stone settings"""
        """turn marker = 0 -> use colour 1"""
        super().__init__()
        self.screen = screen
        self.radius = settings.stone_radius
        self.c1 = settings.stone_c1
        self.c2 = settings.stone_c2
        self.marker = marker
        self.posx = posx
        self.posy = posy