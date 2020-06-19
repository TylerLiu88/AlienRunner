import pygame
import pygame
from pygame.locals import *
import constants
import levels

from player import Player
from enemy import Mob
from enemy2 import Mob_2
from enemy3 import Mob_3

from spritesheet_functions import SpriteSheet


def main():
	pygame.init()
	
	#set the height and width of the screen
	size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Pygame Platform")
	
	player = Player()
	mob = Mob()
	mob2 = Mob_2()
	mob3 = Mob_3()
	
	
	#Levels of the game
	level_list = []
	#level_list.append(levels.Level_01(player))
	#level_list.append(levels.Level_02(player))
	#level_list.append(levels.Level_03(player))
	#level_list.append(levels.Level_04(player))
	#level_list.append(levels.Level_05(player))
	level_list.append(levels.Level_06(player))
	
	
	#set the current level
	current_level_no = 0
	current_level = level_list[current_level_no]
	
	active_sprite_list = pygame.sprite.Group()
	a_list = pygame.sprite.Group()
	player.level = current_level
	
	
	player.rect.x = 340
	player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)
	#add enemies
	a_list.add(Mob())
	a_list.add(Mob_2())
	a_list.add(Mob_3())
	
	
	
	#loop until user clicks button
	done = False
	
	#How fast screen updates
	clock = pygame.time.Clock()
	

	
	while not done: 
		for event in pygame.event.get(): # user performed action
			if event.type == pygame.QUIT: # if user quits
				done = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
				if event.key == pygame.K_a:
					player.go_left()
				if event.key == pygame.K_d:
					player.go_right()
				if event.key == pygame.K_w:
					player.jump()
				if event.key == pygame.K_DOWN:
					player.fall()
				if event.key == pygame.K_s:
					player.fall()
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()				
				if event.key == pygame.K_a and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_d and player.change_x > 0:
					player.stop()				
			
		#update player
		active_sprite_list.update()
		a_list.update()
		
		#update item in the level
		current_level.update()
		
		
		
		#if right, shift player left
		if player.rect.right >=500:
			diff = player.rect.right - 500
			player.rect.right = 500
			current_level.shift_world(-diff)
			
		#if left, shift player to right
		if player.rect.left <=120:
			diff = 120- player.rect.left 
			player.rect.left = 120
			current_level.shift_world(diff)
			
		#once player reaches end of level, move onto the next one.
		current_position = player.rect.x + current_level.world_shift
		if current_position < current_level.level_limit:
			player.rect.x = 120
			if current_level_no < len(level_list)-1:
				current_level_no +=1
				current_level = level_list[current_level_no]
				player.level = current_level
			else: #Else, the player wins!
				screen.fill((0,204,255))	
				#load image of winner & text
				image = pygame.image.load("Enemies/frame-4.png")
				image = pygame.transform.scale(image, (381,250))
				y = image.get_rect(center = (350,150))
				screen.blit(image, y)
				myfont = pygame.font.SysFont('Comic Sans MS', 52)
				surface = myfont.render("Congragulations! You win!", True,  (255,255,255))
				text_rect = surface.get_rect(center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
				screen.blit(surface, text_rect)
				#wait until user quits
				pygame.display.flip()
				waiting = True
				while waiting:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							waiting = False
							pygame.display.quit()
		#If collision with between player and enemies
		if pygame.sprite.spritecollide(player, a_list, False, pygame.sprite.collide_mask):
				#Add animation to the game_over screen
					
			screen.fill((0,0,0))
			#load game-over image & add text & restart button
			image = pygame.image.load("Enemies/frame-3.png").convert()
			image = pygame.transform.scale(image, (381,250))
			y = image.get_rect(center = (350,150))
			screen.blit(image, y)
			myfont = pygame.font.SysFont('Comic Sans MS', 52)
			surface = myfont.render("Game Over! ", True,  (255,51,0))
			text_rect = surface.get_rect(center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
			screen.blit(surface, text_rect)
			x1 = myfont.render("Press 'R' to restart", True, (255,255,255))
			x2 = x1.get_rect(center = (400, 400))
			screen.blit(x1, x2)
			
			pygame.display.flip()
			waiting = True
			while waiting:
				
			# if r is clicked, then the game will restart
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key ==pygame.K_r:
							main()
					elif event.type == pygame.QUIT:
						waiting = False
			
			pygame.display.quit()


			
		#Draw active players, enemies, and level
		current_level.draw(screen)
		active_sprite_list.draw(screen)
		a_list.draw(screen)
		
		
		#80 frames per second
		clock.tick(60)
		
		pygame.display.flip()
		
	pygame.quit()
if __name__ == "__main__":
	main()
					
	
