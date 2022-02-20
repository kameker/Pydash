import pygame
from Generation import Generator
from Square import player
from Square import player_sprites
from Square import clock
from Generation import all_Obstacle_sprites
from Obstacle import stop_flag


def startlvl(name_level):
    pygame.init()
    background = pygame.image.load('textures/background.jpg')
    size = (1300, 700)
    level = pygame.display.set_mode(size)
    board = Generator(name_level)
    board.open_file()
    board.generate_level()
    running = True
    while running:
        level.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.jump_flag = True
        if stop_flag:
            print('anything')
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


