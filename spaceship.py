import pygame
import valuables
from bullet import Bullet
import random


class Spaceship:
    def __init__(self):
        self.rect = pygame.Rect(valuables.START_X, valuables.START_Y,
                                valuables.WIDTH_OF_OBJECT, valuables.HEIGHT_OF_OBJECT)
        self.speed = 50
        self.image = pygame.image.load(random.choice(valuables.SPACESHIPS))

    def move(self, direction=1):
        self.rect.x += (self.speed * direction)

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self):
        valuables.BULLETS.append(Bullet(self.rect.x + 45, self.rect.y, -1))
        valuables.BULLETS.append(Bullet(self.rect.x + 5, self.rect.y, -1))