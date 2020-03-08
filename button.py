import pygame.font

class button():
    
    def __init__(self, settings, screen):
        """initiate button settings"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # button attributes
        self.height, self.width = settings.button_height, settings.button_width
        
        # create button's rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    