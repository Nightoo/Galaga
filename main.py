import pygame, random
from enemy import Enemy
from bullet import Bullet
from spaceship import Spaceship
import valuables
pygame.init()
MYEVENTSPAWN = 10
MYEVENTSHOOT = 11
pygame.time.set_timer(MYEVENTSPAWN, valuables.ENEMYRESPAWNTIME)
pygame.time.set_timer(MYEVENTSHOOT, valuables.ENEMYSHOOTTIME)
SIZE = valuables.WIDTH, valuables.HEIGHT
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
FPS = 60
ship = Spaceship()

while running:
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()
        if event.type == MYEVENTSPAWN:
            enemy = Enemy()
            enemy.spawn()
            enemy.shoot()

        if event.type == MYEVENTSHOOT:
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
            print('LOSE')

    ship.draw(SCREEN)
    clock.tick(FPS)
    pygame.display.flip()
