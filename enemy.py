import pygame
import random
import valuables
from bullet import Bullet


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, valuables.WIDTH - valuables.WIDTH_OF_OBJECT),
                                random.randint(100, valuables.HEIGHT - 400),
                                valuables.WIDTH_OF_OBJECT,
                                valuables.HEIGHT_OF_OBJECT)
        self.image = pygame.image.load(random.choice(valuables.ALIENS))

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def spawn(self):
        valuables.ENEMIES.append(self)

    def shoot(self):
        valuables.BULLETS.append(Bullet(self.rect.x + (valuables.WIDTH_OF_OBJECT / 2),
                                        self.rect.y + valuables.HEIGHT_OF_OBJECT, 1))
