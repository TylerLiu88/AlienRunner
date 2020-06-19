import pygame
import constants
from spritesheet_functions import SpriteSheet
from random import choice, randrange

class Mob_2(pygame.sprite.Sprite):
	"""Second Enemy"""
	
	def __init__(self):
		super().__init__()
		
		 # Set speed vector of player
		self.change_x = 0
		self.change_y = 0
		self._layer = constants.Mob_layer
        # This holds all the images for the animated walk left/right
		self.walking_frames_l = []
		self.walking_frames_r = []
		
 
        # player facing right
		self.direction = "L"
 
        # List of sprites we can bump against
		self.level = None
		
		#load the sprite sheet that I am using
		sprite_sheet = SpriteSheet("spritesheet_jumper.png")
        # Load all the left facing images into a list
		image = sprite_sheet.get_image(0, 1152, 260, 134)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_r.append(image)
		
		#Reverse the image
		image = sprite_sheet.get_image(0, 1152, 260, 134)
		self.walking_frames_l.append(image)
		
 
        # Set the image the player starts with
		self.image = self.walking_frames_l[0]
 
        # Set a reference to the image rect.
		self.rect = self.image.get_rect()
		self.rect.centerx = choice([-100, constants.SCREEN_HEIGHT + 100])
		self.vx = 1
		
		if self.rect.centerx > constants.SCREEN_WIDTH:
			self.vx *= -1
		self.rect.y = randrange(400,550)
		self.vy = 0
		self.dy = 0.5
		
	def update(self):
		"""Move the Enemy"""
		self.rect.x += self.vx
		self.vy += self.dy 
		if self.vy > 3 or self.vy < -3:
			self.dy *= -1
		center = self.rect.center
		if self.dy < 0:
			self.image = self.walking_frames_r[0]

		self.rect = self.image.get_rect()
		self.rect.center = center
		self.rect.y += self.vy
		if self.rect.left > constants.SCREEN_WIDTH + 100 or self.rect.right < -100:
			self.vx *= -1
		#Make collision with player more concise 
		self.mask = pygame.mask.from_surface(self.image)
	
