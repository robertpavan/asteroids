import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, width=2)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(random.uniform(-50, 50), random.uniform(-50, 50))

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width = 2)

    def update(self, dt):
        # Move position using velocity
        self.position += self.velocity * dt
        # Update rect position (so Pygame knows where to draw)
        self.rect.center = (int(self.position.x), int(self.position.y))

    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity * 1  # Create first copy
        new_velocity2 = self.velocity * 1  # Create second copy

        # Now rotate the copies
        new_velocity1 = new_velocity1.rotate(random_angle)
        new_velocity2 = new_velocity2.rotate(-random_angle)

        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = new_velocity1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = new_velocity2 * 1.2

        asteroids.add(new_asteroid1)
        asteroids.add(new_asteroid2)