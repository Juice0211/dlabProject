import pygame
import sys
from pygame.locals import *

width = 1200
height = 900

pygame.init()
# x:1은 x24로 정하기 y:1은 y 18

class Block:
	def __init__(self, block_name):
		self.block_name = block_name
		self.rect = pygame.Rect(0, 0, 50, 50)
		self.image = pygame.image.load("%s.png" % self.block_name)
		self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))

	def draw(self):
		screen.blit(self.image, self.rect)



coal = Block('coal')
iron = Block('iron')
grass = Block('grass')
stone = Block('stone')
tnt = Block('tnt')
emerald = Block('emerald')
diamond = Block('diamond')
ice = Block('ice')
block_list = [coal, iron, stone, tnt, emerald, grass, diamond, ice]

steve_hand = pygame.Rect(594, 378, 50, 50)
hand_wood_image = pygame.image.load("hand_wood.png")
hand_wood_image = pygame.transform.scale(hand_wood_image, (steve_hand.w, steve_hand.h))
hand_wood_image_45 = pygame.transform.rotate(hand_wood_image, 135)
hand_wood_image_90 = pygame.transform.rotate(hand_wood_image, 90)
hand_wood_image_135 = pygame.transform.rotate(hand_wood_image, 45)
# hand_wood_image_flip = pygame.transform.flip(hand_wood_image, True, False)
# hand_wood_image_45_flip = pygame.transform.flip(hand_wood_image_45, True, False)
# hand_wood_image_90_flip = pygame.transform.flip(hand_wood_image_90, True, False)
# hand_wood_image_135_flip = pygame.transform.flip(hand_wood_image_135, True, False)

hand_stone_image = pygame.image.load("hand_stone.png")
hand_stone_image = pygame.transform.scale(hand_stone_image, (steve_hand.w, steve_hand.h))
hand_stone_image_45 = pygame.transform.rotate(hand_stone_image, 135)
hand_stone_image_90 = pygame.transform.rotate(hand_stone_image, 90)
hand_stone_image_135 = pygame.transform.rotate(hand_stone_image, 45)
# hand_stone_image_flip = pygame.transform.flip(hand_stone_image, True, False)
# hand_stone_image_45_flip = pygame.transform.flip(hand_stone_image_45, True, False)
# hand_stone_image_90_flip = pygame.transform.flip(hand_stone_image_90, True, False)
# hand_stone_image_135_flip = pygame.transform.flip(hand_stone_image_135, True, False)

hand_iron_image = pygame.image.load("hand_iron.png")
hand_iron_image = pygame.transform.scale(hand_iron_image, (steve_hand.w, steve_hand.h))
hand_iron_image_45 = pygame.transform.rotate(hand_iron_image, 135)
hand_iron_image_90 = pygame.transform.rotate(hand_iron_image, 90)
hand_iron_image_135 = pygame.transform.rotate(hand_iron_image, 45)
# hand_iron_image_flip = pygame.transform.flip(hand_iron_image, True, False)
# hand_iron_image_45_flip = pygame.transform.flip(hand_iron_image_45, True, False)
# hand_iron_image_90_flip = pygame.transform.flip(hand_iron_image_90, True, False)
# hand_iron_image_135_flip = pygame.transform.flip(hand_iron_image_135, True, False)

hand_dia_image = pygame.image.load("hand_dia.png")
hand_dia_image = pygame.transform.scale(hand_dia_image, (steve_hand.w, steve_hand.h))
hand_dia_image_45 = pygame.transform.rotate(hand_dia_image, 135)
hand_dia_image_90 = pygame.transform.rotate(hand_dia_image, 90)
hand_dia_image_135 = pygame.transform.rotate(hand_dia_image, 45)
# hand_dia_image_flip = pygame.transform.flip(hand_dia_image, True, False)
# hand_dia_image_45_flip = pygame.transform.flip(hand_dia_image_45, True, False)
# hand_dia_image_90_flip = pygame.transform.flip(hand_dia_image_90, True, False)
# hand_dia_image_135_flip = pygame.transform.flip(hand_dia_image_135, True, False)
# 리스트에 넣어서 for i in range를 이용하여 인덱싱으로 맞춘다.
steve_hand_image = hand_wood_image

steve = pygame.Rect(600, 450, 24, 100)
steve_image = pygame.image.load("steve.png")
steve_image = pygame.transform.scale(steve_image, (steve.w, steve.h))
# steve_image_flip = pygame.transform.flip(steve_image, True, False)
steve.centerx = 600
steve.bottom = 450
# steve_image_now = steve_image



screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

Open_store = False
Open_inventory = False

if steve_hand_image == hand_wood_image_45 or steve_hand_image == hand_stone_image_45 or steve_hand_image == hand_iron_image_45 or steve_hand_image == hand_dia_image_45:
	steve_hand.left = 568
	steve_hand.top = 318

if steve_hand_image == hand_wood_image_90 or steve_hand_image == hand_stone_image_90 or steve_hand_image == hand_iron_image_90 or steve_hand_image == hand_dia_image_90:
	steve_hand.left = 595
	steve_hand.top = 338

if steve_hand_image == hand_wood_image_135 or steve_hand_image == hand_stone_image_135 or steve_hand_image == hand_iron_image_135 or steve_hand_image == hand_dia_image_135:
	steve_hand.left = 594
	steve_hand.top = 348

# if steve_hand_image == hand_wood_image_flip or steve_hand_image == hand_stone_image_flip or steve_hand_image == hand_iron_image_flip or steve_hand_image == hand_dia_image_flip:
# 	steve_hand.left = 606
# 	steve_hand.top = 375
#
# if steve_hand_image == hand_wood_image_45_flip or steve_hand_image == hand_stone_image_45_flip or steve_hand_image == hand_iron_image_45_flip or steve_hand_image == hand_dia_image_45_flip:
# 	steve_hand.left = 568
# 	steve_hand.top = 318
#
# if steve_hand_image == hand_wood_image_90_flip or steve_hand_image == hand_stone_image_90_flip or steve_hand_image == hand_iron_image_90_flip or steve_hand_image == hand_dia_image_90_flip:
# 	steve_hand.left = 595
# 	steve_hand.top = 338
#
# if steve_hand_image == hand_wood_image_135_flip or steve_hand_image == hand_stone_image_135_flip or steve_hand_image == hand_iron_image_135_flip or steve_hand_image == hand_dia_image_135_flip:
# 	steve_hand.left = 594
# 	steve_hand.top = 348

while True:

	keyInput = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if keyInput[K_a] and steve.left >= 50:
		steve.centerx -= 5
		steve_hand.left -= 5
		# steve_image_now = steve_image_flip

	if keyInput[K_d] and steve.right <= 1150:
		steve.centerx += 5
		steve_hand.right += 5
		# steve_image_now = steve_image

	screen.fill((255, 255, 255))
	clock.tick(60)
	if Open_store == False and Open_inventory == False:
		for i in block_list:
			i.draw()
		# screen.blit(steve_image_now, steve)
		screen.blit(steve_image, steve)
		screen.blit(steve_hand_image, steve_hand)
	pygame.display.update()
