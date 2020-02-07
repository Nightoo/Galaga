import pygame
import random
import valuables
from bullet import Bullet


class Enemy:
    def __init__(self):
        self.allowed = False
        if len(valuables.ENEMIES) != 0:
            attempts = 0
            while not self.allowed:
                new_coord_y = random.randint(0, valuables.HEIGHT // 2)
                new_coord_x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
                new_coords = pygame.Rect(new_coord_x, new_coord_y,
                                            valuables.WIDTH_OF_OBJECT,
                                            valuables.HEIGHT_OF_OBJECT)
                while self.is_ok(new_coords):
                    self.x = new_coord_x
                    self.y = new_coord_y
                    self.allowed = True
                    break
                attempts += 1
                if attempts == 10:
                    self.x = -100
                    self.y = -100
                    break
        else:
            self.y = random.randint(0, valuables.HEIGHT // 2)
            self.x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)

        self.hitbox = pygame.Rect(self.x, self.y,
                                valuables.WIDTH_OF_OBJECT,
                                valuables.HEIGHT_OF_OBJECT)
        self.image = pygame.image.load(random.choice(valuables.ALIENS))
        self.health = 10
        self.damage = 20
        self.bullet_speed = 0
        self.scorepoints = 1
        self.delay = 0

    def is_ok(self, rect):
        for enemy in valuables.ENEMIES:
            if enemy.hitbox.colliderect(rect):
                return False
        return True

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def spawn(self):
        if self.allowed is True or len(valuables.ENEMIES) == 0:
            valuables.ENEMIES.append(self)

    def shoot(self):
        #1 means that enemy shoots towards the spaceship
        valuables.BULLETS.append(Bullet(self.hitbox.x + (valuables.WIDTH_OF_OBJECT / 2),
                                        self.hitbox.y + valuables.HEIGHT_OF_OBJECT, 1, self.bullet_speed, 'enemy'))

class Green(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.health = 30
        self.damage = 5
        self.scorepoints = 2
        self.bullet_speed = 4
        self.delay = 51

class Purple(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien2.png')
        self.health = 10
        self.damage = 5
        self.scorepoints = 3
        self.bullet_speed = 5
        self.delay = 67


class Box(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien3.png')
        self.health = 80
        self.damage = 5
        self.scorepoints = 5
        self.bullet_speed = 8
        self.delay = 74


class Star(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien4.png')
        self.health = 40
        self.damage = 5
        self.scorepoints = 7
        self.bullet_speed = 2
        self.delay = 81
