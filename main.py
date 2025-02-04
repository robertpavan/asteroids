# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

# Use an infinite while loop for the game loop. At each iteration, it should:
# Use the screen's fill method to fill the screen with a solid "black" color.
# Use pygame's display.flip() method to refresh the screen. Be sure to call this last!

	running = True
	while running:
		screen.fill((0,0,0))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == "__main__":
	main()
