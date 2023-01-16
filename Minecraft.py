import sys
from pygame.locals import *
from hand import *
import math

width = 1200
height = 900

pygame.init()
# x:1은 x24로 정하기 y:1은 y 18
# wood: 3s stone:2s iron:1s diamond:0.5s
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Block:
	def __init__(self, block_name):
		self.distance = 0
		self.x = 0
		self.y = 0
		self.block_name = block_name
		self.rect = pygame.Rect(0, 0, 50, 50)
		self.image = pygame.image.load("image/%s.png" % self.block_name)
		self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))
		self.border_rect = pygame.draw.rect(screen, (0, 0, 0), [self.rect.x, self.rect.y, 50, 50], 2)
		self.hide = False

	def draw(self):
		if not self.hide:
			screen.blit(self.image, self.rect)

	def check_mouse(self):
		self.distance = round(math.sqrt(((steve.centerx -self.rect.centerx) ** 2) + ((steve.top -self.rect.centery) ** 2)))
		if round(self.distance) < 200:
			return True

	def set_border(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and self.hide == False:
			self.border_rect = pygame.draw.rect(screen, (0, 0, 0), [self.rect.x, self.rect.y, 50, 50], 2)
		else:
			self.border_rect = None

	def y_set_block(self):
		if self.block_name == 'grass':
			self.y = 50
		# elif self.block_name == '':

		else:
			self.y = 0

	def set_x(self):
		self.rect.x = 50

	def set_y(self):
		self.rect.y = 900 - (9 * self.y)


coal = Block('coal')
iron = Block('iron')
grass = Block('grass')
stone = Block('stone')
tnt = Block('tnt')
emerald = Block('emerald')
diamond = Block('diamond')
ice = Block('ice')
block_list = [coal, iron, stone, tnt, emerald, grass, diamond, ice]

for i in block_list:
	i.y_set_block()


# 리스트에 넣어서 for i in range를 이용하여 인덱싱으로 맞춘다.
steve_hand_image = hand_wood_image

steve = pygame.Rect(600, 450, 24, 100)
steve_image = pygame.image.load("image/steve.png")
steve_image = pygame.transform.scale(steve_image, (steve.w, steve.h))
steve_image_flip = pygame.transform.flip(steve_image, True, False)
steve.centerx = 600
steve.bottom = 450
steve_image_now = steve_image

Open_store = False

if steve_hand_image == hand_wood_image_45 or steve_hand_image == hand_stone_image_45 or steve_hand_image == hand_iron_image_45 or steve_hand_image == hand_dia_image_45:
	steve_hand.left = 568
	steve_hand.top = 318

if steve_hand_image == hand_wood_image_90 or steve_hand_image == hand_stone_image_90 or steve_hand_image == hand_iron_image_90 or steve_hand_image == hand_dia_image_90:
	steve_hand.left = 595
	steve_hand.top = 338

if steve_hand_image == hand_wood_image_135 or steve_hand_image == hand_stone_image_135 or steve_hand_image == hand_iron_image_135 or steve_hand_image == hand_dia_image_135:
	steve_hand.left = 594
	steve_hand.top = 348

if steve_hand_image == hand_wood_image_flip or steve_hand_image == hand_stone_image_flip or steve_hand_image == hand_iron_image_flip or steve_hand_image == hand_dia_image_flip:
	steve_hand.left = 606
	steve_hand.top = 375

if steve_hand_image == hand_wood_image_45_flip or steve_hand_image == hand_stone_image_45_flip or steve_hand_image == hand_iron_image_45_flip or steve_hand_image == hand_dia_image_45_flip:
	steve_hand.left = 568
	steve_hand.top = 318

if steve_hand_image == hand_wood_image_90_flip or steve_hand_image == hand_stone_image_90_flip or steve_hand_image == hand_iron_image_90_flip or steve_hand_image == hand_dia_image_90_flip:
	steve_hand.left = 595
	steve_hand.top = 338

if steve_hand_image == hand_wood_image_135_flip or steve_hand_image == hand_stone_image_135_flip or steve_hand_image == hand_iron_image_135_flip or steve_hand_image == hand_dia_image_135_flip:
	steve_hand.left = 594
	steve_hand.top = 348

while True:

	keyInput = pygame.key.get_pressed()
	mouseInput = pygame.mouse.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			for i in block_list:
				if i.check_mouse():
					i.hide = True

	if keyInput[K_a] and steve.left >= 0:
		steve.centerx -= 5
		steve_hand.left -= 5
		steve_image_now = steve_image_flip
		for i in hand_image_list:
			if steve_hand_image == hand_image_list[hand_image_list.index(i)]:
				steve_hand_image = hand_image_list_flip[hand_image_list.index(i)]
				steve_hand.right = steve_hand.left + 12

	if keyInput[K_d] and steve.right <= 1200:
		steve.centerx += 5
		steve_hand.right += 5
		steve_image_now = steve_image
		for i in hand_image_list_flip:
			if steve_hand_image == hand_image_list_flip[hand_image_list_flip.index(i)]:
				steve_hand_image = hand_image_list[hand_image_list_flip.index(i)]
				steve_hand.left = steve_hand.right -12

	screen.fill((255, 255, 255))
	clock.tick(60)
	if not Open_store:
		for i in block_list:
			i.set_x()
			i.set_y()
			i.draw()
			i.set_border()
		screen.blit(steve_image_now, steve)
		screen.blit(steve_hand_image, steve_hand)

	pygame.display.update()
