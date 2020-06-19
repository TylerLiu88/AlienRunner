import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet



class Player(pygame.sprite.Sprite):
	"""class represents player controls"""
	
	def __init__(self):
		'''Constructor function'''
	 # Call the parent's constructor
		super().__init__()
 
        # Set speed vector of player
		self.change_x = 0
		self.change_y = 0
		
        # This holds all the images for the animated walk left/right
		self.walking_frames_l = []
		self.walking_frames_r = []
 
        # player facing right
		self.direction = "R"
 
        # List of sprites we can bump against
		self.level = None
		self.mob = None
		sprite_sheet = SpriteSheet("2.png")
        # Load all the right facing images into a list
		image = sprite_sheet.get_image(0, 0, 68, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(68, 0, 68, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(136, 0, 66, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(0, 69, 68, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(68, 69, 68, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(136, 69, 66, 69)
		self.walking_frames_r.append(image)
		image = sprite_sheet.get_image(0, 139, 68, 70)
		self.walking_frames_r.append(image)
 
        # Load all the right facing images, then flip them to face left.
		image = sprite_sheet.get_image(0, 0, 68, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(66, 0, 68, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(136, 0, 66, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(0, 69, 68, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(68, 69, 68, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(136, 69, 66, 69)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_sheet.get_image(0, 139, 68, 70)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
 
        # Set the image the player starts with
		self.image = self.walking_frames_r[0]
 
        # Set a reference to the image rect.
		self.rect = self.image.get_rect()
		
	def update(self):
		""" Move the player. """
        # Player's Gravity
		self.calc_grav()
 
        # Move left or right
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]
 
        # See if player collided with anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right, set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right
		
				
        # Move up/down
		self.rect.y += self.change_y
 
        # Check and see if we collided with anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
			self.change_y = 0
 
			if isinstance(block, MovingPlatform):
				self.rect.x += block.change_x
		#Makes player collison with enemies more accurate
		self.mask = pygame.mask.from_surface(self.image)
	def calc_grav(self):
		""" Calculate effect of gravity. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35
 
        # See if we are on the ground.
		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
 
	def jump(self):
		""" Called when user hits 'jump' button. """
 
        # Move down a bit and see if there is a platform below us. Move down by 2 pixels 
       
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
			self.change_y = -10
 
    # Player-controlled movement:
	def go_left(self):
		""" Called when the user hits the left arrow. """
		self.change_x = -7
		self.direction = "L"
 
	def go_right(self):
		""" Called when the user hits the right arrow. """
		self.change_x = 7
		self.direction = "R"
 
	def stop(self):
		""" Called when the user lets off the keyboard. """
		self.change_x = 0
	def fall(self):
		"""to fall a bit faster"""
		self.change_y += 5
	
