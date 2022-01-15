import pygame
from Obstacle import SpikeObst, LowerOrbObst, CubeObst, FinishObst
from Obstacle import all_Obstacle_sprites


class Generator:
    def __init__(self, width, height, level_name):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 50
        self.level_name = level_name
        self.list_of_object = []
        self.list_of_coords = []

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (i * self.cell_size + self.left, j * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def open_file(self):
        print("levels/" + self.level_name)
        with open("levels/" + self.level_name, encoding="utf8") as f:
            s = f.read()
        if s:
            self.list_of_object = [i for i in s.split("\n")]
            if self.list_of_object[-1] == "":
                self.list_of_object.pop(-1)

    def generate_level(self):
        for i in self.list_of_object:
            data = i.split()
            coords = (int(data[1]), int(data[2]))
            coords = ((coords[0] - self.left) // self.cell_size, (coords[1] - self.top) // self.cell_size)
            x = coords[0] * self.cell_size + self.left
            y = coords[1] * self.cell_size + self.top
            data = data[0]
            if data == "cube":
                cube = CubeObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif data == "spike":
                cube = SpikeObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif data == "loverOrb":
                cube = LowerOrbObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif data == "finish":
                cube = FinishObst(x, y)
                self.second_stage_of_generation(cube, x, y)

    def second_stage_of_generation(self, cube, x, y):
        all_Obstacle_sprites.add(cube)
        cube.rect.x = x
        cube.rect.y = y

