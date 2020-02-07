import pygame
import valuables


class Bullet:
    def __init__(self, x, y, direction, speed, owner):
        self.hitbox = pygame.Rect(x, y, valuables.DEFAULT_BULLET, valuables.DEFAULT_BULLET)
        if owner == 'ship':
            self.image = pygame.image.load('bullet.png')
        elif owner == 'enemy':
            self.image = pygame.image.load('enemybullet.png')
        self.direction = direction
        self.speed = speed

    def fly(self):
        self.hitbox.y += (self.speed * self.direction)

    def draw(self, window):
        if 0 <= self.hitbox.y <= valuables.HEIGHT:
            window.blit(self.image, (self.hitbox.x, self.hitbox.y))