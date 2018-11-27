import pygame
pygame.init()
from pygame.sprite import Group
from pygame.sprite import groupcollide
from Hero import Hero
theHero = Hero()
from BadGuy import BadGuy
bad_guy = BadGuy()
bad_guys = Group()
bad_guys.add(bad_guy)
from Arrow import Arrow
arrows = Group()
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Robin Hood')
background_image = pygame.image.load('background.png')
theHero.draw_me(512,480)
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 275:
                theHero.shouldMove("right",True)
            elif event.key == 276:
                theHero.shouldMove("left",True)
            if event.key == 273:
                theHero.shouldMove("up",True)
            elif event.key == 274:
                theHero.shouldMove("down",True)
            elif event.key == 32:
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)
        elif event.type == pygame.KEYUP:
            if event.key == 275:
                theHero.shouldMove("right",False)
            elif event.key == 276:
                theHero.shouldMove("left",False)
            if event.key == 273:
                theHero.shouldMove("up",False)
            elif event.key == 274:
                theHero.shouldMove("down",False)        
    pygame_screen.blit(background_image,[0,0])
    theHero.draw_me(512,480)
    for bad_guy in bad_guys:
        bad_guy.move_me(theHero)
        pygame_screen.blit(monster_image, [bad_guy.x, bad_guy.y])
    for arrow in arrows:
        arrow.update_me()
        pygame_screen.blit(arrow_image,[arrow.x, arrow.y])
    pygame_screen.blit(hero_image,[theHero.x, theHero.y])
    arrow_hit = groupcollide(arrows, bad_guys, True, True)
    if arrow_hit:
        bad_guys.add(BadGuy())
    pygame_screen.blit(monster_image,[bad_guy.x, bad_guy.y])
    pygame.display.flip()

    
    
