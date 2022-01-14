import pygame
from Obstacle import load_image

all_sprite = pygame.sprite.Group()


class LowerOrbObst(pygame.sprite.Sprite):
    image = load_image('loverOrb.png')

    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = LowerOrbObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, direction):
        if direction > 0:
            self.rect.x += 50
        else:
            self.rect.x -= 50



class NothingObst(pygame.sprite.Sprite):
    image = load_image('nothing.png')

    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = NothingObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, direction):
        if direction > 0:
            self.rect.x += 50
        else:
            self.rect.x -= 50


class SpikeObst(pygame.sprite.Sprite):
    image = load_image('spike.png')

    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, direction):
        if direction > 0:
            self.rect.x += 50
        else:
            self.rect.x -= 50


class CubeObst(pygame.sprite.Sprite):
    image = load_image('cube.png')

    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = CubeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, direction):
        if direction > 0:
            self.rect.x += 50
        else:
            self.rect.x -= 50


class FinishObst(pygame.sprite.Sprite):
    image = load_image('finish.png')

    def __init__(self, x, y):
        super().__init__(all_sprite)
        self.image = FinishObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self, direction):
        if direction > 0:
            self.rect.x += 50
        else:
            self.rect.x -= 50
