import pygame
import valuables
from bullet import Bullet
import random


class Spaceship:
    def __init__(self):
        self.hitbox = pygame.Rect(valuables.START_X, valuables.START_Y,
                                valuables.WIDTH_OF_OBJECT - 2, valuables.HEIGHT_OF_OBJECT - 2)
        self.speed = 0
        self.image = pygame.image.load(random.choice(valuables.SPACESHIPS))
        self.health = 100
        self.damage = 20

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def shoot(self):
        valuables.BULLETS.append(Bullet(self.hitbox.x + 45, self.hitbox.y, -1, 10, 'ship'))
        valuables.BULLETS.append(Bullet(self.hitbox.x + 5, self.hitbox.y, -1, 10, 'ship'))
        pygame.mixer.Sound('LAZER.wav').play()
