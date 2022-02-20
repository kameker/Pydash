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
        if (x + self.removal, y) not in self.list_of_coords:
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
            self.list_of_obj.append(f"{name_obj} {x + self.removal} {y}")

    def second_stage_of_generation(self, cube, x, y):
        all_sprite.add(cube)
        cube.rect.x = x
        cube.rect.y = y

    def save_level(self, fname):
        sp = []
        with open('data/levels.txt', encoding="utf8") as f:
            s = f.read()
            for i in s:
                sp.append(i)
        with open('data/levels.txt', encoding="utf8", mode="w") as f:
            for i in sp:
                f.write(i)
            f.write("\n")
            f.write(fname + ".txt")
        if self.list_of_obj:
            e = open("levelList/" + fname + '.txt', encoding="utf8", mode="w")
            for i in self.list_of_obj:
                if i != "None":
                    e.write(str(i) + '\n')
            e.close()

    # удаляет объект из списков уровня
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
        cube = NothingObst(x, y)
        self.second_stage_of_generation(cube, x, y)
