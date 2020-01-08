import pygame
import valuables


class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, valuables.DEFAULT_BULLET, valuables.DEFAULT_BULLET)
        self.image = pygame.image.load('bullet.png')
        self.direction = direction
        self.speed = 10

    def fly(self):
        self.rect.y += (self.speed * self.direction)

    def draw(self, window):
        if 0 <= self.rect.y <= valuables.HEIGHT:
            window.blit(self.image, (self.rect.x, self.rect.y))