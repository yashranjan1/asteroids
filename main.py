import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteriodfield import AsteroidField
from constants import *

def main():
    # initialise game
    pygame.init()
    
    # create a clock to limit the game to 60 fps
    clock = pygame.time.Clock()
    dt = 0
    
    # creating the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups for managing updates to the screen
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    # create a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidfield = AsteroidField() 

    while True:
        # incase the user quits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        # fill the background in black
        screen.fill("#000000")

        # draw all obj
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.hasCollidedWith(shot):
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.hasCollidedWith(player):
                print("Game over!")
                exit()
        
        for obj in drawable:
            obj.draw(screen)

        # for refreshing the display
        pygame.display.flip()
        
        # for making the game wait before the next frame is rendered
        dt_ms = clock.tick(60) 
        dt = dt_ms / 1000


if __name__ == '__main__':
    main()