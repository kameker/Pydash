import os
import sys
import pygame


pygame.init()
size = width, height = 1300, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player_sprites = pygame.sprite.Group()
jump = False


def load_image(name, colorkey=None):  # функция загрузки изображения
    fullname = os.path.join('textures', name)  # поиск изображения по имени в папке textures
    if not os.path.isfile(fullname): # если файл не существует, то выходим
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:  # прозрачное/непрозрачное
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):  # класс игрока
    image = load_image('player.png')

    def __init__(self, *group):
        super().__init__(player_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = height - 50
        self.jump = 30
        self.jump_flag = False  # флаг прыжка
        self.mask = pygame.mask.from_surface(self.image)
        self.y_now = 650  # переменная координат для возврата

    def update(self):  # метож прыжка
        if self.jump_flag:
            if self.rect.y <= self.y_now:
                if self.jump < -1:
                    self.rect.y += 5
                else:
                    self.rect.y -= 5
                self.jump -= 1
            else:
                self.rect.y = self.y_now
                self.jump_flag = False
                self.jump = 30
        else:  # эта часть нужна для работы запрыгивания на куб
            if self.rect.y < self.y_now:
                self.rect.y += 5
            elif self.rect.y > self.y_now:
                self.rect.y = self.y_now
            self.jump = 30


player = Player(player_sprites)