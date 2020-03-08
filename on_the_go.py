import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from go_board import GoBoard
import game_functions as gf

def run_game():
    # initialize game and create screen instance
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("On the Go")

    board = GoBoard(screen)
    stones = Group()

    # create messages
    # title
    title = gf.prep_text("Go...On the Go!", 48, (0, 0, 0))
    title_rect = title.get_rect()
    title_rect.x, title_rect.y = 5, 20

    # main loop
    while True:

        # monitor events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    gf.get_stone(screen, settings, stones, mouse_pos)
                elif event.button == 3:
                    gf.clear_stone(stones, mouse_pos)

        # update screen
        screen.fill(settings.bg_colour)
        board.blitme()
        screen.blit(title, title_rect)
        for stone in stones.sprites():
            gf.draw_stone(stone)

        pygame.display.flip()

run_game()