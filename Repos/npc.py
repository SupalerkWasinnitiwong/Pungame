import pygame
import math

    
class npc(pygame.sprite.Sprite):
    def __init__(self, name, type, hp, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type = type
        self.hp = hp
    
class Hero(npc):
    def __init__(self, pos, ball_type):
        super().__init__("hero", "player", -1, "hero.png")
        self.pos = pos
        self.ball_type = ball_type
    def ball_shoot(self):
        mx, my = pygame.mouse.get_pos()
        dir = (mx - self.pos[0], my - self.pos[1])
        length = math.hypot(*dir)
        if length == 0.0:
            dir = (0, -1)
        else:
            dir = (dir[0]/length, dir[1]/length)
        return dir

class monster(npc):
    def __init__(self, hp, image, pos):
        super().__init__("hero", "player", -1, "hero.png")
        self.hp = hp
        self.image = image
        self.pos = pos
        self.monster = pygame.image.load(self.image)
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            #die

class Minion1(monster):
    def __init__(self):
        super().__init__(hp = 750, image = "minion1.png")

class Minion1(monster):
    def __init__(self):
        super().__init__(hp = 1250, image = "minion2.png")

class Minion1(monster):
    def __init__(self):
        super().__init__(hp = 5000, image = "minion3.png")

class Boss(monster):
    def __init__(self):
        super().__init__(hp = 20000, image = "boss.png")

class Moodeng(monster):
    def __init__(self):
        super().__init__(hp = 50000, image = "moodeng.png")

