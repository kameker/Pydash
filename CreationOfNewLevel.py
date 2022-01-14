import os

import pygame

from Generation import Generator
from Square import clock
from Obstacle import load_image


class NewLevel:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = 50
        self.all_sprite = pygame.sprite.Group()
        self.list_of_coords = []
        self.list_of_obj = []
        self.removal = 0

    def get_click(self, coords, name_obj):
        coords = ((coords[0]) // self.cell_size, (coords[1]) // self.cell_size)
        x = coords[0] * self.cell_size
        y = coords[1] * self.cell_size
        if name_obj == "orb":
            x += 5
            y += 5
        if (x, y) not in self.list_of_coords:
            picture = load_image(name_obj + ".png")
            cube = pygame.sprite.Sprite()
            cube.image = picture
            cube.rect = cube.image.get_rect()
            self.all_sprite.add(cube)
            cube.rect.x = x
            cube.rect.y = y
            self.list_of_coords.append((x, y))
            self.list_of_obj.append(f"{name_obj} {x + self.removal} {y}")

    def save_level(self, fname):
        if self.list_of_obj:
            e = open("levels/" + fname + '.txt', encoding="utf8", mode="w")
            for i in self.list_of_obj:
                e.write(str(i) + '\n')
            e.close()



background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
work_zone = pygame.display.set_mode(size)
level_zone = NewLevel(work_zone, size[0], size[1])
board = Generator(30, 14, "level.txt")
work_zone.blit(background, (0, 0))
board.render(work_zone)
running = True
flag_obj = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_s:
                level_zone.save_level(input("Название уровня: "))
            if event.key == pygame.K_RIGHT:
                level_zone.removal += 50
                #moveRight()
            if event.key == pygame.K_LEFT:
                level_zone.removal -= 50
                #moveLeft()
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = event.pos
            flag_obj = True
        if event.type == pygame.KEYDOWN and flag_obj:
            name_obj = "cube"
            if event.key == pygame.K_z:
                name_obj = "cube"
            if event.key == pygame.K_x:
                name_obj = "spike"
            if event.key == pygame.K_c:
                name_obj = "orb"
            if event.key == pygame.K_v:
                name_obj = "loverOrb"
            flag_obj = False
            level_zone.get_click(coords, name_obj)
        level_zone.all_sprite.draw(work_zone)
    pygame.display.flip()
    clock.tick(100)
