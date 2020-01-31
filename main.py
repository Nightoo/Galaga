import pygame, random, sys
from enemy import Enemy
from spaceship import Spaceship
import valuables
pygame.init()
pygame.time.set_timer(valuables.MYEVENTSPAWN, valuables.ENEMYRESPAWNTIME)
pygame.time.set_timer(valuables.MYEVENTSHOOT, valuables.ENEMYSHOOTTIME)
SIZE = valuables.WIDTH, valuables.HEIGHT
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 60
ship = Spaceship()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.4)


def mainn():
    intro_text = ['Начать игру', 'Выйти']
    SCREEN.fill((0, 0, 0))

    font_basic = pygame.font.Font(None, 40)
    text_coord = 200
    k = 0

    for line in intro_text:
        string_rendered = font_basic.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        if k == 0:
            intro_rect.x = 120
            text_coord += 80
        elif k == 1:
            intro_rect.x = 120
            text_coord += 40
        else:
            text_coord += 40
            intro_rect.x = 150
        k += 1
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        SCREEN.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 105 < event.pos[0] < 290 and 280 < event.pos[1] < 300:
                    game()
                elif 120 < event.pos[0] < 270 and 350 < event.pos[1] < 370:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


def game():
    running = True
    while running:
        SCREEN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
            if event.type == valuables.MYEVENTSPAWN:
                enemy = Enemy()
                enemy.spawn()
                enemy.shoot()

            if event.type == valuables.MYEVENTSHOOT:
                for enemy in valuables.ENEMIES:
                    enemy.shoot()
        keystate = pygame.key.get_pressed()
        ship.speed = 0
        if keystate[pygame.K_a] and ship.rect.x > 0:
            ship.speed = -8
        if keystate[pygame.K_d] and ship.rect.x + 50 < valuables.WIDTH:
            ship.speed = 8
        ship.rect.x += ship.speed

        if len(valuables.ENEMIES) == 0:
            for i in range(valuables.COUNT_ENEMIES):
                enemy = Enemy()
                enemy.spawn()
                enemy.shoot()
        if valuables.COUNT_ENEMIES == 2:
            valuables.COUNT_ENEMIES = 1
        for enemy in valuables.ENEMIES:
            enemy.draw(SCREEN)

        for bullet in valuables.BULLETS:
            bullet.fly()
            bullet.draw(SCREEN)

        for bullet in valuables.BULLETS:
            for enemy in valuables.ENEMIES:
                if bullet.direction == 1 and bullet.rect.colliderect(enemy.hitbox):
                    continue
                if bullet.rect.colliderect(enemy.hitbox):
                    valuables.ENEMIES.remove(enemy)
                    valuables.BULLETS.remove(bullet)
                    for i in range(valuables.COUNT_ENEMIES):
                        enemy = Enemy()
                        enemy.spawn()
                        enemy.shoot()
            if bullet.rect.colliderect(ship.rect):
                running = False
                restart()

        ship.draw(SCREEN)
        clock.tick(FPS)
        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()

def restart():
    intro_text = ['GAME OVER', 'Заново', 'Выйти']
    SCREEN.fill((0, 0, 0))

    font_basic = pygame.font.Font(None, 40)
    font_over = pygame.font.Font(None, 90)
    text_coord = 200
    k = 0

    for line in intro_text:
        string_rendered = font_basic.render(line, 1, pygame.Color('white'))
        string_over = font_over.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        if k == 0:
            intro_rect.x = 15
            text_coord += 20
        elif k == 1:
            intro_rect.x = 150
            text_coord += 100
        else:
            text_coord += 40
            intro_rect.x = 150
        k += 1
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        if k - 1 == 0:
            SCREEN.blit(string_over, intro_rect)
        else:
            SCREEN.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 150 < event.pos[0] < 370 and 350 < event.pos[1] < 380:
                    valuables.ENEMIES = []
                    valuables.BULLETS = []
                    game()
                elif 150 < event.pos[0] < 270 and 420 < event.pos[1] < 440:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


mainn()