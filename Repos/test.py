import pygame
import math

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        #self.ball = pygame.Surface((2, 2)).convert_alpha()
        #self.ball.fill((255, 255, 255))
        self.ball = pygame.image.load("fireball.png")
        self.ball = pygame.transform.rotate(self.ball, self.angle)
        self.speed = 13

    def update(self,hitbox):
        self.hitbox = hitbox
        out_right = self.pos[0] > self.hitbox.right
        out_left = self.pos[0] < self.hitbox.left
        out_bottom = self.pos[1] > self.hitbox.bottom
        out_up = self.pos[1] < self.hitbox.top
        if out_right or out_left:
            self.dir = (self.dir[0] * -1, self.dir[1])
        elif out_bottom or out_up:
            self.dir = (self.dir[0],self.dir[1] * -1)
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)
        
    def draw(self, surf):
        ball_rect = self.ball.get_rect(center = self.pos)
        surf.blit(self.ball, ball_rect)

    #def reflection(self,hitbox):
       #self.hitbox = hitbox
        #out_right = self.pos[0] > self.hitbox.right
        #out_left = self.pos[0] < self.hitbox.left
        #out_bottom = self.pos[1] > self.hitbox.bottom
        #out_up = self.pos[1] < self.hitbox.top
        #if out_right or out_left:
            #self.pos[0] = self.pos[0] * -1
        #elif out_bottom or out_up:
            #self.pos[1] = self.pos[1] * -1
        #else:
            #self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                       #self.pos[1]+self.dir[1]*self.speed)
        #self.ball = pygame.transform.rotate(self.ball, self.angle)

balls = []
pos = (250, 250) #ที่ตำแหน่งฮีโร่
run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(*pos))

    for ball in balls[:]:
        ball.update(hitbox)
        if not window.get_rect().collidepoint(ball.pos):
            ball.update(hitbox)
            ball.draw(window)

    hitbox = pygame.draw.rect(window, (255,255,255), pygame.Rect(25,25,450,450), 2)
    window.fill(0)
    pygame.draw.circle(window, (0, 255, 0), pos, 10)
    for ball in balls:
        ball.draw(window)
    pygame.display.flip()