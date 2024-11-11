#import sys
import pygame
import math
#pygame.init()

#pygame.display.set_caption('Ball test')
#screen = pygame.display.set_mode((640,480))

#clock = pygame.time.Clock()


class Ball:
    def __init__ (self, effect, damage, speed, image):
        self.effect = effect
        self.damage = damage
        self.speed = speed
        self.image = image
        self.pos = player.pos
        self.ball = pygame.image.load(self.image)

    def move (self, dir): # dir = tuple
        self.dir = dir
        speedx, speedy = (self.dir[0]*self.speed, self.dir[1]*self.speed)
        self.pos = (self.pos[0] + speedx, self.pos[1] + speedy)

    def reflection(self, hitbox):
        self.hitbox = hitbox
        out_right = self.pos[0] > self.hitbox.right
        out_left = self.pos[0] < self.hitbox.left
        out_bottom = self.pos[1] > self.hitbox.bottom
        out_up = self.pos[1] < self.hitbox.top
        if out_right or out_left:
            self.dir = (self.dir[0] * -1, self.dir[1])
        elif out_bottom or out_up:
            self.dir = (self.dir[0],self.dir[1] * -1)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.ball = pygame.transform.rotate(self.ball, self.angle)

    def draw(self, surf):
        ball_rect = self.ball.get_rect(center = self.pos)
        surf.blit(self.ball, ball_rect)




class normalBall(Ball):
    def __init__(self):
        self.effect = "normal"
        self.damage = 50
        self.speed = 13
        self.image = "Ball.png"

class fireBall(Ball):
    def __init__(self):
        self.effect = "fire"
        self.damage = 50
        self.speed = 13
        self.image = "fireBall.png"

class moodengBall(Ball):
    def __init__(self):
        self.effect = "normal"
        self.damage = 120
        self.speed = 7
        self.image = None


# FOR TESTING
#while True:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #pygame.quit()
            #sys.exit()


    #pygame.display.update()
    #clock.tick(60)      #clock = pygame.time.Clock().tick(60)
    

