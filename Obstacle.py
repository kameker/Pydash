import os
import sys
import pygame
from Square import Player


def load_image(name, colorkey=None):
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


class CubeObst(pygame.sprite.Sprite):
    image = load_image('cube.png')

    def __init__(self):
        super().__init__()
        self.image = CubeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.y + 50 > Player.image.rect.y + 50 > self.rect.y \
                and self.rect.x + 50 > Player.image.rect.x + 50 > self.rect.x:
            print('cube!')  # проверка
        elif self.rect.x + 50 > Player.image.rect.x + 50 > self.rect.x \
                and Player.image.rect.y + 50 == self.rect.y:
            print('продолжаем ехать')


class SpikeObst(pygame.sprite.Sprite):
    image = load_image('spike.png')

    def __init__(self):
        super().__init__()
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, Player.image):
            print('spike!')  # проверка


class OrbObst(pygame.sprite.Sprite):
    image = load_image('orb.png')

    def __init__(self):
        super().__init__()
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        if pygame.sprite.collide_mask(self, Player.image) and pygame.event.type == pygame.MOUSEBUTTONDOWN:
            print('прыжок!')  # проверка


class LowerOrbObst(pygame.sprite.Sprite):
    image = load_image('loverOrb.png')

    def __init__(self):
        super().__init__()
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, Player.image):
            print('нижний прыжок!')  # проверка