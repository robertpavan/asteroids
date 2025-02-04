import pygame
from constants import *
from circleshape import *
from shot import *

# Create a new file called player.py with a Player class that inherits from CircleShape.
# The Player class should have a constructor that takes x and y parameters.

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.timer = 0

        # Create a transparent surface for self.image that's big enough for the triangle
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        # Create self.rect from that surface and position it
        self.rect = self.image.get_rect(center=(x, y))
        self.draw_triangle()  # Move drawing to separate method

    # in the player class
    # def triangle(self):
    #     forward = pygame.Vector2(0, 1).rotate(self.rotation)
    #     right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    #     a = self.position + forward * self.radius
    #     b = self.position - forward * self.radius - right
    #     c = self.position - forward * self.radius + right
    #     return [a, b, c]

    def draw_triangle(self):
        # Clear the surface before first draw
        self.image.fill((0, 0, 0))  # Transparent
        # Move the triangle drawing code to update the image instead of drawing directly to the screen
        pygame.draw.polygon(self.image, (255, 255, 255), self.triangle())

    # Modify the triangle() method to return coordinates relative to the surface size instead of screen coordinates
    def triangle(self):
        # Calculate relative to center of surface
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        center = pygame.Vector2(self.radius, self.radius)  # Center of surface
        
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    # def draw(self, screen):
    #     pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width = 2)

    # def rotate(self, dt):
    #     self.rotation += PLAYER_TURN_SPEED * dt

    # In the rotate() method, after changing rotation, redraw the triangle on self.image
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.draw_triangle()  # Use same method here

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

        if self.timer > 0:
            self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # In the move() method, after updating self.position, update self.rect.center
        self.rect.center = self.position

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.containers[0].add(shot)  # Add the shot to the updatable group
        self.containers[1].add(shot)  # Add the shot to the drawable group
        self.timer = PLAYER_SHOOT_COOLDOWN