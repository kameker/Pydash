import pygame
from Generation import Generator
from Square import player
from Square import player_sprites
from Square import clock
from Generation import all_Obstacle_sprites, finish_sprites


def StartLevel(name_level, running):
    pygame.init()
    for item in all_Obstacle_sprites:
        item.kill()
    background = pygame.image.load('textures/background.jpg')
    level = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    board = Generator(name_level)
    board.open_file()
    board.generate_level()
    while running:
        level.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.jump_flag = True  # прыжок
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
        for i in finish_sprites:
            if i.stop_flag:
                running = False
        player_sprites.draw(level)
        player_sprites.update()
        all_Obstacle_sprites.draw(level)
        all_Obstacle_sprites.update()
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
    for item in all_Obstacle_sprites:
        item.kill()
    return
