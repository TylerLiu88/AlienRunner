import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
from random import choice, randrange
from player import Player

class Mob(pygame.sprite.Sprite):
	"""Class for Mobs of enemies"""
	
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
		self.player = None
		
		sprite_sheet = SpriteSheet("spritesheet_jumper.png")
        # Load all the left facing images into a list
		image = sprite_sheet.get_image(814, 1417, 90, 155)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(736, 1063, 114, 155)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_r.append(image)
		
		#reverse all the images
		image = sprite_sheet.get_image(814, 1417, 90, 155)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(704, 1256, 120, 159)
		self.walking_frames_l.append(image)	
 
        # Set the image the player starts with
		self.image = self.walking_frames_l[0]
 
        # Set a reference to the image rect.
		self.rect = self.image.get_rect()
		self.rect.centerx = choice([-100, constants.SCREEN_HEIGHT + 100])
		self.vx = randrange(1,5)
		
		if self.rect.centerx > constants.SCREEN_WIDTH:
			self.vx *= -1
		self.rect.y = randrange(200,500)
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
		else:
			self.image = self.walking_frames_r[1]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.rect.y += self.vy
		if self.rect.left > constants.SCREEN_WIDTH + 100 or self.rect.right < -100:
			self.vx *= -1
		#Make collison with player more accurate
		self.mask = pygame.mask.from_surface(self.image)
		
		
	
       
	
			
		
	
	
