import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "#FFFFFF", self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_i]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)                       
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        x, y = self.position.x, self.position.y
        shot = Shot(x, y)
        # Create vector pointing up, then rotate using from_polar
        velocity = pygame.Vector2()
        velocity.from_polar((1, self.rotation + 90 ))  # Note the negative rotation
        velocity *= PLAYER_SHOT_SPEED
        shot.velocity = velocity 