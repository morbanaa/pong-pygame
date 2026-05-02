import random

class GameObjects():
    def __init__(self,xpos,ypos,speed):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed

class PlayerOne(GameObjects):
    pass

class PlayerTwo(GameObjects):
    pass

class Ball(GameObjects):
    def __init__(self,xpos,ypos,speed,direction,angle):
        super().__init__(xpos,ypos,speed)
        self.direction = direction
        self.angle = angle

    def update(self):
        if self.direction == 1:
            self.xpos -= self.speed
        elif self.direction == 2:
            self.xpos += self.speed

        if self.direction == 1:
            self.ypos -= self.angle
        elif self.direction == 2:
            self.ypos += self.angle
        

        return self.xpos,self.ypos
