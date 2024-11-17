import pygame
import sys
import random
import math

# Global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



class MainMenu:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Shooting Star: INTERGALACTIC FRONTIER")
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Load assets
        self.background = pygame.image.load(r"background.png")
        self.background = pygame.transform.scale(self.background, (3840, 2160))
        self.background_width, self.background_height = self.background.get_size()

        self.logo = pygame.image.load("logo.png")

        # Buttons
        self.play_button_1 = pygame.image.load("play1.png")
        self.play_button_1 = pygame.transform.scale(self.play_button_1, (300, 120))
        self.play_button_2 = pygame.image.load("play2.png")
        self.play_button_2 = pygame.transform.scale(self.play_button_2, (300, 120))
        self.play_button_1_rect = self.play_button_1.get_rect()

        self.shop_button_1 = pygame.image.load("shop1.png")
        self.shop_button_1 = pygame.transform.scale(self.shop_button_1, (300, 120))
        self.shop_button_2 = pygame.image.load("shop2.png")
        self.shop_button_2 = pygame.transform.scale(self.shop_button_2, (300, 120))
        self.shop_button_1_rect = self.shop_button_1.get_rect()

        self.sound_button_1 = pygame.image.load("volume.png")
        self.sound_button_1 = pygame.transform.scale(self.sound_button_1, (80, 80))
        self.sound_button_2 = pygame.image.load("mute.png")
        self.sound_button_2 = pygame.transform.scale(self.sound_button_2, (80, 80))
        self.sound_button_1_rect = self.sound_button_1.get_rect()

        self.exit_button_1 = pygame.image.load("exit1.png")
        self.exit_button_1 = pygame.transform.scale(self.exit_button_1, (300, 120))
        self.exit_button_2 = pygame.image.load("exit2.png")
        self.exit_button_2 = pygame.transform.scale(self.exit_button_2, (300, 120))
        self.exit_button_1_rect = self.exit_button_1.get_rect()
        
        #self.exit_button_1 = pygame.image.load("restart1.png")
        #self.exit_button_1 = pygame.transform.scale(self.exit_button_1, (360, 90))
        #self.exit_button_2 = pygame.image.load("restart2.png")
        #self.exit_button_2 = pygame.transform.scale(self.exit_button_2, (360, 9))
        #self.exit_button_1_rect = self.exit_button_1.get_rect()

        pygame.mixer.music.load(r"Null Point.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        self.sound_on = True

        # Background
        self.center_x, self.center_y = self.screen.get_size()[0] / 2, self.screen.get_size()[1] / 2
        self.a, self.b = 800, 600
        self.angle = 60
        self.BACKGROUND_SPEED = 0.001

        self.main_menu()

    def update_background(self):
        self.bg_x = self.center_x + self.a * math.cos(self.angle) - self.background_width / 2
        self.bg_y = self.center_y + self.b * math.sin(self.angle) - self.background_height / 2
        self.angle += 0.0001
        self.angle += self.BACKGROUND_SPEED

    def main_menu(self):
        running = True
        while running:
            self.clock.tick(self.FPS)
            self.update_background()
            play_button_rect = pygame.Rect(self.WIDTH // 2 - self.play_button_1.get_width() // 2, 300, 300, 100)
            shop_button_rect = pygame.Rect(self.WIDTH // 2 - self.shop_button_1.get_width() // 2, 300 + self.play_button_1.get_height() + 10, 300, 100)
            exit_button_rect = pygame.Rect(self.WIDTH // 2 - self.exit_button_1.get_width() // 2, 300 + self.play_button_1.get_height() + self.shop_button_1.get_height() + 20, 300, 100)
            sound_button_rect = pygame.Rect(10, self.HEIGHT - self.sound_button_1.get_height() - 10, 300, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("Mean Meteor.mp3")
                        pygame.mixer.music.set_volume(0.4)
                        pygame.mixer.music.play(-1)
                        GameLoop().run_game()  # Start the game loop
                        running = False  # Exit the menu
                    elif shop_button_rect.collidepoint(event.pos):
                        pass
                    elif exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif sound_button_rect.collidepoint(event.pos):
                        if self.sound_on:
                            pygame.mixer.music.pause()
                            self.screen.blit(self.sound_button_2, sound_button_rect.topleft)
                        else:
                            pygame.mixer.music.unpause()
                            self.screen.blit(self.sound_button_1, sound_button_rect.topleft)
                        self.sound_on = not self.sound_on
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (self.bg_x, self.bg_y))
            logo_rect = self.logo.get_rect(center=(self.WIDTH // 2, 150))
            self.screen.blit(self.logo, logo_rect)
            if self.sound_on:
                self.screen.blit(self.sound_button_1, sound_button_rect.topleft)
            else:
                self.screen.blit(self.sound_button_2, sound_button_rect.topleft)
            # buttons
            mouse_pos = pygame.mouse.get_pos()
            self.ALL_buttons = [play_button_rect, shop_button_rect, sound_button_rect, exit_button_rect]
            for button in self.ALL_buttons:
                if button.collidepoint(mouse_pos):
                    if button == play_button_rect:
                        self.screen.blit(self.play_button_2, play_button_rect.topleft)
                    elif button == shop_button_rect:
                        self.screen.blit(self.shop_button_2, shop_button_rect.topleft)
                    elif button == exit_button_rect:
                        self.screen.blit(self.exit_button_2, exit_button_rect.topleft)
                else:
                    if button == play_button_rect:
                        self.screen.blit(self.play_button_1, play_button_rect.topleft)
                    elif button == shop_button_rect:
                        self.screen.blit(self.shop_button_1, shop_button_rect.topleft)
                    elif button == exit_button_rect:
                        self.screen.blit(self.exit_button_1, exit_button_rect.topleft)

            pygame.display.flip()

class GameLoop:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1280, 720
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Shooting Star: INTERGALACTIC FRONTIER")
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Load assets
        self.background = pygame.image.load("background.png")
        self.background_width, self.background_height = self.background.get_size()
        self.wallside_texture = pygame.image.load("wall_side.png")
        self.walltop_texture = pygame.image.load("wall_top.png")
        self.wallblock_texture = "wall.png"
        self.multiplier_texture = "multiplier.png"
        self.multiplier_inactive_texture = "multiplier_inactive.png"
        self.floor_texture = pygame.image.load("floor.png")
        self.hero_texture = pygame.image.load("hero.png")
        self.monster_texture = "monster.png"
        self.monster_medium_texture = "monster_medium.png"
        self.monster_hard_texture = "monster_hard.png"
        self.monster_boss_texture = "monster_boss.png"
        self.monster_moodeng_texture = "monster_moodeng.png"
        self.ball_texture = pygame.image.load("ball.png")

        self.restart_button_1 = pygame.image.load("Restart 1.png")
        self.restart_button_2 = pygame.image.load("Restart 2.png")


        # Initialize game entities
        self.hero = Hero("Hero", 10, self.hero_texture)
        self.monster = Monster("Monster", 10, self.monster_texture)

        self.wall_list = pygame.sprite.Group()
        self.rock_list = pygame.sprite.Group()
        self.multiplier_list = pygame.sprite.Group()

        self.wave = {"tutorial" : 2, "wave 1" : 5, "wave 2" : 3, "BOSS" : 1, "MOODENG" : 1}
        self.wave_state = "tutorial"

        for i in range(7):
            wall = Wallblock(self.wallblock_texture)
            self.wall_list.add(wall)

        for i in range(2):
            multiplier = Multiplier(self.multiplier_texture)
            self.multiplier_list.add(multiplier)


    def run_game(self):
        running = True
        a = 1280  # Semi-major axis
        b = 720  # Semi-minor axis
        center_x = self.WIDTH // 2
        center_y = self.HEIGHT // 2
        angle = 59

        while running:
            self.clock.tick(self.FPS)

            # Calculate background movement
            bg_x = center_x + a * math.cos(angle) - self.background_width / 2
            bg_y = center_y + b * math.sin(angle) - self.background_height / 2
            angle += 0.001

            # Draw background
            self.WIN.blit(self.background, (bg_x, bg_y))
            self.WIN.blit(self.wallside_texture, (370, 30))  # Left wall texture
            self.WIN.blit(self.wallside_texture, (850, 30))  # Right wall texture
            self.WIN.blit(self.floor_texture, (430, 120))
            self.WIN.blit(self.walltop_texture, (430, 30))  # Top wall texture

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.hero.can_shoot and not restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                        target_x, target_y = pygame.mouse.get_pos()
                        self.hero.shoot(target_x, target_y, self.ball_texture)
                        self.monster.movetile = True       # monster ready to move next turn
                    if event.button == 1 and restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                        for ball in self.hero.balls:
                            self.hero.balls.remove(ball)

            self.hero.update()
            self.rock_list.update()


            # remove objects
            for wall in self.wall_list:
                if wall.x == self.monster.x and wall.y == self.monster.y:
                    self.wall_list.remove(wall)
                    new_wall = Wallblock(self.wallblock_texture)
                    self.wall_list.add(new_wall)
                for multiplier in self.multiplier_list:
                    if wall.x == multiplier.x and wall.y == multiplier.y:
                        self.wall_list.remove(wall)
                        new_wall = Wallblock(self.wallblock_texture)
                        self.wall_list.add(new_wall)
            for multiplier in self.multiplier_list:
                if multiplier.x == self.monster.x and multiplier.y == self.monster.y:
                    self.multiplier_list.remove(multiplier)
                    new_multiplier = Multiplier(self.multiplier_texture)
                    self.multiplier_list.add(new_multiplier)

            for ball in self.hero.balls:
                ball.move()
                if not ball.active:
                    self.hero.balls.remove(ball)
                elif ball.check_collision(self.monster):
                    if self.monster.is_dead():
                        for i in range(13):
                            # construct 13 blocks
                            rock = Rock()

                            # construct on mouse position
                            rock.rect.x = self.monster.x
                            rock.rect.y = self.monster.y

                            # sort them into block_list
                            self.rock_list.add(rock)

                        self.monster.y = 5000      # hide the monster far away
                        self.wave[self.wave_state] -= 1
                        if self.wave[self.wave_state] > 0 and self.wave_state == "tutorial":
                            self.monster = Monster("Monster", 10, self.monster_texture)
                        if self.wave[self.wave_state] > 0 and self.wave_state == "wave 1":
                            self.monster = Monster("Monster", 20, self.monster_medium_texture)
                        if self.wave[self.wave_state] > 0 and self.wave_state == "wave 2":
                            self.monster = Monster("Monster", 50, self.monster_hard_texture)
                
                for multiplier in self.multiplier_list:
                    ball_rect = ball.get_rect()
                    multiplier_rect = multiplier.rect
                    if len(self.hero.balls) == 0 and multiplier.active == False:
                        multiplier.image = pygame.image.load("multiplier.png")
                        multiplier.active = True

                    if ball_rect.colliderect(multiplier_rect) and multiplier.active == True:
                        # Create new ball with slightly modified velocity
                        for i in range(multiplier.multiply):
                            dx = ball.x_vel + random.uniform(-50,50)
                            dy = ball.y_vel + random.uniform(-50,50)
                            new_ball = Ball(ball.x, ball.y, dx, dy, self.ball_texture)
                            self.hero.balls.append(new_ball)
                        multiplier.image = pygame.image.load("multiplier_inactive.png")
                        multiplier.active = False


                for wall in self.wall_list:
                    # Calculate the edges of both objects
                    ball_left = ball.x
                    ball_right = ball.x + ball.width
                    ball_top = ball.y
                    ball_bottom = ball.y + ball.height
                    
                    wall_left = wall.x
                    wall_right = wall.x + wall.width
                    wall_top = wall.y
                    wall_bottom = wall.y + wall.height
                    
                    # Check if there's a collision
                    if (ball_right > wall_left and 
                        ball_left < wall_right and 
                        ball_bottom > wall_top and 
                        ball_top < wall_bottom):
                        
                        # Calculate overlap on each axis
                        overlap_left = ball_right - wall_left
                        overlap_right = wall_right - ball_left
                        overlap_top = ball_bottom - wall_top
                        overlap_bottom = wall_bottom - ball_top
                        
                        # Find smallest overlap to determine collision side
                        min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                        
                        if min_overlap == overlap_left or min_overlap == overlap_right:
                            # Horizontal collision
                            ball.x_vel *= -1
                            if min_overlap == overlap_left:
                                ball.x = wall_left - ball.width  # Move ball to left of wall
                            else:
                                ball.x = wall_right  # Move ball to right of wall
                        else:
                            # Vertical collision
                            ball.y_vel *= -1
                            if min_overlap == overlap_top:
                                ball.y = wall_top - ball.height  # Move ball above wall
                            else:
                                ball.y = wall_bottom  # Move ball below wall

            # monster moves each turn
            if len(self.hero.balls) == 0 and self.monster.movetile == True:
                grid = (random.randint(0, 6), random.randint(0, 7))
                self.monster.x = grid[0]*60 + 430
                self.monster.y = grid[1]*60 + 120
                self.monster.movetile = False

            # WAVE CHANGE STATE
            if len(self.hero.balls) == 0 and self.wave_state == "tutorial" and self.wave[self.wave_state] == 0:

                self.wave_state = "wave 1"
                self.monster = Monster("Monster", 20, self.monster_medium_texture)

                self.wall_list = pygame.sprite.Group()
                self.multiplier_list = pygame.sprite.Group()
                for i in range(7):
                    wall = Wallblock(self.wallblock_texture)
                    self.wall_list.add(wall)

                for i in range(2):
                    multiplier = Multiplier(self.multiplier_texture)
                    self.multiplier_list.add(multiplier)

            if len(self.hero.balls) == 0 and self.wave_state == "wave 1" and self.wave[self.wave_state] == 0:

                self.wave_state = "wave 2"
                self.monster = Monster("Monster", 50, self.monster_hard_texture)

                self.wall_list = pygame.sprite.Group()
                self.multiplier_list = pygame.sprite.Group()
                for i in range(6):
                    wall = Wallblock(self.wallblock_texture)
                    self.wall_list.add(wall)
                    

                for i in range(3):
                    multiplier = Multiplier(self.multiplier_texture)
                    self.multiplier_list.add(multiplier)

            if len(self.hero.balls) == 0 and self.wave_state == "wave 2" and self.wave[self.wave_state] == 0:

                pygame.mixer.music.stop()
                pygame.mixer.music.load("Mean Meteor.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                self.wave_state = "BOSS"
                self.monster = Monster("Monster", 500, self.monster_boss_texture)

                self.wall_list = pygame.sprite.Group()
                self.multiplier_list = pygame.sprite.Group()
                for i in range(9):
                    wall = Wallblock(self.wallblock_texture)
                    self.wall_list.add(wall)

                for i in range(4):
                    multiplier = Multiplier(self.multiplier_texture)
                    self.multiplier_list.add(multiplier)

            if len(self.hero.balls) == 0 and self.wave_state == "BOSS" and self.wave[self.wave_state] == 0:

                pygame.mixer.music.stop()
                pygame.mixer.music.load("Sunny-side Supernova (PYGAME FINAL PROJECT BOSS OST- PROPERTY OF W.THIRABORWORNSAKUL).mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                self.wave_state = "MOODENG"
                self.monster = Monster("Monster", 2000, self.monster_moodeng_texture)

                self.wall_list = pygame.sprite.Group()
                self.multiplier_list = pygame.sprite.Group()
                for i in range(9):
                    wall = Wallblock(self.wallblock_texture)
                    self.wall_list.add(wall)

                for i in range(24):
                    multiplier = Multiplier(self.multiplier_texture)
                    self.multiplier_list.add(multiplier)
            if len(self.hero.balls) == 0 and self.wave_state == "MOODENG" and self.wave[self.wave_state] == 0:

                pygame.quit()   # เดี๋ยวใส่เครดิต


            if not self.hero.balls:
                self.hero.can_shoot = True

            # Draw hero, monster, and balls
            hero_rect = self.hero.get_rect()
            self.WIN.blit(self.hero_texture, hero_rect.topleft)
            monster_rect = self.monster.get_rect()
            self.WIN.blit(self.monster.image, monster_rect.topleft)
            self.wall_list.draw(self.WIN)
            self.rock_list.draw(self.WIN)
            self.multiplier_list.draw(self.WIN)
            print(len(self.hero.balls))

            for ball in self.hero.balls:
                if ball.active:
                    ball_rect = ball.get_rect()
                    self.WIN.blit(self.ball_texture, ball_rect.topleft)

            # UI

            font = pygame.font.SysFont('Arial', 32)

            # enemy hp
            hp_text = font.render(str(self.monster.hp), True, (255, 255, 255))  # (text, anti-aliasing, color)
            hp_text_rect = hp_text.get_rect(center=(self.monster.x + 30, self.monster.y + 20))  # Center of monster
            self.WIN.blit(hp_text, hp_text_rect)

            # multiplier
            for multiplier in self.multiplier_list:
                multiplier_text = font.render(str(multiplier.multiply), True, (255, 255, 255))  # (text, anti-aliasing, color)
                multiplier_text_rect = multiplier_text.get_rect(center=(multiplier.x + 30, multiplier.y + 20))  # Center of multiplier
                self.WIN.blit(multiplier_text, multiplier_text_rect)

            # wave count and enemy count
            wave_state_text = font.render(str(self.wave_state), True, (255, 255, 255))  # (text, anti-aliasing, color)
            wave_state_text_rect = wave_state_text.get_rect(center=(self.WIDTH - 200, 100))  # Center of monster
            self.WIN.blit(wave_state_text, wave_state_text_rect)

            wave_count_text = font.render("x" + str(self.wave[self.wave_state]), True, (255, 255, 255))  # (text, anti-aliasing, color)
            wave_count_text_rect = wave_count_text.get_rect(center=(self.WIDTH - 100, self.HEIGHT - 100))  # Center of monster
            self.WIN.blit(wave_count_text, wave_count_text_rect)

            # enemy icon
            enemy_icon = self.monster.image
            enemy_icon = pygame.transform.scale(enemy_icon, (120, 120))
            enemy_icon_rect = enemy_icon.get_rect(center=(wave_count_text_rect.x - 130, wave_count_text_rect.y))
            self.WIN.blit(enemy_icon, enemy_icon_rect)

            # restart button

            restart_button_rect = pygame.Rect(30, self.HEIGHT - 30 - self.restart_button_1.get_height(), self.restart_button_1.get_width(), self.restart_button_1.get_height())
            if restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.WIN.blit(self.restart_button_2, restart_button_rect.topleft)
            else:
                self.WIN.blit(self.restart_button_1, restart_button_rect.topleft)

            pygame.display.flip()

        pygame.quit()

# NPC base class
class NPC(pygame.sprite.Sprite):
    def __init__(self, name, type_, hp):
        super().__init__()
        self.name = name
        self.type = type_
        self.hp = hp

# Hero subclass
class Hero(NPC):
    def __init__(self, name, hp, texture):
        super().__init__(name, "Hero", hp)
        self.width = texture.get_width()
        self.height = texture.get_height()
        self.x = (1280 // 2) - (self.width//2)
        self.y = 720 - self.height
        self.texture = texture
        self.balls = []
        self.can_shoot = True
        self.shots_fired = 0
        self.shoot_delay = 200
        self.last_shot_time = 0
        self.shooting = False

    def shoot(self, target_x, target_y, texture):
        if self.can_shoot and not self.shooting and len(self.balls) == 0:
            self.shooting = True
            self.shots_fired = 0
            self.last_shot_time = pygame.time.get_ticks()
            self.fire(target_x, target_y, texture)

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.shooting and self.shots_fired < 10:
            if current_time - self.last_shot_time >= self.shoot_delay:
                target_x, target_y = pygame.mouse.get_pos()
                self.fire(target_x, target_y, self.balls[0].texture)
                self.last_shot_time = current_time
                self.shots_fired += 1
            if self.shots_fired >= 10:
                self.shooting = False

    def fire(self, target_x, target_y, texture):
        ball = Ball(self.x, self.y - 20, target_x, target_y, texture)
        self.balls.append(ball)
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

'''
    monsters position is determined by grid [7x8]
    (0,0)(1,0)(2,0)(3,0)(4,0)(5,0)(6,0)
    (0,1)(1,1)(2,1)(3,1)(4,1)(5,1)(6,1)
    (0,2)(1,2)(2,2)(3,2)(4,2)(5,2)(6,2)
    (0,3)(1,3)(2,3)(3,3)(4,3)(5,3)(6,3)
    (0,4)(1,4)(2,4)(3,4)(4,4)(5,4)(6,4)
    (0,5)(1,5)(2,5)(3,5)(4,5)(5,5)(6,5)
    (0,6)(1,6)(2,6)(3,6)(4,6)(5,6)(6,6)
    (0,7)(1,7)(2,7)(3,7)(4,7)(5,7)(6,7)

    Formula: (x*60)+430, (y*60)+120
'''
# Monster subclass
class Monster(NPC):
    def __init__(self, name, hp, texture):
        super().__init__(name, "Monster", hp)
        self.texture = texture
        self.image = pygame.image.load(self.texture)
        grid = (random.randint(0, 6), random.randint(0, 7))
        self.x = grid[0]*60 + 430
        self.y = grid[1]*60 + 120
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.movetile = True

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, texture):
        super().__init__()
        self.x = x + 30
        self.y = y
        self.texture = texture
        self.width = texture.get_width()
        self.height = texture.get_height()

        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        self.x_vel = (dx / distance) * 13
        self.y_vel = (dy / distance) * 13

        self.active = True
        self.collision_cooldown = 0

    def move(self):
        if self.active:
            self.x += self.x_vel
            self.y += self.y_vel

            if self.x <= 0 or self.x >= 1280:
                self.x_vel *= -1
            if self.x <= 430 + 5 or self.x >= 850 - 20: # wall left and right
                self.x_vel *= -1
            if self.y <= 0:
                self.y_vel *= -1
            if self.y <= 120:
                self.y_vel *= -1
            elif self.y >= 720:
                self.active = False

            if self.collision_cooldown > 0:
                self.collision_cooldown -= 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, monster):
        monster_rect = monster.get_rect()
        ball_rect = self.get_rect()

        if self.collision_cooldown == 0 and ball_rect.colliderect(monster_rect):
            overlap_left = ball_rect.right - monster_rect.left
            overlap_right = monster_rect.right - ball_rect.left
            overlap_top = ball_rect.bottom - monster_rect.top
            overlap_bottom = monster_rect.bottom - ball_rect.top

            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                self.x = monster_rect.left - self.width
                self.x_vel *= -1
            elif min_overlap == overlap_right:
                self.x = monster_rect.right
                self.x_vel *= -1
            elif min_overlap == overlap_top:
                self.y = monster_rect.top - self.height
                self.y_vel *= -1
            elif min_overlap == overlap_bottom:
                self.y = monster_rect.bottom
                self.y_vel *= -1

            monster.take_damage(1)
            self.collision_cooldown = 10
            return True
        return False

    
class Wallblock(pygame.sprite.Sprite):
    def __init__(self, texture):
        super().__init__()
        self.image = pygame.image.load(texture)
        self.rect = self.image.get_rect()
        grid = (random.randint(0, 6), random.randint(0, 6))
        self.rect.x = grid[0]*60 + 430
        self.rect.y = grid[1]*60 + 120
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

class Multiplier(pygame.sprite.Sprite):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture
        self.image = pygame.image.load(self.texture)
        self.rect = self.image.get_rect()
        grid = (random.randint(0, 6), random.randint(0, 6))
        self.rect.x = grid[0]*60 + 430
        self.rect.y = grid[1]*60 + 120
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.multiply = random.randint(3, 17)
        self.active = True


class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Construct your sprite image.
        self.image = pygame.image.load("monster_rock.png")
        self.rect = self.image.get_rect()

        # create instances for movement
        speed = random.randrange(5, 15)
        dir_x = random.uniform(-1.0, 1.0)
        dir_y = random.uniform(-1.0, 1.0)
        dir_total = abs(dir_x) + abs(dir_y)
    
        self.change_x = dir_x/dir_total*speed
        self.change_y = dir_y/dir_total*speed

    def update(self):

        # update position
        self.rect.x += self.change_x
        self.rect.y += self.change_y


if __name__ == "__main__":
    MainMenu()
