import pygame
import random
import valuables
from bullet import Bullet


class Enemy:
    def __init__(self):
        if len(valuables.ENEMIES) != 0:
            allowed = False
            for enemy in valuables.ENEMIES:
                while not allowed:
                    new_coord_y = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
                    new_coord_x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
                    new_coords = pygame.Rect(new_coord_x, new_coord_y,
                                valuables.WIDTH_OF_OBJECT - 2,
                                valuables.HEIGHT_OF_OBJECT - 2)
                    if not enemy.hitbox.colliderect(new_coords):
                        self.x = new_coord_x
                        self.y = new_coord_y
                        allowed = True
        else:
            self.y = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
            self.x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)

        self.hitbox = pygame.Rect(self.x, self.y,
                                valuables.WIDTH_OF_OBJECT - 2,
                                valuables.HEIGHT_OF_OBJECT - 2)
        self.image = pygame.image.load(random.choice(valuables.ALIENS))
        self.health = 10
        self.damage = 20
        self.scorepoints = 1

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def spawn(self):
        valuables.ENEMIES.append(self)

    def shoot(self):
        valuables.BULLETS.append(Bullet(self.hitbox.x + (valuables.WIDTH_OF_OBJECT / 2),
                                        self.hitbox.y + valuables.HEIGHT_OF_OBJECT, 1, 5, 'enemy'))

class Green(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.health = 30
        self.damage = 10
        self.scorepoints = 2

class Purple(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien2.png')
        self.health = 10
        self.damage = 30
        self.scorepoints = 3

class Box(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien3.png')
        self.health = 80
        self.damage = 5
        self.scorepoints = 5

class Star(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien4.png')
        self.health = 40
        self.damage = 40
        self.scorepoints = 7