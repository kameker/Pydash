import os
import sys
import pygame
from Square import player

all_Obstacle_sprites = pygame.sprite.Group()


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
        super().__init__(all_Obstacle_sprites)
        self.image = CubeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.y + 50 > player.rect.y + 50 > self.rect.y \
                and self.rect.x + 50 > player.rect.x + 50 > self.rect.x:
            player.rect.x = 0
            player.rect.y = 650
        elif self.rect.x + 50 > player.rect.x + 50 > self.rect.x \
                and player.rect.y + 50 == self.rect.y:
            player.jump = False


class SpikeObst(pygame.sprite.Sprite):
    image = load_image('spike.png')

    def __init__(self):
        super().__init__(all_Obstacle_sprites)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, player):
            player.rect.x = 0
            player.rect.y = 650


class OrbObst(pygame.sprite.Sprite):
    image = load_image('orb.png')

    def __init__(self):
        super().__init__(all_Obstacle_sprites)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        if pygame.sprite.collide_mask(self, player) and pygame.event.type == pygame.MOUSEBUTTONDOWN:
            player.jump = True


class LowerOrbObst(pygame.sprite.Sprite):
    image = load_image('loverOrb.png')

    def __init__(self):
        super().__init__(all_Obstacle_sprites)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, player):
            player.jump = True
