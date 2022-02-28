import pygame

from CreationOfNewLevel import NewLevel
from Square import clock
from ObstacleForNewLevel import all_sprite


def StartCreation():
    background = pygame.image.load('textures/background.jpg')
    size = (1920, 1080)
    work_zone = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    level_zone = NewLevel(work_zone, size[0], size[1])  # поле для создания уровня
    running = True
    flag_obj = False

    while running:
        work_zone.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:
                    running = False
                if event.key == pygame.K_RIGHT:
                    level_zone.removal += 50
                    all_sprite.update(-50)  # смещение поля на 1 клетку влево
                if event.key == pygame.K_LEFT:
                    level_zone.removal -= 50
                    all_sprite.update(50)  # смещение поля на 1 клетку вправо
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = event.pos  # координаты от клика
                flag_obj = True
                name_obj = None
            if event.type == pygame.KEYDOWN and flag_obj:
                if event.key == pygame.K_z:
                    name_obj = "cube"
                if event.key == pygame.K_x:
                    name_obj = "spike"
                if event.key == pygame.K_c:
                    name_obj = "loverOrb"
                if event.key == pygame.K_d:
                    level_zone.del_obj(coords)
                if event.key == pygame.K_v:
                    name_obj = "finish"
                flag_obj = False
                if name_obj:
                    level_zone.get_click(coords, name_obj)  # при клике на определённые клавиши будет появляться объект
        all_sprite.draw(work_zone)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
