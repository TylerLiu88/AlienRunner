import pygame
import constants
from platforms import MovingPlatform
class Enemy(pygame.sprite.Sprite):

	def __init__(self, platform):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('level_6/Brightness_contrast 1.png')
		self.rect = self.image.get_rect()
		self.dx = 1  # Or whatever speed you want you enemies to walk in.
		self.platform = platform
                
	def update(self):
		self.rect.move(self.dx, 0)
		if self.rect.left > constants.SCREEN_HEIGHT  or self.rect.right <constants.SCREEN_HEIGHT + 100:
			self.dx *= -1
		

