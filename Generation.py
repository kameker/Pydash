import os
import sys

import pygame


class Generator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 50
        self.name_file = "level.txt"
        self.list_of_object = []
        self.list_of_coords = []
        self.Obstacle_sprites = pygame.sprite.Group()

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (i * self.cell_size + self.left, j * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def open_file(self):
        with open(self.name_file, encoding="utf8") as f:
            s = f.read()
        if s:
            self.list_of_object = [i for i in s.split("\n")]
            if self.list_of_object[-1] == "":
                self.list_of_object.pop(-1)
        print(self.list_of_object)

    def generate_level(self):
        for i in self.list_of_object:
            data = i.split()
            coords = (int(data[1]), int(data[2]))
            coords = ((coords[0] - self.left) // self.cell_size, (coords[1] - self.top) // self.cell_size)
            x = coords[0] * self.cell_size + self.left
            y = coords[1] * self.cell_size + self.top
            self.first_stage_generation(data[0], x, y)
        self.Obstacle_sprites.draw(screen)

    def first_stage_generation(self, data, x, y):
        picture = self.load_image(data + ".png")
        cube = pygame.sprite.Sprite()
        cube.image = picture
        cube.rect = cube.image.get_rect()
        self.Obstacle_sprites.add(cube)
        if data == "orb":
            x += 5
            y += 5
        cube.rect.x = x
        cube.rect.y = y

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('textures', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
screen = pygame.display.set_mode(size)
screen.blit(background, (0, 0))
board = Generator(20, 14)
running = True
# board.render(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = event.pos
            board.open_file()
            board.generate_level()
        pygame.display.flip()
