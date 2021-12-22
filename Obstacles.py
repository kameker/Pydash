import os
import sys
import pygame


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


class Level(''''''):
    pass


class SquareObst:
    image = load_image('''file_name''')  # уровень генерируется через текстовый файл, примеров пока нет

    def __init__(self):
        super().__init__(all_sprites)
        self.image = SquareObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
