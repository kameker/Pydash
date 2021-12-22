# импорт библиотек
import pygame

pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)

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




class Main:
    # инициальзация
    def __init__(self):

        menu_img = pygame.image.load('background.png')

        running = True

        screen.blit(menu_img, (0, 0))
        pygame.display.update()
        button = Button(180, 70)
        button.print_text('PyDash', 350, 100, font_size=62, font_color=(0, 0, 0))
        button.print_text('PyDash', 350, 100, font_size=60, font_color=(73, 210, 11))
        button.draw(400, 300, 'Играть')

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()




    # открытие окна с заданиями
    def open_level(self):
        pass
        # открытие qt окна с уровнями

    def open_registration(self):
        pass
        # открытие окна qt с регистрацией и статистикой

    def open_creation_new_level(self):
        pass
        # открытие pygame окна с созданием уровней




# запуск
if __name__ == '__main__':
    main = Main()
