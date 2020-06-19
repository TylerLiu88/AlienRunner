import pygame
import constants
def game_over():
	"""Display game over sign"""
	if done == True:
		return
		self.screen.fill(BGCOLOR)
		self.draw_text("Game Over", 48, WHITE, constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
	pygame.display.flip()
	wait_for_key()
	
def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False

                if event.type == pg.KEYUP:
                    waiting = False
