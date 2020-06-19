import pygame
import constants
from random import choice, randrange
from spritesheet_functions import SpriteSheet

class Mob_3(pygame.sprite.Sprite):
	"""Third and possibly final monster?"""
	
	def __init__(self):
		super().__init__()
		
		 # Set speed vector of player
		self.change_x = 0
		self.change_y = 0
		self._layer = constants.Mob_layer
        # This holds all the images for the animated walk left/right
		self.walking_frames_l = []
		
		
 
        # player facing right
		self.direction = "L"
 
        # List of sprites we can bump against
		self.level = None
		
		
		sprite_sheet = SpriteSheet("Enemies/frame-2.png")
        
		
		#reverse all the images
		image = sprite_sheet.get_image(0, 0, 369, 369)
		image = pygame.transform.scale(image, (50,50))
		self.walking_frames_l.append(image)
		
		
	
 
        # Set the image the player starts with
		self.image = self.walking_frames_l[0]
 
        # Set a reference to the image rect.
		self.rect = self.image.get_rect()
		self.rect.centerx = choice([-100, constants.SCREEN_HEIGHT + 100])
		self.vx = 8
		
		if self.rect.centerx > constants.SCREEN_WIDTH:
			self.vx *= -1
		self.rect.y = randrange(0,100)
		self.vy = 0
		self.dy = 0.5
		
	def update(self):
		"""Move the Enemy"""
		self.rect.x += self.vx
		self.vy += self.dy
		if self.vy > 3 or self.vy < -3:
			self.dy *= -1
		center = self.rect.center
		
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.rect.y += self.vy
		if self.rect.left > constants.SCREEN_WIDTH + 100 or self.rect.right < -100:
			self.vx *= -1
		#Make collision with player only by direct contactt with the outline of the enemy
		self.mask = pygame.mask.from_surface(self.image)
	
