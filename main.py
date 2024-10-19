# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # get a new GUI

    while True:                                                     # create a game loop
        for event in pygame.event.get():                            # makes window close button work
            if event.type == pygame.QUIT:                           # by checking if player closed window
                return    
        screen.fill((0, 0 , 0))                                     # fill the screen with black color
        pygame.display.flip()                                       # refresh the screen


if __name__ == "__main__":
    main()