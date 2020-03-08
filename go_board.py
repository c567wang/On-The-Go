import pygame

class GoBoard():
    """go board scaled to screen"""

    def __init__(self, screen):
        """initialize board settings"""
        # get images and rects
        self.screen = screen
        self.image = pygame.image.load('images/go_board.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # align board with right side of screen
        self.rect.right = self.screen_rect.right

    def blitme(self):
        """blit board onto screen"""
        self.screen.blit(self.image, self.rect)