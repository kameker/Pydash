from ObstacleForNewLevel import all_sprite
from ObstacleForNewLevel import SpikeObst, LowerOrbObst, CubeObst, NothingObst, FinishObst

list_of_obj = []


class NewLevel:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = 50
        self.list_of_coords = []
        self.removal = 0
        self.porg = 30

    def get_click(self, coords, name_obj):
        global list_of_obj
        coords = ((coords[0]) // self.cell_size, (coords[1]) // self.cell_size)
        x = coords[0] * self.cell_size
        y = coords[1] * self.cell_size
        if (x + self.removal,
            y) not in self.list_of_coords:  # сравнивает еслти объект с темеже координатами в списке координат
            if name_obj == "cube":
                cube = CubeObst(x + self.removal, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "spike":
                cube = SpikeObst(x + self.removal, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "loverOrb":
                cube = LowerOrbObst(x + self.removal, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "nothing":
                cube = NothingObst(x + self.removal, y)
                self.second_stage_of_generation(cube, x, y)
            elif name_obj == "finish":
                cube = FinishObst(x + self.removal, y)
                self.second_stage_of_generation(cube, x, y)
            self.list_of_coords.append((x, y))
            list_of_obj.append(f"{name_obj} {x + self.removal} {y}")

    def second_stage_of_generation(self, cube, x, y):
        all_sprite.add(cube)
        cube.rect.x = x
        cube.rect.y = y

    # удаляет объект из списков уровня
    def del_obj(self, coords):
        global list_of_obj
        id = 0
        coords = ((coords[0]) // self.cell_size, (coords[1]) // self.cell_size)
        x = coords[0] * self.cell_size
        y = coords[1] * self.cell_size
        for i in self.list_of_coords:
            if (x, y) == i:
                self.list_of_coords[id] = "None"
                list_of_obj[id] = "None"
                break
            id += 1
        cube = NothingObst(x, y)
        self.second_stage_of_generation(cube, x, y)
