import pygame
from Generation import Generator
from Square import Camera
from Square import Player
from Square import player_sprites
from Square import clock
from Generation import Obstacle_sprites
from Generation import orb_sprites
from Generation import lower_orb_sprites
from Generation import cube_sprites

background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
level = pygame.display.set_mode(size)
board = Generator(30, 14, "level.txt")
running = True
camera = Camera()
player = Player(player_sprites)
board.open_file()
board.generate_level(level)
while running:
    level.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.jump_flag = True
    player_sprites.draw(level)
    player_sprites.update()
    Obstacle_sprites.draw(level)
    Obstacle_sprites.update()
    orb_sprites.draw(level)
    orb_sprites.update()
    lower_orb_sprites.draw(level)
    lower_orb_sprites.update()
    cube_sprites.draw(level)
    cube_sprites.update()
    pygame.display.flip()
    clock.tick(60)
