import os
import sys
import pygame


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
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
    image = load_image('cube.png')

    def __init__(self, *group):
        super().__init__(all_sprites, player_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height - 50
        self.jump = 9

    def update(self, *args):
        global jump
        self.rect.x += 10
        if jump:
            if self.jump >= -9:
                if self.jump < 0:
                    self.rect.y += (self.jump ** 2) / 2
                else:
                    self.rect.y -= (self.jump ** 2) / 2
                self.jump -= 1
            else:
                jump = False
                self.jump = 9


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


camera = Camera()
player = Player(all_sprites, player_sprites)
running = True
while running:
    # изменяем ракурс камеры
    camera.update(player)
    # обновляем положение всех спрайтов
    for sprite in all_sprites:
        camera.apply(sprite)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            jump = True
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()
    all_sprites.update()
    clock.tick(60)
pygame.quit()