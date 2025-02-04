# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0

	# Create the player once before the loop

	# create the empty groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# set the containers
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	updatable.add(asteroid_field)
	Shot.containers = (shots, updatable, drawable)

	# create the player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
    	
		screen.fill((0, 0, 0))

		# Calculate delta time
		dt = clock.tick(60) / 1000

		# Update and draw the player
		updatable.update(dt)
		drawable.draw(screen)

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_if_collide(shot):
					asteroid.split(asteroids)
					shot.kill()

		for asteroid in asteroids:
			if asteroid.check_if_collide(player):
				print("Game over!")
				sys.exit()

		# Update the display
		pygame.display.flip()

if __name__ == "__main__":
	main()
