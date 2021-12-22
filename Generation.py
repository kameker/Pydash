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
        print(self.list_of_object)

    def generate_level(self):
        for i in self.list_of_object:
            data = i.split()
            coords = (int(data[1]), int(data[2]))
            coords = ((coords[0] - self.left) // self.cell_size, (coords[1] - self.top) // self.cell_size)
            x = coords[0] * self.cell_size + self.left
            y = coords[1] * self.cell_size + self.top
            if (x, y) not in self.list_of_coords:
                if data[0] == "cube":
                    pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                                     (x + 1, y + 1,
                                      self.cell_size - 2, self.cell_size - 2))
                    self.list_of_coords.append((x, y))
                elif data[0] == "spike":
                    pygame.draw.polygon(screen, pygame.Color(0, 255, 0),
                                        ((x, y + self.cell_size), (x + self.cell_size, y + self.cell_size),
                                         (x + self.cell_size // 2, y)))
                    self.list_of_coords.append((x, y))
                elif data[0] == "orb":
                    pygame.draw.circle(screen, pygame.Color(255, 255, 0), (x + self.cell_size // 2, y + self.cell_size // 2),
                                       self.cell_size // 3)
                    self.list_of_coords.append((x, y))


size = (1000, 700)
screen = pygame.display.set_mode(size)
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
