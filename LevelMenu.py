import pygame

play_button = 'textures/play_button.png'
left = 'textures/left120.png'
right = 'textures/right120.png'

pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
pygame.display.set_caption('PyDash')
clock = pygame.time.Clock()
music = pygame.mixer.Sound('textures/music_menu.mp3')
music.play(-1)
menu_img = pygame.image.load('background.png')


class Level(pygame.sprite.Sprite):
    def __init__(self, *group, name, x, y):
        super().__init__(*group)
        self.name = name

        self.image = pygame.image.load(self.name)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            ans = args[0].pos
            if ans[0] > 800:
                print('Нажата кнопка: Вправо')
            if ans[0] < 218:
                print('Нажата кнопка: Влево')


running = True

screen.blit(menu_img, (0, 0))
pygame.display.update()

Level(all_sprites, name=right, x=800, y=300)
Level(all_sprites, name=left, x=100, y=300)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    all_sprites.draw(screen)
    all_sprites.update(event)
    clock.tick(30)
    pygame.display.flip()