import pygame, sys, random as r
from Platform import Platform

from Slime import Slime

pygame.init()

ekran_res = [500,900]

ekran = pygame.display.set_mode(ekran_res)
clock = pygame.time.Clock()
# CODE +++++++++++++++++++++++++++++++++++++++++++++++++ 1
slime = Slime(ekran,ekran_res)
platform_list = []

platformID = 1
while platformID <= 100:
    platform_list.append(Platform(ekran, ekran_res, r.randint(0,370), 800 - (80 * platformID)))
    platformID += 1

left = False
right = False

kamera_vel = 0

platform_hareket = False





# CODE +++++++++++++++++++++++++++++++++++++++++++++++++ 1
run = True
while run:
    ekran.fill((50,50,50))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                slime.left = True
            if e.key == pygame.K_RIGHT:
                slime.right = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                slime.left = False
            if e.key == pygame.K_RIGHT:
                slime.right = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if not slime.is_jump:
            slime.is_jump = True
            jump_boost = 1
            if abs(slime.x_vel) >= 8:
                jump_boost = 2
            elif abs(slime.x_vel) > 3:
                jump_boost = 1 + abs(slime.x_vel)/15
            slime.gravity_vel = -(slime.jump_vel * jump_boost)
               
    # CODE +++++++++++++++++++++++++++++++++++++++++++++++++ 2
    # KAMERA
    if slime.rect.top < 200:
        kamera_vel += 0.25
    else:
        if kamera_vel > 0:
            kamera_vel -= 0.5
        else:
            kamera_vel = 0
    
    for x in platform_list:
        x.update(kamera_vel)
    
    for x in platform_list:
        if x.rect.y > 900:
            #slime.yer_kaldır = False
            platform_list.remove(x)

    slime.update(platform_list, kamera_vel)






    # CODE +++++++++++++++++++++++++++++++++++++++++++++++++ 2
    pygame.display.update()
    clock.tick(60)
