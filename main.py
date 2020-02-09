import pygame
import random
import sys
from enemy import Enemy, Green, Purple, Box, Star
from spaceship import Spaceship
import valuables
pygame.init()
pygame.time.set_timer(valuables.EVENTSPAWN, valuables.ENEMYRESPAWNTIME)
SIZE = valuables.WIDTH, valuables.HEIGHT
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 60
ship = Spaceship()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.4)
font_basic = pygame.font.Font(None, 40)


def main():
    intro_text = ['Start', 'Exit']
    SCREEN.fill((0, 0, 0))

    global font_basic
    text_coord = 200
    text_coords_factor = 0

    for line in intro_text:
        string_rendered = font_basic.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        if text_coords_factor == 0:
            intro_rect.x = 120
            text_coord += 80
        elif text_coords_factor == 1:
            intro_rect.x = 120
            text_coord += 40
        else:
            text_coord += 40
            intro_rect.x = 150
            text_coords_factor += 1
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        SCREEN.blit(string_rendered, intro_rect)
    rules_coord = 400
    text = ['A to move left', 'D to move right', 'Space to shoot']
    for line in text:
        string_rendered = font_basic.render(line, 1, pygame.Color('yellow'))
        SCREEN.blit(string_rendered, (50, rules_coord))
        rules_coord += 35

    while True:
        startscreen = pygame.image.load('startscreen.png')
        SCREEN.blit(startscreen, (50, 500))
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
        for i in range(10):
            star_x = random.randint(0, 400)
            star_y = random.randint(0, 800)
            pygame.draw.circle(SCREEN, (255, 255, 255), (star_x, star_y), 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
            if event.type == valuables.EVENTSPAWN or len(valuables.ENEMIES) == 0:
                if len(valuables.ENEMIES) <= ((valuables.HEIGHT // 2 * valuables.WIDTH) //
                                              (valuables.HEIGHT_OF_OBJECT * valuables.WIDTH_OF_OBJECT) // 2):
                    pick = random.randint(1, 4)
                    if pick == 1:
                        enemy = Green()
                    elif pick == 2:
                        enemy = Purple()
                    elif pick == 3:
                        enemy = Box()
                    elif pick == 4:
                        enemy = Star()
                    enemy.spawn()
                    enemy.shoot()

        keystate = pygame.key.get_pressed()
        ship.speed = 0
        if keystate[pygame.K_a] and ship.hitbox.x > 0:
            ship.speed = -8
        if keystate[pygame.K_d] and ship.hitbox.x + 50 < valuables.WIDTH:
            ship.speed = 8
        ship.hitbox.x += ship.speed

        for enemy in valuables.ENEMIES:
            enemy.draw(SCREEN)

        for bullet in valuables.BULLETS:
            bullet.fly()
            bullet.draw(SCREEN)

        if len(valuables.ENEMIES) > 0:
            # 1000 and 100 are correct amount of ms
            if pygame.time.get_ticks() % (1000 // len(valuables.ENEMIES) + 1) == 0:
                (valuables.ENEMIES[random.randint(0, len(valuables.ENEMIES) - 1)]).shoot()
        elif len(valuables.ENEMIES) > ((valuables.HEIGHT // 2 * valuables.WIDTH) //
                                        (valuables.HEIGHT_OF_OBJECT * valuables.WIDTH_OF_OBJECT) // 6):
            if pygame.time.get_ticks() % (10 // len(valuables.ENEMIES) + 1) == 0:
                (valuables.ENEMIES[random.randint(0, len(valuables.ENEMIES) - 1)]).shoot()

        for enemy in valuables.ENEMIES:
            if pygame.time.get_ticks() % enemy.delay == 0:
                enemy.shoot()
            if enemy.health <= 0:
                valuables.ENEMIES.remove(enemy)
                ship.health += 1
                pick = random.randint(1, 4)
                if pick == 1:
                    enemy = Green()
                elif pick == 2:
                    enemy = Purple()
                elif pick == 3:
                    enemy = Box()
                elif pick == 4:
                    enemy = Star()
                if len(valuables.ENEMIES) <= ((valuables.HEIGHT // 2 * valuables.WIDTH) //
                                              (valuables.HEIGHT_OF_OBJECT * valuables.WIDTH_OF_OBJECT) // 2):
                    enemy.spawn()
                    enemy.shoot()
                    valuables.SCORE += enemy.scorepoints

        for bullet in valuables.BULLETS:
            for enemy in valuables.ENEMIES:
                if bullet.hitbox.colliderect(enemy.hitbox) and bullet.direction == -1:
                    enemy.health -= ship.damage
                    if bullet not in valuables.BULLETS:
                        continue
                    else:
                        valuables.BULLETS.remove(bullet)

                if bullet.hitbox.colliderect(ship.hitbox):
                    if bullet not in valuables.BULLETS:
                        continue
                    else:
                        valuables.BULLETS.remove(bullet)
                    ship.health -= enemy.damage
                    if ship.health <= 0:
                        running = False
                        restart()

        scoreboard = 'Score:' + str(valuables.SCORE)
        scoreboard_rendered = font_basic.render(scoreboard, 1, pygame.Color('green'))
        scoreboard_x = 10
        scoreboard_y = valuables.HEIGHT - scoreboard_rendered.get_height()
        SCREEN.blit(scoreboard_rendered, (scoreboard_x, scoreboard_y))

        healthbar = 'Health:' + str(ship.health)
        healthbar_rendered = font_basic.render(healthbar, 1, pygame.Color('green'))
        healthbar_x = valuables.WIDTH // 2
        healthbar_y = valuables.HEIGHT - healthbar_rendered.get_height()
        SCREEN.blit(healthbar_rendered, (healthbar_x, healthbar_y))

        ship.draw(SCREEN)
        clock.tick(FPS)
        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()


def restart():
    intro_text = ['GAME OVER', 'Restart', 'Exit']
    SCREEN.fill((0, 0, 0))
    endscreen = pygame.image.load('endscreen.png')
    SCREEN.blit(endscreen, (50, 500))

    global font_basic
    font_over = pygame.font.Font(None, 90)
    text_coord = 200
    text_coords_factor = 0

    for line in intro_text:
        string_rendered = font_basic.render(line, 1, pygame.Color('white'))
        string_over = font_over.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        if text_coords_factor == 0:
            intro_rect.x = 15
            text_coord += 20
        elif text_coords_factor == 1:
            intro_rect.x = 150
            text_coord += 100
        else:
            text_coord += 40
            intro_rect.x = 150
            text_coords_factor += 1
        intro_rect.top = text_coord
        text_coord += intro_rect.height
        if text_coords_factor - 1 == 0:
            SCREEN.blit(string_over, intro_rect)
        else:
            SCREEN.blit(string_rendered, intro_rect)

        scoreboard = 'Your score:' + str(valuables.SCORE)
        scoreboard_rendered = font_basic.render(scoreboard, 1, pygame.Color('white'))
        scoreboard_x = 150
        scoreboard_y = 500 - scoreboard_rendered.get_height()
        SCREEN.blit(scoreboard_rendered, (scoreboard_x, scoreboard_y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 150 < event.pos[0] < 370 and 350 < event.pos[1] < 380:
                    valuables.ENEMIES = []
                    valuables.BULLETS = []
                    valuables.SCORE = 0
                    ship.health = 100
                    game()
                elif 150 < event.pos[0] < 270 and 420 < event.pos[1] < 440:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


main()
