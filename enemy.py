import pygame
import random
import valuables
from bullet import Bullet


class Enemy:
    def __init__(self):
        self.x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
        self.y = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
        if len(valuables.ENEMIES) != 0:
            for enemy in valuables.ENEMIES:
                while enemy.hitbox.x + 50 == self.x or enemy.hitbox.x - 50 == self.x:
                    self.x = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)
                while enemy.hitbox.y + 50 == self.y or enemy.hitbox.y - 50 == self.y:
                    self.y = random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT)

        self.hitbox = pygame.Rect(self.x, self.y,
                                valuables.WIDTH_OF_OBJECT - 2,
                                valuables.HEIGHT_OF_OBJECT - 2)
        self.image = pygame.image.load(random.choice(valuables.ALIENS))

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def spawn(self):
        valuables.ENEMIES.append(self)

    def shoot(self):
        valuables.BULLETS.append(Bullet(self.hitbox.x + (valuables.WIDTH_OF_OBJECT / 2),
                                        self.hitbox.y + valuables.HEIGHT_OF_OBJECT, 1, 5))
