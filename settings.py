class Settings():
    """settings for the library"""

    def __init__(self):
        """initialize game settings"""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_colour = (200, 200, 150)
        
        # stone settings
        self.stone_radius = 15
        self.stone_c1 = (0, 0, 0)
        self.stone_c2 = (255, 255, 255)

        # button settings
        self.button_height = 100
        self.button_width = 200
        self.button_fontsize = 50

        # manual text
        self.mantxt = "Left click to place stones\nRight click to remove stones" 
        self.mantxt += "\n\nHave fun!"