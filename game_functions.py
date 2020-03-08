# functions in alphabetical order 

import pygame

from stone import Stone

# global variables
turn_marker = 0
occupied = False
cleared = False


def clear_stone(stones, mouse_pos):
    """clear stone chosen"""
    global cleared

    if (315 <= mouse_pos[0] < 885) and (15 <= mouse_pos[1] < 585):
        posx = determine_pt(mouse_pos[0])
        posy = determine_pt(mouse_pos[1])
    
        # check if there is a stone to clear on designated point
        for stone in stones.copy():
            if posx == stone.posx and posy == stone.posy:
                stones.remove(stone)
                cleared = True
                break

def determine_pt(coor):
    """takes x,y coodinates and pulls them to a point on the board"""
    pt = ((coor + 15)//30)*30
    return pt

def draw_stone(stone):
    """draw stone at designated position"""
    if stone.marker == 0:
        pygame.draw.circle(stone.screen, stone.c1, (stone.posx, stone.posy), stone.radius)
    else:
        pygame.draw.circle(stone.screen, stone.c2, (stone.posx, stone.posy), stone.radius)

def get_stone(screen, settings, stones, mouse_pos):
    """get stone at point clicked"""
    global occupied

    if (315 <= mouse_pos[0] < 885) and (15 <= mouse_pos[1] < 585):
        posx = determine_pt(mouse_pos[0])
        posy = determine_pt(mouse_pos[1])
        
        # make stone only if point is unoccupied
        for stone in stones.copy():
            if posx == stone.posx and posy == stone.posy:
                occupied = True
                break
        if not occupied:
            make_stone(screen, settings, posx, posy, turn_marker, stones)
            
        # reset occupied marker
        occupied = False

        
def make_stone(screen, settings, posx, posy, turn_marker, stones):
    cs = Stone(screen, settings, posx, posy, turn_marker)
    stones.add(cs)
    next_turn()

def next_turn():
    """moves turn marker(tm)"""
    global turn_marker
    turn_marker = (turn_marker + 1) % 2

def prep_text(text, fontsize, fontcolour):
    """converts given text into image and places center of image
    at given coordinates"""
    font = pygame.font.SysFont(None, fontsize)
    msg = font.render(text, False, fontcolour)
    return msg