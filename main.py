import pygame
from Generation import Generator
from Square import Camera
from Square import Player
from Square import all_sprites
from Square import player_sprites
from Square import clock

background = pygame.image.load('textures/background.jpg')
size = (1300, 700)
level = pygame.display.set_mode(size)
level.blit(background, (0, 0))
board = Generator(30, 14)
running = True
camera = Camera()
player = Player(all_sprites, player_sprites)
# board.render(level)
board.open_file()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            jump = True
    all_sprites.draw(level)
    board.generate_level(level)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(60)
