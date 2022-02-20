import pygame
from Square import player, load_image
from QTStopGame import Main

all_Obstacle_sprites = pygame.sprite.Group()
finish_sprites = pygame.sprite.Group()
speed = 5  # скорость
deaths = 0  # счётчик смертей


def restart():  # функция рестарта
    global deaths
    deaths += 1
    pygame.time.delay(1000)
    for i in all_Obstacle_sprites:
        i.rect.x = i.x
        i.rect.y = i.y
        player.jump_flag = False


class CubeObst(pygame.sprite.Sprite):  # класс кубов
    image = load_image('cube.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = CubeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        global speed
        self.rect.x -= speed  # перемещение
        if self.rect.y + 50 >= player.rect.y + 50 > self.rect.y \
                and player.rect.x + 50 == self.rect.x:  # условие при котором соприкосновение игрока и куба смертельно
            restart()
        if pygame.sprite.collide_mask(self, player):
            player.y_now = self.rect.y - 50  # смена координат возврата
            player.rect.y = player.y_now - 1
            player.jump_flag = False
        else:
            player.y_now = 650  # если игрок не на кубе то он будет падать вниз пока не упрётся пол (или другой куб)


class SpikeObst(pygame.sprite.Sprite):  # класс шипов
    image = load_image('spike.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = SpikeObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):  # соприкосновение игрока и шипа смертельно
            restart()


class OrbObst(pygame.sprite.Sprite):  # класс орбов
    image = load_image('orb.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = OrbObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):  # вызов прыжка при соприкосновении орба и игрока
            player.jump_flag = True
            player.jump = 30


class LowerOrbObst(pygame.sprite.Sprite):  # класс нижних орбов
    image = load_image('loverOrb.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = LowerOrbObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):  # вызов прыжка при соприкосновении нижнего орба и игрока
            player.jump_flag = True


class FinishObst(pygame.sprite.Sprite):  # класс финиша
    image = load_image('finish.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = FinishObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.stop_flag = False
        self.x = x
        self.y = y

    def update(self):
        global speed
        global deaths
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player): # остановка игрока (но на самом деле карты) на финише
            speed = 0
            deaths = 0
            self.stop_flag = True
