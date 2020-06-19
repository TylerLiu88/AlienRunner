import pygame
import constants
import platforms
from enemy import Mob


class Level():
	"""Super class used to define a level"""
	def __init__(self, player):
		"""initialize the player"""
				
		#background image
		self.background = None
		
		#How far world will be scrolled left or right
		self.world_shift = 0
		self.level_limit = -1000
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
	
	#update everything on level
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()
			
	def draw(self, screen):
		"""Draw everythin on this level"""
		#Draw Background
		screen.fill(constants.White)
		screen.blit(self.background, (self.world_shift// 3,0))
		
		#Draw all the sprite list 
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
		
		
	def shift_world(self, shift_x):
		"""everytime we move left or right the world will move as well"""
		#keep track of shift 
		self.world_shift += shift_x
		
		#pass through all of sprites and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x
			
		for enemy in self.enemy_list:
			enemy.rect.x += shift_x
			
		
		'''
class Level_01(Level):
	"""Level 1 of my game"""
	def __init__(self, player):
		
		#call the parent constructor
		Level.__init__(self,player)
		#load background
		self.background = pygame.image.load("B1_new2.png").convert()
		self.background.set_colorkey(constants.White)
		self.level_limit = -1700
		
		 # Array with type of platform, and x, y location of the platform.
		level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.GRASS_LEFT, 1120, 280],
                  [platforms.GRASS_MIDDLE, 1190, 280],
                  [platforms.GRASS_RIGHT, 1260, 280],
                  [platforms.GRASS_LEFT, 1500, 400],
                  [platforms.GRASS_MIDDLE, 1570, 400],
                  [platforms.GRASS_RIGHT, 1640, 400],
                  [platforms.GRASS_LEFT, 1710 , 300],
                  [platforms.GRASS_MIDDLE, 1780, 300],
                  [platforms.GRASS_MIDDLE, 1970, 225],
                  [platforms.GRASS_MIDDLE, 2100, 500], 
                  [platforms.CRATE_01, -72,550], 
                  [platforms.CRATE_01, -72,500], 
                  [platforms.CRATE_01, -72,450], 
                  [platforms.CRATE_01, -72,400], 
                  [platforms.CRATE_01, -72,350],
                  [platforms.CRATE_01, -72,300],
                  [platforms.CRATE_01, -72,250], 
                  [platforms.CRATE_01, -72,200], 
                  [platforms.CRATE_01, -72,150],
                  [platforms.CRATE_01, -144,550], 
                  [platforms.CRATE_01, -144,500], 
                  [platforms.CRATE_01, -144,450], 
                  [platforms.CRATE_01, -144,400], 
                  [platforms.CRATE_01, -144,350],
                  [platforms.CRATE_01, -144,300],
                  [platforms.CRATE_01, -144,250], 
                  [platforms.CRATE_01, -144,200], 
                  [platforms.CRATE_01, -144,150],
                  [platforms.CRATE_01, -72,100], 
                  [platforms.CRATE_01, -72,50], 
                  [platforms.CRATE_01, -72,0], 
                  [platforms.CRATE_01, -144,150], 
                  [platforms.CRATE_01, -144,100],
                  [platforms.CRATE_01, -144,50],
                  [platforms.CRATE_01, -144,0], 
                  ]
                  
           # Go through the array above and add platforms
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
 
        # Add a custom moving platform
		block = platforms.MovingPlatform(platforms.GRASS_MOVPLAT)
		block.rect.x = 1350
		block.rect.y = 280
		block.boundary_left = 1350
		block.boundary_right = 1600
		block.change_x = 1
		block.player = self.player
		block.level = self
		self.platform_list.add(block)

# Create platforms for the level
class Level_02(Level):
    """ Level 2 """
 
    def __init__(self, player):
        """ Create level 2. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("Level_2/Level2B.png").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -3000
 
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.STONE_PLATFORM_LEFT, 800, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 870, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 940, 400],
                  [platforms.STONE_PLATFORM_LEFT, 1000, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 1070, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_BLK, -72,550], 
                  [platforms.STONE_BLK, -72,500], 
                  [platforms.STONE_BLK, -72,450], 
                  [platforms.STONE_BLK, -72,400], 
                  [platforms.STONE_BLK, -72,350],
                  [platforms.STONE_BLK, -72,300],
                  [platforms.STONE_BLK, -72,250], 
                  [platforms.STONE_BLK, -72,200], 
                  [platforms.STONE_BLK, -72,150],
                  [platforms.STONE_BLK, -144,550], 
                  [platforms.STONE_BLK, -144,500], 
                  [platforms.STONE_BLK, -144,450], 
                  [platforms.STONE_BLK, -144,400], 
                  [platforms.STONE_BLK, -144,350],
                  [platforms.STONE_BLK, -144,300],
                  [platforms.STONE_BLK, -144,250], 
                  [platforms.STONE_BLK, -144,200], 
                  [platforms.STONE_BLK, -144,150],
                  [platforms.STONE_BLK, -72,100], 
                  [platforms.STONE_BLK, -72,50], 
                  [platforms.STONE_BLK, -72,0], 
                  [platforms.STONE_BLK, -144,150], 
                  [platforms.STONE_BLK, -144,100],
                  [platforms.STONE_BLK, -144,50],
                  [platforms.STONE_BLK, -144,0],
                  [platforms.STONE_PLATFORM_MIDDLE, 1900, 160],
                  [platforms.STONE_PLATFORM_MIDDLE, 2100, 500], 
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform (vertical)
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #moving platform (horizontal)
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1650
        block.rect.y = 280
        block.boundary_left = 1650
        block.boundary_right = 2000
        block.change_x = 4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
            
class Level_03(Level):
	"""Level 3 of the game"""
	
	def __init__(self, player):
		#load/create player and the background
		Level.__init__(self,player)
	
		self.background = pygame.image.load("Level_3/Level3B.png").convert()
		self.background.set_colorkey(constants.White)
		self.level_limit = -3000
    
		#Array with type of platform
		level = [[platforms.DES_BLK_LEFT, 500, 550],
                  [platforms.DES_BLK_MIDDLE, 570, 550],
                  [platforms.DES_BLK_RIGHT, 640, 550],
                  [platforms.DES_BLK_LEFT, 800, 400],
                  [platforms.DES_BLK_MIDDLE, 870, 400],
                  [platforms.DES_BLK_RIGHT, 940, 400],
                  [platforms.DES_BLK_S, 845, 465],
                  [platforms.DES_BLK_S, 845, 535],
                  [platforms.DES_BLK_S, 845, 610],
                  [platforms.DES_BLK_S, 895, 465],
                  [platforms.DES_BLK_S, 895, 535],
                  [platforms.DES_BLK_S, 895, 610],
                  [platforms.DES_BLK_LEFT, 1000, 500],
                  [platforms.DES_BLK_MIDDLE, 1070, 500],
                  [platforms.DES_BLK_RIGHT, 1140, 500],
                  [platforms.DES_BLK_S, 1045,570],
                  [platforms.DES_BLK_S, 1095, 570],
                  [platforms.DES_BLK_L1, 1160, 260],
                  [platforms.DES_BLK_MIDDLE, 1230, 260],
                  [platforms.DES_BLK_R1, 1300, 260],
                  ]
 
 
		# Go through the array above and add platforms
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
			
		# Add a custom moving platform
		block = platforms.MovingPlatform(platforms.DES_BLK_MOV)
		block.rect.x = 1500
		block.rect.y = 300
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -5
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.DES_BLK_MOV)
		block.rect.x = 1650
		block.rect.y = 280
		block.boundary_left = 1650
		block.boundary_right = 1900
		block.change_x = 7
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.DES_BLK_MOV)
		block.rect.x= 1500
		block.rect.y=500
		block.boundary_left = 1500
		block.boundary_right = 1900
		block.change_x = 50
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
class Level_04(Level):
	"""Level 4 of the game"""
	
	def __init__(self, player):
		#load player and background
		Level.__init__(self,player)
		self.background = pygame.image.load("Level_4/Level4B.png").convert()
		self.background.set_colorkey(constants.White)
		self.level_limit = -2900
		
		  # Array with type of platform, and x, y location of the platform.
		level = [ 	[platforms.ICE, -72,550], 
					[platforms.ICE, -72,500], 
					[platforms.ICE, -72,450], 
					[platforms.ICE, -72,400], 
					[platforms.ICE, -72,350],
					[platforms.ICE, -72,300],
					[platforms.ICE, -72,250], 
					[platforms.ICE, -72,200], 
					[platforms.ICE, -72,150],
					[platforms.ICE, -144,550], 
					[platforms.ICE, -144,500], 
					[platforms.ICE, -144,450], 
					[platforms.ICE, -144,400], 
					[platforms.ICE, -144,350],
					[platforms.ICE, -144,300],
					[platforms.ICE, -144,250], 
					[platforms.ICE, -144,200], 
					[platforms.ICE, -144,150],
					[platforms.ICE, -72,100], 
					[platforms.ICE, -72,50], 
					[platforms.ICE, -72,0], 
					[platforms.ICE, -144,150], 
					[platforms.ICE, -144,100],
					[platforms.ICE, -144,50],
					[platforms.ICE, -144,0],
					[platforms.ICE_LEFT, 500, 550],
					[platforms.ICE_MIDDLE, 570, 550],
					[platforms.ICE_RIGHT, 640, 550],
					[platforms.ICE_LEFT, 800, 400],
					[platforms.ICE_MIDDLE, 870, 400],
					[platforms.ICE_RIGHT, 940, 400],
					[platforms.ICE_S_MID, 845, 465],
					[platforms.ICE_S_MID, 845, 535],
					[platforms.ICE_S_MID, 845, 610],
					[platforms.ICE_S_MID, 895, 465],
					[platforms.ICE_S_MID, 895, 535],
					[platforms.ICE_S_MID, 895, 610],
					[platforms.ICE_LEFT, 1000, 500],
					[platforms.ICE_MIDDLE, 1070, 500],
					[platforms.ICE_RIGHT, 1140, 500],
					[platforms.ICE_S_MID, 1045,570],
					[platforms.ICE_S_MID, 1095, 570],
					[platforms.ICE_S_LEFT, 1120, 280],
					[platforms.ICE_MIDDLE, 1190, 280],
					[platforms.ICE_S_RIGHT, 1260, 280],
					[platforms.ICE_HILL_LEFT, 1440, 430],
					[platforms.ICE_HILL_LEFT, 1510, 360],
					[platforms.ICE_HILL_LEFT, 1580, 290],
					[platforms.ICE_HILL_LEFT1, 1580, 360],
					[platforms.ICE_HILL_LEFT1, 1510, 430],
					[platforms.ICE_HILL_RIGHT, 1650, 290 ],
					[platforms.ICE_HILL_RIGHT, 1720, 360],
					[platforms.ICE_HILL_RIGHT, 1790, 430],
					[platforms.ICE_HILL_RIGHT1, 1720, 430],
					[platforms.ICE_HILL_RIGHT1, 1650, 360],
					[platforms.ICE_S_MID, 1650, 430],
					[platforms.ICE_S_MID, 1580, 430],
					[platforms.ICE_MIDDLE, 1900, 160],
					[platforms.ICE_MIDDLE, 2100, 500], 
					]
 
 
        # Go through the array above and add platforms
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
'''
'''
class Level_05(Level):
	def __init__(self, player):
		#Player and background
		Level.__init__(self,player)
		self.background = pygame.image.load("Level_5/Level5B.png").convert()
		self.background.set_colorkey(constants.White)
		self.level_limit = -2500
		
		 # Array with type of platform, and x, y location of the platform.
		level = [ 	[platforms.A, -72,550], 
					[platforms.A, -72,500], 
					[platforms.A, -72,450], 
					[platforms.A, -72,400], 
					[platforms.A, -72,350],
					[platforms.A, -72,300],
					[platforms.A, -72,250], 
					[platforms.A, -72,200], 
					[platforms.A, -72,150],
					[platforms.A, -144,550], 
					[platforms.A, -144,500], 
					[platforms.A, -144,450], 
					[platforms.A, -144,400], 
					[platforms.A, -144,350],
					[platforms.A, -144,300],
					[platforms.A, -144,250], 
					[platforms.A, -144,200], 
					[platforms.A, -144,150],
					[platforms.A, -72,100], 
					[platforms.A, -72,50], 
					[platforms.A, -72,0], 
					[platforms.A, -144,150], 
					[platforms.A, -144,100],
					[platforms.A, -144,50],
					[platforms.A, -144,0],
					[platforms.A_LEFT, 500, 550],
					[platforms.A_MID, 570, 550],
					[platforms.A_RIGHT, 640, 550],
					[platforms.A_LEFT, 800, 400],
					[platforms.A_MID, 870, 400],
					[platforms.A_RIGHT, 940, 400],
					[platforms.ICE_S_MID, 845, 465],
					[platforms.ICE_S_MID, 845, 535],
					[platforms.ICE_S_MID, 845, 610],
					[platforms.ICE_S_MID, 895, 465],
					[platforms.ICE_S_MID, 895, 535],
					[platforms.ICE_S_MID, 895, 610],
					[platforms.A_S_LEFT, 1000, 500],
					[platforms.A_MID, 1070, 500],
					[platforms.A_S_RIGHT, 1140, 500],
					[platforms.ICE_S_MID, 1045,570],
					[platforms.ICE_S_MID, 1095, 570],
					[platforms.A_LEFT, 1120, 280],
					[platforms.A_MID, 1190, 280],
					[platforms.A_RIGHT, 1260, 280],
					[platforms.A_LEFT, 2500, 400],
					[platforms.A_MID, 2570, 400],
					[platforms.A_RIGHT, 2640, 400],
					[platforms.ICE_S_MID, 2525, 465],
					[platforms.ICE_S_MID, 2525, 535],
					[platforms.ICE_S_MID, 2525, 610],
					[platforms.ICE_S_MID, 2595, 465],
					[platforms.ICE_S_MID, 2595, 535],
					[platforms.ICE_S_MID, 2595, 610],
					
					] 
		# Use the array to make platforms			
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
						
					
			
		# Add a custom moving platform
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x = 1650
		block.rect.y = 280
		block.boundary_left = 1650
		block.boundary_right = 1900
		block.change_x = 7
		block.player = self.player
		block.level = self
		self.platform_list.add(block) 
		
		#Vertical
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x = 1900
		block.rect.y = 350
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -7
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x = 2100
		block.rect.y = 200
		block.boundary_top = 200
		block.boundary_bottom = 550
		block.change_y = -7
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x= 1500
		block.rect.y=500
		block.boundary_left = 1500
		block.boundary_right = 2100
		block.change_x = 50
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x= 2200
		block.rect.y=200
		block.boundary_left = 2200
		block.boundary_right = 2400
		block.change_x = 6
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.A_PLAT)
		block.rect.x= 2300
		block.rect.y=350
		block.boundary_left = 2300
		block.boundary_right = 2500
		block.change_x = 8
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Vertical
		block = platforms.MovingPlatform(platforms.A_MID)
		block.rect.x = 2750
		block.rect.y = 350
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -50
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		# Add special monster (does not actually collide with player)
		self.enemy_list.add(Mob())
'''
class Level_06(Level):
	def __init__(self, player):
		#load/create player and background
		Level.__init__(self,player)
		self.background = pygame.image.load("Level_6/Level6B.png").convert()
		self.background.set_colorkey(constants.White)
		self.level_limit = -2500
		
		 # Array with type of platform, and x, y location of the platform.
		level = [ 	[platforms.B, -72,550], 
					[platforms.B, -72,500], 
					[platforms.B, -72,450], 
					[platforms.B, -72,400], 
					[platforms.B, -72,350],
					[platforms.B, -72,300],
					[platforms.B, -72,250], 
					[platforms.B, -72,200], 
					[platforms.B, -72,150],
					[platforms.B, -144,550], 
					[platforms.B, -144,500], 
					[platforms.B, -144,450], 
					[platforms.B, -144,400], 
					[platforms.B, -144,350],
					[platforms.B, -144,300],
					[platforms.B, -144,250], 
					[platforms.B, -144,200], 
					[platforms.B, -144,150],
					[platforms.B, -72,100], 
					[platforms.B, -72,50], 
					[platforms.B, -72,0], 
					[platforms.B, -144,150], 
					[platforms.B, -144,100],
					[platforms.B, -144,50],
					[platforms.B, -144,0],
					[platforms.B1, 500, 550],
					[platforms.B1, 570, 550],
					[platforms.B1, 640, 550],
					[platforms.B1, 800, 400],
					[platforms.B1, 870, 400],
					[platforms.B1, 940, 400],
					[platforms.B1, 1000, 500],
					[platforms.B1, 1070, 500],
					[platforms.B1, 1140, 500],
					[platforms.B1, 1045,570],
					[platforms.B1, 1095, 570],
					[platforms.B1, 1120, 280],
					[platforms.B1, 1190, 280],
					[platforms.B1, 1260, 280],
					[platforms.B1, 2500, 400],
					[platforms.B1, 2570, 400],
					[platforms.B1, 2640, 400],
					[platforms.B1, 2500, 470],
					[platforms.B1, 2570, 470],
					[platforms.B1, 2640, 470],
					[platforms.B1, 2500, 540],
					[platforms.B1, 2570, 540],
					[platforms.B1, 2640, 540],
					] 
		#Go through array and add platforms			
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)
						
		# Add a custom moving platform
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x = 1650
		block.rect.y = 280
		block.boundary_left = 1650
		block.boundary_right = 1900
		block.change_x = 7
		block.player = self.player
		block.level = self
		self.platform_list.add(block) 
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x = 1900
		block.rect.y = 350
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -7
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Vertical
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x = 2100
		block.rect.y = 200
		block.boundary_top = 200
		block.boundary_bottom = 550
		block.change_y = -7
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x= 1500
		block.rect.y=500
		block.boundary_left = 1500
		block.boundary_right = 2100
		block.change_x = 50
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x= 2200
		block.rect.y=200
		block.boundary_left = 2200
		block.boundary_right = 2400
		block.change_x = 6
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Horizontal
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x= 2300
		block.rect.y=350
		block.boundary_left = 2300
		block.boundary_right = 2500
		block.change_x = 8
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		
		#Vertical
		block = platforms.MovingPlatform(platforms.B2)
		block.rect.x = 2750
		block.rect.y = 350
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -50
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
		

								
			  
	
		
		
