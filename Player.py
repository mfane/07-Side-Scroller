#!/usr/bin/python
import pygame, logging, os
from Color import Color

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
img_size = (47, 56)
img_margin = (70, 60)


class Player(pygame.sprite.Sprite):
	def __init__(self,position,lives,size,gravity,friction):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(os.path.join('.', 'Green-Cap-Character-Classic-Hero-Edit.png')).convert()
		(self.width, self.height) = img_size
		(self.margin_x, self.margin_y) = img_margin
		self.rect = pygame.Rect((self.margin_x, self.margin_y, self.width, self.height))
		self.image = pygame.Surface(self.rect.size).convert()
		self.image.blit(self.sheet, (0, 0), self.rect)
		(self.rect.x,self.rect.y) = position
		self.starting_position = position

		(self.dx,self.dy) = (0,0)
		self.ramp_up = 1
		self.max_dx = 10

		self.jump_force = 40
		self.gravity = gravity
		self.friction = friction
		
		self.on_ground = False
		
		self.lives = lives

		self.timer = 0
	
	def get_position(self):
		return (self.rect.x,self.rect.y)
	
	def move(self,direction):
		if abs(self.dx + (direction * self.ramp_up)) <= self.max_dx:
			self.dx += direction * self.ramp_up


	def jump(self):
		if self.on_ground:
			self.dy -= self.jump_force
			self.on_ground = False
		
	def die(self,level, enemies):
		self.lives -= 1
		(self.rect.x,self.rect.y) = self.starting_position
		(self.dx,self.dy) = (0,0)
		level.screen_shake = True
		for e in enemies:
			(e.rect.x, e.rect.y) = e.starting_position
	
	def update(self,level,enemies,floors):
		self.rect.x += self.dx
		self.rect.y += self.dy
		if self.dx > 0:
			self.dx -= self.friction
			self.dx = max(self.dx,0)
			if self.timer < 8:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x, self.margin_y + 60, self.width, self.height))
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 16:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 65, self.margin_y + 60, self.width, self.height))
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 24:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 125, self.margin_y + 60, self.width, self.height))
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 32:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 185, self.margin_y + 60, self.width, self.height))
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 39:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 250, self.margin_y + 60, self.width, self.height))
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			else:
				self.timer = 0



		elif self.dx < 0:
			self.dx += self.friction
			self.dx = min(self.dx,0)
			if self.timer < 8:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 305, self.margin_y + 60, self.width, self.height))
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 16:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 243, self.margin_y + 60, self.width, self.height))
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 24:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 178, self.margin_y + 60, self.width, self.height))
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 32:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 118, self.margin_y + 60, self.width, self.height))
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			elif self.timer < 39:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 58, self.margin_y + 60, self.width, self.height))
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
				self.timer += 1
			else:
				self.timer = 0
		else:
			position = (self.rect.x, self.rect.y)
			self.rect = pygame.Rect((self.margin_x, self.margin_y, self.width, self.height))
			self.image = pygame.Surface(self.rect.size).convert()
			self.image.blit(self.sheet, (0, 0), self.rect)
			(self.rect.x, self.rect.y) = position
			self.timer = 0
			
		if not self.on_ground:
			self.dy += self.gravity
			if self.dx > 0:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x, self.margin_y + 120, self.width, self.height))
				self.image = pygame.Surface(self.rect.size).convert()
				self.image.blit(self.sheet, (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
			else:
				position = (self.rect.x, self.rect.y)
				self.rect = pygame.Rect((self.margin_x + 305, self.margin_y + 120, self.width, self.height))
				self.image = pygame.Surface(self.rect.size).convert()
				self.image.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), self.rect)
				(self.rect.x, self.rect.y) = position
		else:
			self.dy = 0
			
		if self.rect.x <= 0:
			self.rect.x = 0
			self.dx = 0
		if self.rect.right >= level.rect.right:
			self.rect.right = level.rect.right
			self.dx = 0
		self.on_ground = False
		
		self.mask = pygame.mask.from_surface(self.image)
		(pl,pr,pt,pb,pcx,pcy) = (self.rect.left,self.rect.right,self.rect.top,self.rect.bottom,self.rect.centerx,self.rect.centery)
		
		for f in floors:
			margin = float(f.rect.height) / 4
			(fl,fr,ft,fb,fcx,fcy) = (f.rect.left,f.rect.right,f.rect.top,f.rect.bottom,f.rect.centerx,f.rect.centery)
			if pb == ft and ((pl >= fl and pl <= fr) or (pr >= fl and pr <= fr)):
				self.on_ground = True
				self.dy = 0
			else: 
				collision = pygame.sprite.collide_rect(self, f)
				if collision:
					if pr <= fl + margin and ((pt >= ft and pt <= fb) or (pb >= ft and pb <= ft)):
						self.rect.right = fl - 1
						self.dx *= -0.25
					elif pl >= fr - margin and ((pt >= ft and pt <= fb) or (pb >= ft and pb <= ft)):
						self.rect.left = fr + 1
						self.dx *= -0.25
					elif pb <= ft + margin and ((pl >= fl and pl <= fr) or (pr >= fl and pr <= fr)):
						self.rect.bottom = ft
						self.dy = 0
						self.on_ground = True
					elif pt >= fb - margin and ((pl >= fl and pl <= fr) or (pr >= fl and pr <= fr)):
						self.rect.top = fb + 1
						self.dy = 0
		if self.rect.top >= level.rect.bottom:
			self.die(level, enemies)
		for e in enemies:
			collision = pygame.sprite.collide_rect(self,e)
			if collision:
				self.die(level, enemies)
