import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = max(self.radius - ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS)

        for _ in range(2):
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            # generate random angle
            angle = int(random.uniform(20, 50))
            # rotate the velocity vector by the random angle
            new_velocity = self.velocity.rotate(random.randint(-angle, angle))
            new_asteroid.velocity = new_velocity * 1.2
            new_asteroid.add(self.containers)
            


        