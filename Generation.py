from Obstacle import SpikeObst, LowerOrbObst, CubeObst, FinishObst
from Obstacle import all_Obstacle_sprites, finish_sprites


class Generator:
    def __init__(self, level_name):
        self.cell_size = 50
        self.level_name = level_name
        self.list_of_object = []  # список объектов с координатаим
        self.list_of_coords = []  # список координат

    # открытие файла с уровнем и запись его в список объектов
    def open_file(self):
        with open("levelList/" + self.level_name, encoding="utf8") as f:
            s = f.read()
        if s:
            self.list_of_object = [i for i in s.split("\n")]
            if self.list_of_object[-1] == "":
                self.list_of_object.pop(-1)

    # генерация уровня по списку объектов
    def generate_level(self):
        for i in self.list_of_object:
            data = i.split()  # координаты по умолчанию
            coords = (int(data[1]),
                      int(data[2]))  # изменение координат чтобы они были кратны self.cell_size
            x = coords[0]
            y = coords[1]
            data = data[0]  # data ахранит название припятствия
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
                finish_sprites.add(cube)
                self.second_stage_of_generation(cube, x, y)

    def second_stage_of_generation(self, cube, x, y):
        all_Obstacle_sprites.add(cube)
        cube.rect.x = x
        cube.rect.y = y
