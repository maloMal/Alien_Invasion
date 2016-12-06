import sys

import pygame
from pygame.sprite import Group

from settings import Setting
from ship import Ship
from bullet import Bullet
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
    #Make a group to store bullets in.
    bullets = Group()

	#Set the Background Color.
	#bg_color = (230, 230, 230)

	#Start the main loop for the game,
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
        bullets.update()
		gf.update_screen(ai_settings, screen, ship, bullets)
        
        #redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

		#Watch for keyboard and mouse events.
		#for even in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()


		#Make the most reently drawn screen visible.
		pygame.display.flip()

run_game()