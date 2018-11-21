import pygame
pygame.init()
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Robin Hood')
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
heroLoc = {'x':0, 'y':0}

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            print (event.key)
            print (heroLoc)
            if event.key == 275:
                heroLoc['x'] += 10
            elif event.key == 276:
                heroLoc['x'] -= 10
            elif event.key == 273:
                heroLoc['y'] -= 10
            elif event.key == 274:
                heroLoc['y'] += 10
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image,[heroLoc['x'], heroLoc['y']])
    pygame.display.flip()

    
    
