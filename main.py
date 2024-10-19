# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # get a new GUI

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:                                                     # create a game loop
        for event in pygame.event.get():                            # makes window close button work
            if event.type == pygame.QUIT:                           # by checking if player closed window
                return    
        screen.fill((0, 0 , 0))                                     # fill the screen with black color
        
        player.draw(screen)                                         # draw player on screen

        pygame.display.flip()                                       # refresh the screen
        
        dt = (clock.tick(60)) / 1000                                # pause the loop for 1/60th of a second
                                                                    # assign return delta time to dt as seconds

if __name__ == "__main__":
    main()