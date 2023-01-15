import pygame
import sys
from pygame.locals import *

width = 1200
height = 900

#image setup
pygame.init()
screen = pygame.display.set_mode((width, height))
# x:1은 x24로 정하기 y:1은 y 18
#coal, iron, gold, eme, stone, copper, dia, grass, ice, tnt
class Block():
	def __init__(self):
		self.image = pygame.image.load("%s.png", self)
		self.image = pygame.transform.scale(self.image, 50, 50)
		self.rect = pygame.Rect(0, 0, 50, 50)
	def draw(self):
		screen.blit(self.image, self.rect)





while True:

	clock = pygame.time.Clock()

	keyInput = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((255, 255, 255))
	clock.tick(60)
	pygame.display.update()
