import sys
from pygame.locals import *
from hand import *
import math
from random import *

width = 1200
height = 900

pygame.init()
# x:1은 x24로 정하기 y:1은 y 18
# wood: 3s stone:2s iron:1s diamond:0.5s
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dia_num_x = list()
dia_num_y = list()
iron_num_x = list()
iron_num_y = list()
coal_num_x = list()
coal_num_y = list()
ice_num_x = list()
ice_num_y = list()
eme_num_x = list()
eme_num_y = list()
tnt_num_x = list()
tnt_num_y = list()
list_50 = list()
list_24 = list()
list_40 = list()
list_30 = list()
list_20 = list()
list_11 = list()
stone_num_x = list()
stone_num_y = list()

for i in range(50):
	list_50.append(i)
for i in range(24):
	list_24.append(i)
for i in range(40):
	list_40.append(i)
for i in range(30):
	list_30.append(i)
for i in range(20):
	list_20.append(i)
for i in range(11):
	list_11.append(i)
for i in range(20):
	dia_num_x.append(choice(list_24))
	dia_num_y.append(choice(list_11))
for i in range(140):
	coal_num_x.append(choice(list_24))
	coal_num_y.append(choice(list_50))
for i in range(150):
	iron_num_x.append(choice(list_24))
	iron_num_y.append(choice(list_40))
for i in range(130):
	ice_num_x.append(choice(list_24))
	ice_num_y.append(choice(list_40))
for i in range(30):
	eme_num_x.append(choice(list_24))
	eme_num_y.append(choice(list_20))
for i in range(40):
	tnt_num_x.append(choice(list_24))
	tnt_num_y.append(choice(list_40))
for i in range(50):
	for j in range(24):
		stone_num_x.append(list_24[j])
for i in range(24):
	for j in range(50):
		stone_num_y.append(list_50[j])

stone_num_x_dummy = dia_num_x + coal_num_x + iron_num_x + ice_num_x + eme_num_x + tnt_num_x
stone_num_y_dummy = dia_num_y + coal_num_y + iron_num_y + ice_num_y + eme_num_y + tnt_num_y
print(stone_num_x_dummy)
print(stone_num_x)
print(len(stone_num_x_dummy))
for i in range(510):
	stone_num_x.remove(stone_num_x_dummy[i])
	stone_num_y.remove(stone_num_y_dummy[i])


class Block:
	def __init__(self, block_name, number):
		self.number = number
		self.distance = 0
		self.x = 0
		self.y = 0
		self.block_name = block_name
		self.rect = pygame.Rect(0, 0, 50, 50)
		self.image = pygame.image.load("image/%s.png" % self.block_name)
		self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))
		self.border_rect = pygame.draw.rect(screen, (0, 0, 0), [self.rect.x, self.rect.y, 50, 50], 2)
		self.hide = False
		self.border = False

	def draw(self):
		if not self.hide:
			screen.blit(self.image, self.rect)

	def check_mouse(self):
		if not self.hide and self.border:
			if steve_image_now == steve_image:
				if self.rect.left >= steve.right:
					self.distance = round(math.sqrt(((steve.centerx -self.rect.centerx) ** 2) + ((steve.top -self.rect.centery) ** 2)))
					if self.distance < 200:
						return True
				else:
					return False
			if steve_image_now == steve_image_flip:
				if self.rect.right <= steve.left:
					self.distance = round(math.sqrt(((steve.centerx - self.rect.centerx) ** 2) + ((steve.top - self.rect.centery) ** 2)))
					if self.distance < 200:
						return True
				else:
					return False

	def set_border(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and self.hide == False:
			self.border_rect = pygame.draw.rect(screen, (0, 0, 0), [self.rect.x, self.rect.y, 50, 50], 2)
			self.border = True
		else:
			self.border_rect = None
			self.border = False

	def set_block_xy(self):
		if self.block_name == 'grass':
			self.y = 50
			self.x = self.number
		elif self.block_name == 'tnt':
			self.y = tnt_num_y[self.number]
			self.x = tnt_num_x[self.number]
		elif self.block_name == 'diamond':
			self.y = dia_num_y[self.number]
			self.x = dia_num_x[self.number]
		elif self.block_name == 'emerald':
			self.y = eme_num_y[self.number]
			self.x = eme_num_x[self.number]
		elif self.block_name == 'iron':
			self.y = iron_num_y[self.number]
			self.x = iron_num_x[self.number]
		elif self.block_name == 'coal':
			self.y = coal_num_y[self.number]
			self.x = coal_num_x[self.number]
		elif self.block_name == 'ice':
			self.y = ice_num_y[self.number]
			self.x = ice_num_x[self.number]
		elif self.block_name == 'stone':
			self.y = stone_num_y[self.number]
			self.x = stone_num_x[self.number]
		else:
			print("Error!%n")
			print("Please remove this program%n")
			print("and download Program again.")
			sys.exit()

	def set_x(self):
		self.rect.x = self.x * 50

	def set_y(self):
		self.rect.y = 2950 - (50 * self.y)


coal_list = list()
iron_list = list()
grass_list = list()
ice_list = list()
stone_list = list()
tnt_list = list()
emerald_list = list()
diamond_list = list()

for i in range(150):
	iron = Block('iron', i)
	iron_list.append(iron)
for i in range(130):
	ice = Block('ice', i)
	ice_list.append(ice)
for i in range(140):
	coal = Block('coal', i)
	coal_list.append(coal)
for i in range(30):
	emerald = Block('emerald', i)
	emerald_list.append(emerald)
for i in range(20):
	diamond = Block('diamond', i)
	diamond_list.append(diamond)
for i in range(40):
	tnt = Block('tnt', i)
	tnt_list.append(tnt)
for i in range(24):
	grass = Block('grass', i)
	grass_list.append(grass)
for i in range(666):
	stone = Block('stone', i)
	stone_list.append(stone)


block_list = [coal_list, iron_list, emerald_list, diamond_list, ice_list, tnt_list, stone_list, grass_list]
#coal iron eme dia ice tnt stone
for i in block_list:
	for j in i:
		j.set_block_xy()


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

#0도 594, 378
#45도: -26 -60
#90도: +0 -40
# 135도: +0 -30
#flip:
#0도: +12: 606, 378
#45도: -38 -60
#90도: + 0 -40
#135도: +0 -30
while True:

	keyInput = pygame.key.get_pressed()
	mouseInput = pygame.mouse.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			for j in block_list:
				for i in j:
					if i.check_mouse():
						if steve_hand_image == hand_wood_image:
							steve_hand_image = hand_wood_image_45
							steve_hand.left -= 26
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image
							steve_hand.top += 30
							i.hide = True
							event = None
						elif steve_hand_image == hand_stone_image:
							steve_hand_image = hand_stone_image_45
							steve_hand.left -= 26
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image
							steve_hand.top += 30
							i.hide = True
							event = None
						elif steve_hand_image == hand_iron_image:
							steve_hand_image = hand_iron_image_45
							steve_hand.left -= 26
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image
							steve_hand.top += 30
							i.hide = True
							event = None
						elif steve_hand_image == hand_dia_image:
							steve_hand_image = hand_dia_image_45
							steve_hand.left -= 26
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image
							steve_hand.top += 30
							i.hide = True
							event = None
						if steve_hand_image == hand_wood_image_flip:
							steve_hand_image = hand_wood_image_45_flip
							steve_hand.left += 6
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image_135_flip
							steve_hand.left -= 21
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_wood_image_flip
							steve_hand.top += 30
							steve_hand.left += 21
							i.hide = True
							event = None
						elif steve_hand_image == hand_stone_image_flip:
							steve_hand_image = hand_stone_image_45_flip
							steve_hand.left +=6
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image_135_flip
							steve_hand.left -= 21
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_stone_image_flip
							steve_hand.left += 21
							steve_hand.top += 30
							i.hide = True
							event = None
						elif steve_hand_image == hand_iron_image_flip:
							steve_hand_image = hand_iron_image_45_flip
							steve_hand.left += 6
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image_135_flip
							steve_hand.left -= 21
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_iron_image_flip
							steve_hand.left += 21
							steve_hand.top += 30
							i.hide = True
							event = None
						elif steve_hand_image == hand_dia_image_flip:
							steve_hand_image = hand_dia_image_45_flip
							steve_hand.left += 6
							steve_hand.top -=60
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image_135_flip
							steve_hand.top += 10
							steve_hand.left -= 21
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(1000)
							steve_hand_image = hand_dia_image_flip
							steve_hand.top += 30
							steve_hand.left += 21
							i.hide = True
							event = None
						else:
							break

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
		for j in block_list:
			for i in j:
				i.set_x()
				i.set_y()
				i.draw()
				i.set_border()
		screen.blit(steve_image_now, steve)
		screen.blit(steve_hand_image, steve_hand)

	pygame.display.update()
