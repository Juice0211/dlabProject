import pygame

steve_hand = pygame.Rect(594, 378, 50, 50)
hand_wood_image = pygame.image.load("image/hand_wood.png")
hand_wood_image = pygame.transform.scale(hand_wood_image, (steve_hand.w, steve_hand.h))
hand_wood_image_45 = pygame.transform.rotate(hand_wood_image, 135)
hand_wood_image_90 = pygame.transform.rotate(hand_wood_image, 90)
hand_wood_image_135 = pygame.transform.rotate(hand_wood_image, 45)
hand_wood_image_flip = pygame.transform.flip(hand_wood_image, True, False)
hand_wood_image_45_flip = pygame.transform.flip(hand_wood_image_45, True, False)
hand_wood_image_90_flip = pygame.transform.flip(hand_wood_image_90, True, False)
hand_wood_image_135_flip = pygame.transform.flip(hand_wood_image_135, True, False)

hand_stone_image = pygame.image.load("image/hand_stone.png")
hand_stone_image = pygame.transform.scale(hand_stone_image, (steve_hand.w, steve_hand.h))
hand_stone_image_45 = pygame.transform.rotate(hand_stone_image, 135)
hand_stone_image_90 = pygame.transform.rotate(hand_stone_image, 90)
hand_stone_image_135 = pygame.transform.rotate(hand_stone_image, 45)
hand_stone_image_flip = pygame.transform.flip(hand_stone_image, True, False)
hand_stone_image_45_flip = pygame.transform.flip(hand_stone_image_45, True, False)
hand_stone_image_90_flip = pygame.transform.flip(hand_stone_image_90, True, False)
hand_stone_image_135_flip = pygame.transform.flip(hand_stone_image_135, True, False)

hand_iron_image = pygame.image.load("image/hand_iron.png")
hand_iron_image = pygame.transform.scale(hand_iron_image, (steve_hand.w, steve_hand.h))
hand_iron_image_45 = pygame.transform.rotate(hand_iron_image, 135)
hand_iron_image_90 = pygame.transform.rotate(hand_iron_image, 90)
hand_iron_image_135 = pygame.transform.rotate(hand_iron_image, 45)
hand_iron_image_flip = pygame.transform.flip(hand_iron_image, True, False)
hand_iron_image_45_flip = pygame.transform.flip(hand_iron_image_45, True, False)
hand_iron_image_90_flip = pygame.transform.flip(hand_iron_image_90, True, False)
hand_iron_image_135_flip = pygame.transform.flip(hand_iron_image_135, True, False)

hand_dia_image = pygame.image.load("image/hand_dia.png")
hand_dia_image = pygame.transform.scale(hand_dia_image, (steve_hand.w, steve_hand.h))
hand_dia_image_45 = pygame.transform.rotate(hand_dia_image, 135)
hand_dia_image_90 = pygame.transform.rotate(hand_dia_image, 90)
hand_dia_image_135 = pygame.transform.rotate(hand_dia_image, 45)
hand_dia_image_flip = pygame.transform.flip(hand_dia_image, True, False)
hand_dia_image_45_flip = pygame.transform.flip(hand_dia_image_45, True, False)
hand_dia_image_90_flip = pygame.transform.flip(hand_dia_image_90, True, False)
hand_dia_image_135_flip = pygame.transform.flip(hand_dia_image_135, True, False)

hand_image_list = [hand_wood_image, hand_wood_image_45, hand_wood_image_90, hand_wood_image_135, hand_stone_image, hand_stone_image_45,
				   hand_stone_image_90, hand_stone_image_135, hand_iron_image, hand_iron_image_45, hand_iron_image_90, hand_iron_image_135,
				   hand_dia_image, hand_dia_image_45, hand_dia_image_90, hand_dia_image_135]
hand_image_list_flip = [hand_wood_image_flip, hand_wood_image_45_flip, hand_wood_image_90_flip, hand_wood_image_135_flip, hand_stone_image_flip, hand_stone_image_45_flip,
				   hand_stone_image_90_flip, hand_stone_image_135_flip, hand_iron_image_flip, hand_iron_image_45_flip, hand_iron_image_90_flip, hand_iron_image_135_flip,
				   hand_dia_image_flip, hand_dia_image_45_flip, hand_dia_image_90_flip, hand_dia_image_135_flip]

pickaxe_list = [hand_wood_image, hand_stone_image, hand_iron_image, hand_dia_image]
pickaxe_list_flip = [hand_wood_image_flip, hand_stone_image_flip, hand_iron_image_flip, hand_dia_image_flip]
