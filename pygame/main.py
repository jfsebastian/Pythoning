#!/usr/bin/env python

import pygame
import inspect
from pprint import pprint

# If the variable is not changed can be declared in a more general scope
screenSize = (900, 700)
background_position = (0, 0)
screen = pygame.display.set_mode(screenSize)
project_files = "assets/"

player_size = (24, 32)
treasure_size = (28, 24)
enemy_size = (32, 24)

treasure_position = ( screenSize[0] / 2 - treasure_size[0] / 2, treasure_size[1] )
initial_enemy_position = ( screenSize[0] / 2 - treasure_size[0] / 2, screenSize[1] / 2 - treasure_size[1] )
# print vars()
# print globals()

def main():
    pygame.init()
    frame = pygame.time.Clock()

    background_image = pygame.image.load(project_files + "background.png")
    background_image = pygame.transform.scale(background_image, screenSize)

    player_image = pygame.image.load(project_files + "player.png")
    player_image = pygame.transform.scale(player_image, player_size)
    player_image = player_image.convert_alpha()

    treasure_image = pygame.image.load(project_files + "treasure.png")
    treasure_image = pygame.transform.scale(treasure_image, treasure_size)
    treasure_image = treasure_image.convert_alpha()

    enemy_image = pygame.image.load(project_files + "enemy.png")
    enemy_image = pygame.transform.scale(enemy_image, enemy_size)
    enemy_image = enemy_image.convert_alpha()
    enemy_position = initial_enemy_position

    screen.blit(background_image, background_position)
    screen.blit(treasure_image, treasure_position)

    # print pygame.font.get_fonts()
    font = pygame.font.SysFont("notomono", 60, False, False)
    textWin = font.render("It's a Trap!", True, (0, 0, 0), (255, 255, 255))

    x = screenSize[0] / 2 - player_size[0] / 2
    y = screenSize[1] - player_size[1]
    pygame.init()
    finished = False
    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE] == 1:
            y -= 5
        # rect_one = pygame.Rect(x, y, 30, 30)
        # color = (0, 0, 255)
        # black = (0, 0, 0)
        # screen.fill(black)
        screen.blit(background_image, (0, 0))
        screen.blit(treasure_image, treasure_position)
        screen.blit(player_image, (x, y))

        enemy_position = (enemy_position[0] + 5, enemy_position[1])
        if enemy_position[0] > screenSize[0] + 5:
            enemy_position = (0, enemy_position[1])

        screen.blit(enemy_image, enemy_position)


        collision_treasure = check_collision_treasure(x, y)
        if collision_treasure == True:
            show_text(screen, textWin, screenSize)
            pygame.display.flip()
            frame.tick(1)
            x = screenSize[0] / 2 - player_size[0] / 2
            y = screenSize[1] - player_size[1]

        # pygame.draw.rect(screen, color, rect_one)
        pygame.display.flip()
        frame.tick(30)

def check_collision_treasure(x, y):
    collision_state = False
    if y >= treasure_position[1] and y <= treasure_position[1] + treasure_size[1]:
        if x >= treasure_position[0] and x <= treasure_position[0] + treasure_size[0]:
            collision_state = True
        elif x + player_size[0] >= treasure_position[0] and x + player_size[0] <= treasure_position[0] + treasure_size[0]:
            collision_state = True
    elif y + player_size[1] >= treasure_position[1] and y + player_size[1] <= treasure_position[1] + player_size[1]:
        if x >= treasure_position[0] and x <= treasure_position[0] + treasure_size[0]:
            collision_state = True
        elif x + player_size[0] >= treasure_position[0] and x + player_size[0] <= treasure_position[0] + treasure_size[0]:
            collision_state = True
    return collision_state

def show_text(screen, textWin, screenSize):
    screen.blit(textWin, (screenSize[0] / 2 - textWin.get_width() / 2, screenSize[1] / 2 - textWin.get_height() / 2))


if __name__ == '__main__':
    print 'EXECUTING...'
    main()