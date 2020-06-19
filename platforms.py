import pygame
from spritesheet_functions import SpriteSheet

#Defined platforms using the spritesheet
#name = (x,y,width, height)
GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504,576, 70, 70)
GRASS_MOVPLAT= (576, 432, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_RIGHT = (648, 648, 70, 40)
STONE_PLATFORM_MIDDLE = (792, 648, 70, 40)
CRATE_01 = (0,864,70,70)
STONE_BLK = (504, 720, 70, 70)
DES_BLK = (216, 0, 70, 70)
DES_BLK_MIDDLE = (288, 504, 70, 70)
DES_BLK_RIGHT = (360, 504, 70, 70)
DES_BLK_LEFT = (360, 648 , 70, 70)
DES_BLK_MOV = (360, 432 , 70, 70)
DES_BLK_S = (576, 792, 70,100)
DES_BLK_R1= (360, 576, 70,70) 
DES_BLK_L1= (360, 720, 70,70)
ICE = (432, 504, 70, 50)
ICE_RIGHT = (216, 720, 70, 70)
ICE_LEFT =( 216, 864, 70, 70)
ICE_MIDDLE =(144, 720, 70, 70)
ICE_S_MID =(288, 72, 70, 70)
ICE_S_LEFT =(288, 0,  70, 70)
ICE_S_RIGHT =(216, 792, 70,70)
ICE_HILL_RIGHT =(216, 216, 70,70)
ICE_HILL_LEFT = (216, 360, 70, 70)
ICE_HILL_RIGHT1 = (216, 144, 70, 70)
ICE_HILL_LEFT1 = (216, 288, 70, 70)
A = (144, 504, 70, 70)
A_LEFT = (144, 432, 70, 70)
A_RIGHT = (144, 288 , 70, 70)
A_MID = (72, 360 , 70, 70)
A_S_RIGHT = (144, 216, 70 ,70)
A_S_LEFT =(144, 360 ,70 ,70)
A_PLAT =(144, 144 , 70 ,70 )
B = (0, 144, 70, 70)
B1 = (0 , 792, 70 ,70)
B2 = (0 , 792, 70 ,40)
w = (504, 216, 70 ,70)
w2 = (432, 576, 70, 70)





class Platform(pygame.sprite.Sprite):
	"""the platform that the user can jump on"""
	def __init__(self, sprite_sheet_data):
		""" Platform constructor. Assumes constructed with user passing in an array of 5 numbers like what's defined at the top of this code. """
		#Recieved help from online
		super().__init__()
		
		sprite_sheet= SpriteSheet("tiles_spritesheet.png")
		
		#grab image for this platform
		self.image = sprite_sheet.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])
		self.rect = self.image.get_rect()
		
class MovingPlatform(Platform):
	"""Platform that can move"""
	
	def __init__(self, sprite_sheet_data):
		super().__init__(sprite_sheet_data)
		
		#set movement for the platforms
		self.change_x = 0
		self.change_y = 0
		
		self.boundary_top = 0
		self.boundary_bottom = 0
		self.boundary_left = 0
		self.boundary_right = 0
		
		self.level = None
		self.player = None
		
	def update(self):
		"""Move the platform."""
		
		#move left or right
		self.rect.x += self.change_x
		
		#see if we collide with player (Horizontal)
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			if self.change_x <0:
				self.player.rect.right = self.rect.left
			else:
				self.player.rect.left = self.rect.right	
			
		
		#Move up or down
		self.rect.y += self.change_y
		
		#see if we collided with player (Vertical)
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:			
			#reset our position based on top and bottom of screen
			if self.change_y <0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom		
		
		#check boundaries to see if we need to reverse direction
		if self.rect.bottom > self.boundary_bottom or self.rect.top <self.boundary_top:
			self.change_y *=-1
			
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1
			
			
		
		
		
		
