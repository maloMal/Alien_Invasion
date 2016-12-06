import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        
        
def check_keyup_events(event, ship):
    """respond to keyreleases.""""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
			#if event.key == pygame.K_RIGHT:
				#ship.moving_right = True
				#Move the ship to the right
				#ship.rect.centerx += 1
                #elif event.key == pygame.K_LEFT:
				#ship.moving_left = True
		elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
			#if event.key == pygame.K_RIGHT:
			#	ship.moving_right = False
			#elif event.key == pygame.K_LEFT:
			#	ship.moving_left = False
def update_screen(ai_settings, screen, ship):
	"""Update images on screen and flip to the new screen"""
	#Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#Make the most recently drawn screen visible.
	pygame.display.flip()
