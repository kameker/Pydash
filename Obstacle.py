import os
import sys
import pygame
from Square import player
all_sprite = pygame.sprite.Group()

all_Obstacle_sprites = pygame.sprite.Group()


def restart():
    pygame.time.delay(1000)
    for i in all_Obstacle_sprites:
        i.rect.x = i.x
        i.rect.y = i.y


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


class all_sprites(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = all_sprite.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        self.rect.x -= 5


class CubeObst(pygame.sprite.Sprite):
    image = load_image('cube.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = CubeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.y + 50 >= player.rect.y + 50 > self.rect.y \
                and player.rect.x + 50 == self.rect.x:
            restart()
        if pygame.sprite.collide_mask(self, player):
            player.y_now = self.rect.y - 50
            player.rect.y = player.y_now
        else:
            player.y_now = 650


class SpikeObst(pygame.sprite.Sprite):
    image = load_image('spike.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        self.rect.x -= 5
        if pygame.sprite.collide_mask(self, player):
            restart()


class OrbObst(pygame.sprite.Sprite):
    image = load_image('orb.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = OrbObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, *args):
        self.rect.x -= 5
        if pygame.sprite.collide_mask(self, player):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN:
                player.jump_flag = True
                player.jump = 30


class LowerOrbObst(pygame.sprite.Sprite):
    image = load_image('loverOrb.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = LowerOrbObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        self.rect.x -= 5
        if pygame.sprite.collide_mask(self, player):
            player.jump_flag = True
