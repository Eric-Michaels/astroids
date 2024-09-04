import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from userinterface import UserInterface


def main():
    pygame.init()
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize UserInterface
    ui = UserInterface(screen)

    dt = 0
    kill_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) and player.health <= 0:
                print(f"Game over! {kill_count} asteroids destroyed.")
                sys.exit()
            elif asteroid.collides_with(player) and player.armour >= 1:
                print(f"Armour is at {player.armour}, health is at {player.health}")
                player.armour -= 1
                print(f"Armour is now at {player.armour}, health is at {player.health}")
                asteroid.kill()
            elif asteroid.collides_with(player) and player.health > 0:
                print(f"Armour is at {player.armour}, health is at {player.health}")
                player.health -= 50
                print(f"Armour is now at {player.armour}, health is at {player.health}")
                asteroid.kill()
                if player.health <= 0:
                    print(f"Game over! {kill_count} asteroids destroyed.")
                    sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    kill_count += 1

        screen.fill("black")
        ui.render(player, kill_count)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
