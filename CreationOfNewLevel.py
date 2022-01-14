import pygame

from Generation import Generator
from Square import clock
from ObstacleForNewLevel import all_sprite
from ObstacleForNewLevel import SpikeObst, LowerOrbObst, CubeObst, NothingObst, FinishObst


class NewLevel:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = 50
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
            if name_obj == "cube":
                cube = CubeObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "spike":
                cube = SpikeObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "loverOrb":
                cube = LowerOrbObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "nothing":
                cube = NothingObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "finish":
                cube = FinishObst(x, y)
                self.second_stage_of_generation(cube, x, y)
            self.list_of_coords.append((x, y))
            self.list_of_obj.append(f"{name_obj} {x + self.removal} {y}")
            print(len(self.list_of_obj))

    def second_stage_of_generation(self, cube, x, y):
        all_sprite.add(cube)
        cube.rect.x = x
        cube.rect.y = y

    def save_level(self, fname):
        if self.list_of_obj:
            e = open("levels/" + fname + '.txt', encoding="utf8", mode="w")
            for i in self.list_of_obj:
                if i != "None":
                    e.write(str(i) + '\n')
            e.close()

    def del_obj(self, coords):
        id = 0
        coords = ((coords[0]) // self.cell_size, (coords[1]) // self.cell_size)
        x = coords[0] * self.cell_size
        y = coords[1] * self.cell_size
        for i in self.list_of_coords:
            if (x, y) == i:
                self.list_of_coords[id] = "None"
                self.list_of_obj[id] = "None"
                break
            id += 1
        obst = self.list_of_obj[id].split()[0]
        cube = NothingObst(x, y)
        self.second_stage_of_generation(cube, x, y)


background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
work_zone = pygame.display.set_mode(size)
level_zone = NewLevel(work_zone, size[0], size[1])
board = Generator(30, 14, "")
running = True
flag_obj = False

while running:
    work_zone.blit(background, (0, 0))
    board.render(work_zone)
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
                all_sprite.update(-50)
            if event.key == pygame.K_LEFT:
                level_zone.removal -= 50
                all_sprite.update(50)
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = event.pos
            flag_obj = True
            name_obj = None
        if event.type == pygame.KEYDOWN and flag_obj:
            if event.key == pygame.K_z:
                name_obj = "cube"
            if event.key == pygame.K_x:
                name_obj = "spike"
            if event.key == pygame.K_c:
                name_obj = "loverOrb"
            if event.key == pygame.K_d:
                level_zone.del_obj(coords)
            if event.key == pygame.K_v:
                name_obj = "finish"
            flag_obj = False
            if name_obj:
                level_zone.get_click(coords, name_obj)
    all_sprite.draw(work_zone)
    pygame.display.flip()
    clock.tick(100)
