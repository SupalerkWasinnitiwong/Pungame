import pygame # type: ignore
import random
import math

# Initialize Pygame and the mixer for audio
pygame.init()
pygame.mixer.init()

# Window dimensions
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Star: INTERGALACTIC FRONTIER")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 0, 128)

# Load background image
background = pygame.image.load("background.png")
background_width, background_height = background.get_size()

# Load background music
pygame.mixer.music.load("tutorial.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # Play music indefinitely in a loop

# Game variables
BALL_RADIUS = 10
BALL_SPEED = 13
BALL_DAMAGE = 1
MONSTER_HP = 10
FPS = 60
BACKGROUND_SPEED = 1  # How fast the background pans
WALL_MARGIN = WIDTH // 3

# NPC base class
class NPC():
    def __init__(self, name, type_, hp):
        self.name = name
        self.type = type_
        self.hp = hp

# Hero subclass
class Hero(NPC):
    def __init__(self, name, hp):
        super().__init__(name, "Hero", hp)
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.balls = []
        self.can_shoot = True  #can shoot flag
        self.shots_fired = 0 
        self.shoot_delay = 200  
        self.last_shot_time = 0
        self.shooting = False  #is shooting flag

    def shoot(self, target_x, target_y):
        if self.can_shoot and not self.shooting and len(self.balls) == 0:
            self.shooting = True
            self.shots_fired = 0
            self.last_shot_time = pygame.time.get_ticks()
    def update(self):
        current_time = pygame.time.get_ticks()
        if self.shooting and self.shots_fired < 10:
            if current_time - self.last_shot_time >= self.shoot_delay:
                target_x, target_y = pygame.mouse.get_pos()
                self.fire(target_x, target_y)
                self.last_shot_time = current_time
                self.shots_fired += 1
            if self.shots_fired >= 10:
                self.shooting = False
    def fire(self, target_x, target_y):
        ball = Ball(self.x, self.y - 20, target_x, target_y)
        self.balls.append(ball)

# Monster subclass
class Monster(NPC):
    def __init__(self, name, hp):
        super().__init__(name, "Monster", hp)
        self.x = random.randint(WALL_MARGIN + 60, WIDTH - WALL_MARGIN - 60)
        self.y = random.randint(100, HEIGHT // 2)
        self.width = 60
        self.height = 60

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Ball class
class Ball:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y

        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        self.x_vel = (dx / distance) * BALL_SPEED
        self.y_vel = (dy / distance) * BALL_SPEED

        self.active = True
        self.collision_cooldown = 0

    def move(self):
        if self.active:
            self.x += self.x_vel
            self.y += self.y_vel

            if self.x <= 0 or self.x >= WIDTH:
                self.x_vel *= -1
            if self.x <= WALL_MARGIN + BALL_RADIUS or self.x >= WIDTH - WALL_MARGIN - BALL_RADIUS:
                self.x_vel *= -1
            if self.y <= 0:
                self.y_vel *= -1
            elif self.y >= HEIGHT:
                self.active = False

            if self.collision_cooldown > 0:
                self.collision_cooldown -= 1

    def check_collision(self, monster): #monster is tuple of all monsters and walls
        
        monster_rect = monster.get_rect()
        
        ball_rect = pygame.Rect(self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

        if self.collision_cooldown == 0 and ball_rect.colliderect(monster_rect):
            overlap_left = ball_rect.right - monster_rect.left
            overlap_right = monster_rect.right - ball_rect.left
            overlap_top = ball_rect.bottom - monster_rect.top
            overlap_bottom = monster_rect.bottom - ball_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                self.x = monster_rect.left - BALL_RADIUS
                self.x_vel *= -1
            elif min_overlap == overlap_right:
                self.x = monster_rect.right + BALL_RADIUS
                self.x_vel *= -1
            elif min_overlap == overlap_top:
                self.y = monster_rect.top - BALL_RADIUS
                self.y_vel *= -1
            elif min_overlap == overlap_bottom:
                self.y = monster_rect.bottom + BALL_RADIUS
                self.y_vel *= -1
            monster.take_damage(BALL_DAMAGE)
            self.collision_cooldown = 10
            return True
        return False

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.draw.rect(WIN, (0,255,0), (x, y, width, height))
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    


# Game loop
def main():
    global hero
    hero = Hero("Hero", 10)
    monster = Monster("Monster", MONSTER_HP)
    wall = [Wall(426, 0, 8, 720), Wall(853, 0, 8, 720), Wall(427, 4, 427, 8)]
    clock = pygame.time.Clock()
    running = True


    # Background panning variables
    bg_x = 0
    bg_y = 0
    a =  1280 # Semi-major axis
    b = 720  # Semi-minor axis
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    angle = 59

    while running:
        clock.tick(FPS)

        # Calculate x and y coordinates using parametric equations
        bg_x = center_x + a * math.cos(angle) - background_width/2
        bg_y = center_y + b * math.sin(angle) - background_height/2

        # Increment angle for next frame
        angle += 0.005

        # Draw the background (panning effect)
        WIN.blit(background, (bg_x, bg_y))

        pygame.draw.line(WIN, PURPLE, (WALL_MARGIN, 0), (WALL_MARGIN, HEIGHT), 5)
        pygame.draw.line(WIN, PURPLE, (WIDTH - WALL_MARGIN, 0), (WIDTH - WALL_MARGIN, HEIGHT), 5)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and hero.can_shoot:
                    target_x, target_y = pygame.mouse.get_pos()
                    hero.shoot(target_x, target_y)
        hero.update()

        for ball in hero.balls:
            ball.move()
            if not ball.active:
                hero.balls.remove(ball)
            elif ball.check_collision(monster):
                if monster.is_dead():
                    monster = Monster("Monster", MONSTER_HP)
        if not hero.balls:
            hero.can_shoot = True

        pygame.draw.rect(WIN, BLUE, (hero.x - 25, hero.y, 50, 50))
        pygame.draw.rect(WIN, RED, (monster.x, monster.y, monster.width, monster.height))

        for ball in hero.balls:
            if ball.active:
                pygame.draw.circle(WIN, WHITE, (int(ball.x), int(ball.y)), BALL_RADIUS)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()