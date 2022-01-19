import pygame
from Square import player, load_image
from QTStopGame import Main

all_Obstacle_sprites = pygame.sprite.Group()
speed = 5
deaths = 1


def restart():
    global deaths
    deaths += 1
    pygame.time.delay(1000)
    for i in all_Obstacle_sprites:
        i.rect.x = i.x
        i.rect.y = i.y
        player.jump_flag = False


# класс для кубов
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
        global speed
        self.rect.x -= speed
        if self.rect.y + 50 >= player.rect.y + 50 > self.rect.y \
                and player.rect.x + 50 == self.rect.x:
            restart()
        if pygame.sprite.collide_mask(self, player):
            player.y_now = self.rect.y - 50
            player.rect.y = player.y_now
            player.jump_flag = False
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
        global speed
        self.rect.x -= speed
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

    def update(self):
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):
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
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):
            player.jump_flag = True


class FinishObst(pygame.sprite.Sprite):
    image = load_image('finish.png')

    def __init__(self, x, y):
        super().__init__(all_Obstacle_sprites)
        self.image = FinishObst.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y

    def update(self):
        global speed
        self.rect.x -= speed
        if pygame.sprite.collide_mask(self, player):
            speed = 0
            self.win = Main(deaths)
            self.win.setObjectName("MainWindow")
            self.win.setStyleSheet("#MainWindow{border-image:url(textures/background.jpg)}")
            self.win.show()
            pygame.quit()
