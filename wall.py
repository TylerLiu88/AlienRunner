import pygame
import constants


class Wall(pygame.sprite.Sprite):
	def __init___(self, x, y, width, height):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(Black)
		
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		
		
		
	
