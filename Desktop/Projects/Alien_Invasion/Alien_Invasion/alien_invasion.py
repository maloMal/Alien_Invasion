import sys

import pygame

from settings import Setting
from ship import Ship
import game_functions as gf


def run_game():
	#Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Setting()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make a Ship
	ship = Ship(ai_settings, screen)

	#Set the Background Color.
	#bg_color = (230, 230, 230)

	#Start the main loop for the game,
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

		#Watch for keyboard and mouse events.
		#for even in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()


		#Make the most reently drawn screen visible.
		#pygame.display.flip()

run_game()