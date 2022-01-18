import pygame
from FirstAssembly import MAIN

levels = []
right = 'textures/right120.png'
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
pygame.display.set_caption('PyDash')
clock = pygame.time.Clock()
menu_img = pygame.image.load('textures/background.jpg')

f = open('data/levels.txt', 'r')
a = f.read()
levels = a.split('\n')

global s


# global levels_num


class Level_name:
    # изменение текста
    def __init__(self, f=None):
        global s
        s = f
        self.text_map()


    def text_map(self):
        screen.blit(menu_img, (0, 0))
        pygame.display.update()
        button = Button(160, 70)
        button.print_text(levels[s], 380, 330)
        button.print_text('PyDash', 350, 60, font_size=62, font_color=(0, 0, 0))
        button.print_text('PyDash', 350, 60, font_size=60, font_color=(73, 210, 11))


class Level(pygame.sprite.Sprite):
    def __init__(self, *group, name, x, y):
        super().__init__(*group)
        self.name = name
        self.n = 0
        self.image = pygame.image.load(self.name)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            ans = args[0].pos
            if ans[0] > 800 and self.n <= len(levels) - 2:
                self.n += 1
                Level_name(f=self.n)

            else:
                self.n = 0
                Level_name(f=self.n)


class Button:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.move_button = (222, 31, 192)
        self.not_move_button = (140, 15, 118)

    def print_text(self, text, x, y, font_color=(0, 0, 0), font_size=30, font_type='textures/Geometry_Dash.ttf'):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(text, True, font_color)
        screen.blit(text, (x, y))

    def draw(self, x, y, message, level=None):
        global s
        location = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if x < location[0] < x + self.w and y < location[1] < y + self.h:
            pygame.draw.rect(screen, self.move_button, (x, y, self.w, self.h))

            if click[0] == 1:
                try:
                    MAIN(levels[s], True)
                except:
                    print("не вышло")

        else:
            pygame.draw.rect(screen, self.not_move_button, (x, y, self.w, self.h))

        self.print_text(message, x + 10, y + 10)


def andrey():
    running = True
    screen.blit(menu_img, (0, 0))
    temp = Level(all_sprites, name=right, x=800, y=300)
    levels_num = 0
    button = Button(160, 70)
    button.print_text('PyDash', 350, 60, font_size=62, font_color=(0, 0, 0))
    button.print_text('PyDash', 350, 60, font_size=60, font_color=(73, 210, 11))
    button.print_text(levels[levels_num], 380, 330)
    pygame.display.update()
    temp.update()
    while running:
        screen.blit(menu_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        button.draw(430, 500, 'Играть')
        all_sprites.draw(screen)
        clock.tick(10)
        pygame.display.flip()
