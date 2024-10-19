# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # get a new GUI

    clock = pygame.time.Clock()                                     # instanciate a clock object
    dt = 0                                                          # initialize delta time

    updatable = pygame.sprite.Group()                               # create groups
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)                       # add Player class to groups
    Asteroid.containers = (updatable, drawable, asteroids)          # add Asteroid class to groups
    AsteroidField.containers = (updatable)                          # add AsteroidField class to group

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                # instanciate a player object
    field = AsteroidField()                                         # instanciate an asteroid field object

    while True:                                                     # create a game loop
        for event in pygame.event.get():                            # makes window close button work
            if event.type == pygame.QUIT:                           # by checking if player closed window
                return    
        
        screen.fill((0, 0 , 0))                                     # fill the screen with black color
        
        for object in drawable:
            object.draw(screen)                                     # draw player on screen

        for object in updatable:
            object.update(dt)                                       # updates player position

        for object in asteroids:
            if object.collision_check(player):
                print("Game over!")
                sys.exit()


        pygame.display.flip()                                       # refresh the screen
        
        dt = (clock.tick(60)) / 1000                                # pause the loop for 1/60th of a second
                                                                    # assign return delta time to dt as seconds

if __name__ == "__main__":
    main()