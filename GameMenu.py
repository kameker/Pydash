# импорт библиотек
import pygame
import sys
import os
from Generation import start_genration

play_button = 'textures/play_button.png'

pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)

pygame.display.set_caption('PyDash')

clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

menu_img = pygame.image.load('textures/background.jpg')


class Play_Button(pygame.sprite.Sprite):
    def __init__(self, *group, name):
        super().__init__(*group)
        self.name = name

        self.image = pygame.image.load(self.name)
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(350, 250)


    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            pygame.quit()
            start_genration()


class Button:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.move_button = (222, 31, 192)
        self.not_move_button = (140, 15, 118)

    def print_text(self, text, x, y, font_color=(0, 0, 0), font_size=30, font_type='Geometry_Dash.ttf'):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(text, True, font_color)
        screen.blit(text, (x, y))

    def draw(self, x, y, message, action=None):
        location = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if x < location[0] < x + self.w and y < location[1] < y + self.h:
            pygame.draw.rect(screen, self.move_button, (x, y, self.w, self.h))

            if click[0] == 1:
                pass
        else:
            pygame.draw.rect(screen, self.not_move_button, (x, y, self.w, self.h))

        self.print_text(message, x + 10, y + 10)


running = True

screen.blit(menu_img, (0, 0))
pygame.display.update()
button = Button(180, 70)
button.print_text('PyDash', 350, 60, font_size=62, font_color=(0, 0, 0))
button.print_text('PyDash', 350, 60, font_size=60, font_color=(73, 210, 11))
# button.draw(400, 300, 'Играть')
Play_Button(all_sprites, name=play_button)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    clock.tick(30)
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()


# запуск
#if __name__ == '__main__':
    #main = Main()