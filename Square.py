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
        self.jump = 11
        self.jump_flag = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.jump_flag:
            if self.jump >= -11:
                if self.jump < 0:
                    self.rect.y += (self.jump ** 2) / 2
                else:
                    self.rect.y -= (self.jump ** 2) / 2
                self.jump -= 1
            else:
                self.jump_flag = False
                self.jump = 11


player = Player(player_sprites)