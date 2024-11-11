import pygame
import math
import npc
import ball

class npc:
    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp
    
class Hero(npc):
    def __init__(self, pos, ball_type):
        super().__init__("hero", "player", -1)
        self.pos = pos
        self.ball_type = ball_type
        self.image = "hero.png"
    def ball_shoot(self):
        mx, my = pygame.mouse.get_pos()
        dir = (mx - self.pos[0], my - self.pos[1])
        length = math.hypot(*dir)
        if length == 0.0:
            dir = (0, -1)
        else:
            dir = (dir[0]/length, dir[1]/length)
        return dir

#######################################

class Ball:
    def __init__ (self, effect, damage, speed, image):
        self.effect = effect
        self.damage = damage
        self.speed = speed
        self.image = image
        self.pos = (960, 880)
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
        super().__init__("normal", 50, 13, "Ball.png")

class fireBall(Ball):
    def __init__(self):
        super().__init__("fire", 50, 13, "fireBall.png")
class moodengBall(Ball):
    def __init__(self):
        super().__init__("normal", 120, 7, None)

#######################################

pygame.init()
window = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

balls = []
pos = (960, 880)
ball_type = normalBall()
player = Hero(pos, ball_type)
run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(ball_type)
            
    for ball in balls[:]:
        ball.move(player.ball_shoot())
        if not window.get_rect().collidepoint(ball.pos):
            ball.reflection(hitbox)
            ball.draw(window)

    hitbox = pygame.draw.rect(window, (255,255,255), pygame.Rect(500,25,920,1030), 2)
    window.fill(0)
    #pygame.draw.circle(window, (0, 255, 0), pos, 10)
    for ball in balls:
        ball.draw(window)
    pygame.display.flip()