from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        
        vector_one, vector_two = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_one = Asteroid(self.position.x, self.position.y, new_radius)
        split_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        split_one.velocity = vector_one * 1.2
        split_two.velocity = vector_two * 1.2
        
        