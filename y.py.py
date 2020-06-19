import pygame
import constants
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage a bullet fired from ship"""
	def __init__(self, screen, player):
		"""Create a bullet oject at the ships current position""" 
		super(Bullet, self).__init__()
		self.screen = screen
		
	#create a bullet rect at (0,0) and then set correct position.
		self.rect = pygame.Rect(0, 0, 100, 100)
		self.rect.centerx = player.rect.centerx
	
	
	#store the bullets position as a decimal
		self.y = float(self.rect.x)
		
		self.color = constants.Blue
		self.speed_factor = 10
	def update(self):
		"""Move the bullet up the screen"""
		#update decimal position the bullet
		self.x -= self.speed_factor
		#update the rect position
		self.rect.x = self.x
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

