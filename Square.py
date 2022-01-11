import os
import sys
import pygame


pygame.init()
size = width, height = 1300, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player_sprites = pygame.sprite.Group()
jump = False


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


class Player(pygame.sprite.Sprite):
    image = load_image('player.png')

    def __init__(self, *group):
        super().__init__(player_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height - 50
        self.jump = 10
        self.jump_flag = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += 10
        if self.jump_flag:
            if self.jump >= -10:
                if self.jump < 0:
                    self.rect.y += (self.jump ** 2) / 2
                else:
                    self.rect.y -= (self.jump ** 2) / 2
                self.jump -= 1
            else:
                self.jump_flag = False
                self.jump = 10


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)