import pygame
import valuables


class Bullet:
    def __init__(self, x, y, direction, speed, owner):
        self.rect = pygame.Rect(x, y, valuables.DEFAULT_BULLET, valuables.DEFAULT_BULLET)
        if owner == 'ship':
            self.image = pygame.image.load('bullet.png')
        elif owner == 'enemy':
            self.image = pygame.image.load('enemybullet.png')
        self.direction = direction
        self.speed = speed

    def fly(self):
        self.rect.y += (self.speed * self.direction)

    def draw(self, window):
        if 0 <= self.rect.y <= valuables.HEIGHT:
            window.blit(self.image, (self.rect.x, self.rect.y))