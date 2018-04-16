#!/usr/bin/python

import sys, logging, pygame, random, os
from Color import Color
from Sound import Sound 
from Player import Player
from Enemy import Enemy
from Level import Level, Floor
from itertools import repeat
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
gravity = 2
friction = 0.3
lives = 10

class GameOver(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('.', 'skull.png')).convert()
		self.rect = self.image.get_rect()
		self.rect.x = 330
		self.rect.y = 250


def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	screen_rect = screen.get_rect()
	clock = pygame.time.Clock()

	offset = repeat((0, 0))

	sound = Sound()
	'''
	Add whatever soundtrack files you want to the mp3 folder, and then add them to the soundtrack by calling

	sound.add_music('Ambient_Blues_Joe_ID_773.mp3') # replace with whatever the filename is

	Once you have added the tracks you want, just call

	sound.play_music()

	When the song finishes, the library will queue up and play the next one in the order you added them

	---------------------------------

	You can add sounds to the sound library by calling

	sound.add_sound('footstep','footstep_sound.mp3')

	It assumes the sounds are in the mp3 folder
	To play sounds in the library, you can call

	sound.play_sound('footstep')
	'''

	sound.add_music('Brazzmatazz_-_10_-_Mezcal_Y_Sangrita.mp3')
	sound.add_music('Brazzmatazz_-_07_-_Tiny_Tiger.mp3')
	sound.play_music()

	level = Level('level_1.game') #a game level definition
	players = pygame.sprite.Group()
	player = Player(level.get_player_starting_position(),lives,level.block_size,gravity,friction)
	players.add(player)
	enemies = pygame.sprite.Group()
	for e in level.get_enemies():
		enemy = Enemy(gravity,e,level.block_size)
		enemies.add(enemy)
	floors = pygame.sprite.Group()
	for f in level.get_floor():
		floor = Floor(gravity,f,level.block_size)
		floors.add(floor)
		

	while True:
		clock.tick(FPS)
		screen.fill(Color.black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

		if player.rect.right >= level.rect.right:
			screen.fill(Color.blue_5)
			font = pygame.font.SysFont("arial", 64)
			f = font.render('YOU WIN', True, Color.yellow_0)
			screen.blit(f, (230, 400))
			pygame.display.flip()

		elif player.lives > 0:
			if event.type == sound.event():
				sound.play_music()

			keys = pygame.key.get_pressed()
			# a complete list of the pygame key constants can be found here: https://www.pygame.org/docs/ref/key.html
			if keys[pygame.K_RIGHT]:
				player.move(1)
			if keys[pygame.K_LEFT]:
				player.move(-1)
			if keys[pygame.K_UP]:
				player.jump()
			if keys[pygame.K_SPACE]:
				player.jump()

			floors.update()
			enemies.update()
			players.update(level,enemies,floors)

			full_screen = level.get_full_screen()
			floors.draw(full_screen)
			enemies.draw(full_screen)
			players.draw(full_screen)
		
			if level.screen_shake:
				offset = level.shake()
				level.screen_shake = False
		
			screen.blit(level.get_screen(),next(offset),level.get_rect(screen_size,player))
			pygame.display.flip()
		else:
			screen.fill(Color.black)
			font = pygame.font.SysFont("arial", 64)
			g = pygame.sprite.Group()
			skull = GameOver()
			g.add(skull)
			g.draw(screen)
			f = font.render('GAME OVER', True, Color.white)
			screen.blit(f, (230, 400))
			pygame.display.flip()


if __name__ == '__main__':
	main()