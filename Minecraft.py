import sys
from pygame.locals import *
from hand import *
import math
from random import *

width = 1200
height = 900
jumping = False
colliding = list()
colliding_bool = False
colliding_check = 0

pygame.init()
# x:1은 x24로 정하기 y:1은 y 18
# wood: 3s stone:2s iron:1s diamond:0.5s
'''
해야할 것:
밑에 블럭이 없으면 내려가는거
상점 ... 그냥 돌 몇개 쌓이면 자동으로 바뀌는것도 나쁘지 않을지도(이미지 또 넣기 싫은데)
점프 -> 위로 올라가짐
점프 시스템 개편 -> 2중 점프 가능
조금이라도 닿을시 아예 못움직이는 현상 개편
블럭 뒤도 캐지는거 개편?
'''
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Minecraft")
clock = pygame.time.Clock()

spawn_ore_data = list()

for i in range(1150):
	spawn_ore_data.append('stone')
for i in range(140):
	spawn_ore_data[randint(0, 1149)] = 'coal'
for i in range(150):
	j = randint(216, 1149)
	if spawn_ore_data[j] == 'stone':
		spawn_ore_data[j] = 'iron'
	else:
		j = randint(216, 1149)
		if spawn_ore_data[j] == 'stone':
			spawn_ore_data[j] = 'iron'
for i in range(130):
	j = randint(216, 1149)
	if spawn_ore_data[j] == 'stone':
		spawn_ore_data[j] = 'ice'
	else:
		j = randint(216, 1149)
		if spawn_ore_data[j] == 'stone':
			spawn_ore_data[j] = 'ice'
for i in range(30):
	j = randint(696, 1149)
	if spawn_ore_data[j] == 'stone':
		spawn_ore_data[j] = 'emerald'
	else:
		j = randint(696, 1149)
		if spawn_ore_data[j] == 'stone':
			spawn_ore_data[j] = 'emerald'
for i in range(40):
	j = randint(216, 1149)
	if spawn_ore_data[j] == 'stone':
		spawn_ore_data[j] = 'tnt'
	else:
		j = randint(216, 1149)
		if spawn_ore_data[j] == 'stone':
			spawn_ore_data[j] = 'tnt'
for i in range(20):
	j = randint(912, 1149)
	if spawn_ore_data[j] == 'stone':
		spawn_ore_data[j] = 'diamond'
	else:
		j = randint(912, 1149)
		if spawn_ore_data[j] == 'stone':
			spawn_ore_data[j] = 'diamond'

for i in range(1274):
	colliding.append('False')

steve = pygame.Rect(600, 450, 24, 100)
steve_image = pygame.image.load("image/steve.png")
steve_image = pygame.transform.scale(steve_image, (steve.w, steve.h))
steve_image_flip = pygame.transform.flip(steve_image, True, False)
steve.centerx = 600
steve.bottom = 450
steve_image_now = steve_image


class Block:
	def __init__(self, block_name, number):
		self.steve_on_me = False
		self.isjump = 0
		self.number = int(number)
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
		if not self.hide and self.border and not self.block_name == 'bedrock':
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
			self.x = self.number - 1200
		if self.block_name == 'bedrock':
			self.y = 1
			self.x = self.number - 1250
		for n in range(1150):
			if spawn_ore_data[n] == self.block_name:
				n_x = n % 24
				self.x = 23 - n_x
				n_y = math.trunc(n / 24)
				self.y = 49 - n_y
				spawn_ore_data[n] = 'Done'
				break
		if self.x == 0 and self.y == 0:
			self.x = 100
			self.y = 100

	def set_x(self):
		self.rect.x = self.x * 50

	def set_y(self):
		self.rect.y = 2950 - (50 * self.y)

	def jump(self, jump):
		self.isjump = jump

	def check_jump(self):
		if self.isjump > 0:
			self.y -= 1
			self.isjump = 0
		if self.isjump == -1:
			self.y += 1
			self.isjump = 0

	def check_steve(self):
		global colliding
		if steve_image_now == steve_image:
			if self.rect.collidepoint((steve.right, steve.top + 10)) and not self.hide:
				colliding[self.number] = 'True'
			elif self.rect.collidepoint((steve.right, steve.bottom - 10)) and not self.hide:
				colliding[self.number] = 'True'
			else:
				colliding[self.number] = 'False'
		elif steve_image_now == steve_image_flip:
			if self.rect.collidepoint((steve.left, steve.top + 10)) and not self.hide:
				colliding[self.number] = 'True'
			elif self.rect.collidepoint((steve.left, steve.bottom - 10)) and not self.hide:
				colliding[self.number] = 'True'
			else:
				colliding[self.number] = 'False'


coal_list = list()
iron_list = list()
grass_list = list()
ice_list = list()
stone_list = list()
tnt_list = list()
emerald_list = list()
diamond_list = list()
bedrock_list = list()
for i in range(1, 1201):
	if 1 <= i <= 150:
		iron = Block('iron', i)
		iron_list.append(iron)
	elif 151 <= i <= 280:
		ice = Block('ice', i)
		ice_list.append(ice)
	elif 281 <= i <= 420:
		coal = Block('coal', i)
		coal_list.append(coal)
	elif 421 <= i <= 450:
		emerald = Block('emerald', i)
		emerald_list.append(emerald)
	elif 451 <= i <= 470:
		diamond = Block('diamond', i)
		diamond_list.append(diamond)
	elif 471 <= i <= 510:
		tnt = Block('tnt', i)
		tnt_list.append(tnt)
	elif 511 <= i:
		stone = Block('stone', i)
		stone_list.append(stone)
for i in range(24):
	grass = Block('grass', i+1200)
	grass_list.append(grass)
for i in range(24):
	bedrock = Block('bedrock', i+1250)
	bedrock_list.append(bedrock)

block_list = [coal_list, iron_list, emerald_list, diamond_list, ice_list, tnt_list, stone_list, grass_list, bedrock_list]
#coal iron eme dia ice tnt stone
for i in block_list:
	for j in i:
		j.set_block_xy()


# 리스트에 넣어서 for i in range를 이용하여 인덱싱으로 맞춘다.
steve_hand_image = hand_wood_image

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
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				for j in block_list:
					for i in j:
						if i.isjump == 0:
							i.jump(1)
						if i.isjump == 1:
							i.jump(2)
		if event.type == KEYUP:
			if event.key == K_SPACE:
				for j in block_list:
					for i in j:
						if i.isjump == 0:
							i.jump(-1)
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
							pygame.time.wait(666)
							steve_hand_image = hand_stone_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(666)
							steve_hand_image = hand_stone_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(668)
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
							pygame.time.wait(333)
							steve_hand_image = hand_iron_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(333)
							steve_hand_image = hand_iron_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(334)
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
							pygame.time.wait(166)
							steve_hand_image = hand_dia_image_90
							steve_hand.left += 26
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(166)
							steve_hand_image = hand_dia_image_135
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(167)
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
							pygame.time.wait(666)
							steve_hand_image = hand_stone_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(666)
							steve_hand_image = hand_stone_image_135_flip
							steve_hand.left -= 21
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(668)
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
							pygame.time.wait(333)
							steve_hand_image = hand_iron_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(333)
							steve_hand_image = hand_iron_image_135_flip
							steve_hand.left -= 21
							steve_hand.top += 10
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(334)
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
							pygame.time.wait(166)
							steve_hand_image = hand_dia_image_90_flip
							steve_hand.left -= 6
							steve_hand.top += 20
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(166)
							steve_hand_image = hand_dia_image_135_flip
							steve_hand.top += 10
							steve_hand.left -= 21
							screen.blit(steve_hand_image, steve_hand)
							pygame.display.update()
							pygame.time.wait(167)
							steve_hand_image = hand_dia_image_flip
							steve_hand.top += 30
							steve_hand.left += 21
							i.hide = True
							event = None
						else:
							break
	colliding_check = 0
	for i in range(1274):
		if colliding[i] == 'True':
			colliding_bool = True
		if colliding[i] == 'False':
			colliding_check += 1
		if colliding_check == 1274:
			colliding_bool = False
	if keyInput[K_a] and steve.left >= 0 and not colliding_bool:
		steve.centerx -= 5
		steve_hand.left -= 5
		steve_image_now = steve_image_flip
		for i in hand_image_list:
			if steve_hand_image == hand_image_list[hand_image_list.index(i)]:
				steve_hand_image = hand_image_list_flip[hand_image_list.index(i)]
				steve_hand.right = steve_hand.left + 12

	if keyInput[K_d] and steve.right <= 1200 and not colliding_bool:
		steve.centerx += 5
		steve_hand.right += 5
		steve_image_now = steve_image
		for i in hand_image_list_flip:
			if steve_hand_image == hand_image_list_flip[hand_image_list_flip.index(i)]:
				steve_hand_image = hand_image_list[hand_image_list_flip.index(i)]
				steve_hand.left = steve_hand.right -12

	if keyInput[K_h]:
		for j in block_list:
			for i in j:
				i.y += 1
	if keyInput[K_j]:
		for j in block_list:
			for i in j:
				i.y -= 1

	screen.fill((255, 255, 255))
	clock.tick(60)
	if not Open_store:
		for j in block_list:
			for i in j:
				i.check_steve()
				i.check_jump()
				i.set_x()
				i.set_y()
				i.draw()
				i.set_border()
		screen.blit(steve_image_now, steve)
		screen.blit(steve_hand_image, steve_hand)
	pygame.display.update()
