import random
import pygame
GAME_WIDTH = 1280
GAME_HEIGHT = 720

class GameObjects():
    def __init__(self,xpos,ypos,speed):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed

class PlayerOne(GameObjects):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.ypos -= self.speed
        if keys[pygame.K_s]:
            self.ypos += self.speed

        return self.xpos,self.ypos

class PlayerTwo(GameObjects):
    pass

class Ball(GameObjects):

    def update(self):
        return self.xpos,self.ypos
