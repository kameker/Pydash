import pygame
from Generation import Generator
from Square import Player, player
from Square import player_sprites
from Obstacle import orb_flag
from Square import clock
from Generation import all_Obstacle_sprites

background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
level = pygame.display.set_mode(size)
board = Generator(30, 14, "level.txt")
running = True
board.open_file()
board.generate_level(level)
while running:
    level.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.jump_flag = True
            orb_flag = True
    player_sprites.draw(level)
    player_sprites.update()
    all_Obstacle_sprites.draw(level)
    all_Obstacle_sprites.update()
    pygame.display.flip()
    clock.tick(100)
