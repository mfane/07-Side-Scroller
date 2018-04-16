#!/usr/bin/python
import pygame,os
from Color import Color

class Enemy(pygame.sprite.Sprite):
	def __init__(self,gravity,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('.', "green_little_bug.png")).convert()
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1] - 25
		self.gravity = gravity
		(self.rect.x, self.rect.y) = position
		self.starting_position = position
	
	def get_position(self):
		return (self.rect.x,self.rect.y)
	
	def update(self):
		'''
		update behavior
		'''
		self.rect.x -= 10