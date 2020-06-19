"""Pull Sprite from sprite sheets"""
import pygame
import constants

class SpriteSheet(object):
	"""Used to grab sprites from sprite sheet"""
	def __init__(self,file_name):
		
		#Load Sprite sheet
		self.sprite_sheet = pygame.image.load(file_name).convert()
		
	def get_image(self, x,y,width,height):
		""" Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        #Create blank image
		image= pygame.Surface([width,height]).convert()
        
        #Copy the sprite from the large sheet onto smaller image
		image.blit(self.sprite_sheet, (0,0), (x , y, width, height))
        
        #assuming that black words are transparent in color
		image.set_colorkey(constants.White)
        
        #return image
		return image
        
       
