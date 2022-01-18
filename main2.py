import pygame
from GameMenu import Button
from GameMenu import Play_Button
from GameMenu import CreationLevel
running = True

clock = pygame.time.Clock()
background = pygame.image.load('textures/background.jpg')
size = 1300, 700
screen2 = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
play_button = 'textures/play_button.png'
newlevelbutton = 'textures/newlevelbutton.png'
button = Button(180, 70)
button.print_text('PyDash', 350, 60, font_size=62, font_color=(0, 0, 0))
button.print_text('PyDash', 350, 60, font_size=60, font_color=(73, 210, 11))
Play_Button(all_sprites, name=play_button)
CreationLevel(all_sprites, name=newlevelbutton)

while running:
    screen2.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    clock.tick(30)
    all_sprites.draw(screen2)
    pygame.display.flip()