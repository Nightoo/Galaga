import pygame, random
from enemy import Enemy
from bullet import Bullet
from spaceship import Spaceship
import valuables
pygame.init()
pygame.time.set_timer(valuables.MYEVENTTYPE, 10)
SIZE = valuables.WIDTH, valuables.HEIGHT
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
FPS = 60
MYEVENTTYPE = 5
ship = Spaceship()

while running:
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and 0 < ship.rect.x < valuables.WIDTH:
                ship.move(-1)
            if event.key == pygame.K_d and 0 <= ship.rect.x < valuables.WIDTH - 50:
                ship.move(1)
            if event.key == pygame.K_SPACE:
                ship.shoot()
            if event.key == pygame.K_e:
                enemy = Enemy()
                enemy.spawn()
                enemy.shoot()
        if event.type == MYEVENTTYPE:
            print(True)

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
