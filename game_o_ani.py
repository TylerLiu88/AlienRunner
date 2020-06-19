import pygame
import constants
from spritesheet_functions import SpriteSheet
from random import choice, randrange

class x(pygame.sprite.Sprite):
	"""Game Over Animation"""
	
	def __init__(self):
		
		super().__init__()
		   # player facing right
		self.direction = "L"
		self.walking_frames = []
        # List of sprites we can bump against
		self.level = None
		image = pygame.image.load("Enemies/frame-1.png")
        # Load all the left facing images into a list
		self.walking_frames.append(image)
		
		image2= pygame.image.load("Enemies/frame-2.png")
	
		self.walking_frames.append(image2)
	
 
        # Set the image the player starts with
		self.image = self.walking_frames[0]
		self.image2 = self.walking_frames[1]
		
        # Set a reference to the image rect.
		self.rect = self.image.get_rect()
		
		self.vx = 6
		self.rect.y = 100
		self.vy = 0
		self.dy = 0
		
	def update(self):
		"""Move the Enemy"""
		self.rect.x += self.vx
		self.vy += self.dy
		center = self.rect.center
		#if self.dy < 0:
		#	self.image = self.walking_frames[0]

		self.rect = self.image.get_rect()
		self.rect.center = center
		self.rect.y += self.vy
		if self.rect.left > constants.SCREEN_WIDTH + 100 or self.rect.right < -100:
			self.vx *= -1
		
