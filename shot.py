import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, width=2)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width = 2)    

    def update(self, dt):
        # Move position using velocity
        self.position += self.velocity * dt
        # Update rect position (so Pygame knows where to draw)
        self.rect.center = (int(self.position.x), int(self.position.y))
