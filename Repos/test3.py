import pygame
import math

# Display settings
FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1280, 720

# Global constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



###################################

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([42, 42])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # initialize direction
        mx, my = pygame.mouse.get_pos()
        self.dir = (0,1)
        
    
        
    def update(self):
        # movement settings
        speed = 13

        


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.

        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

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

class Monster(pygame.sprite.Sprite):
    def __init__(self, grid):
        super().__init__()
        self.pos_x = grid[0]*60 + 430
        self.pos_y = grid[1]*60 + 120
        self.health = 10

        self.image = pygame.Surface([60, 60])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([60,570])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 30

#


class Background:  # do not put on pygame.sprite.Sprite

    def __init__(self, image):

        # Background property variables
        self.image = pygame.image.load(image)
        self.width, self.height = self.image.get_size()

        self.pos_x = 0
        self.pos_y = 0

        # Background panning variables
        self.a =  1280       # Semi-major axis
        self.b = 720         # Semi-minor axis
        self.center_x = WIN_WIDTH // 2
        self.center_y = WIN_HEIGHT // 2
        self.angle = 2

    def update(self):

        # calculate movement
        self.pos_x = self.center_x + self.a * math.cos(self.angle) - self.width/2
        self.pos_y = self.center_y + self.b * math.sin(self.angle) - self.height/2

        # Increment angle for next frame
        self.angle += 0.001


class Game:
    def __init__(self):
        self.background = Background("background.png")
        #self.wall_list = pygame.sprite.Group()
        self.ball_list = pygame.sprite.Group()
        #self.all_sprite_list = pygame.sprite.Group()
        self.wall = Wall()

#
    #def run_logic(self):

    def process_events(self):      # check all user input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                self.player.ball_shoot(mx,my)
        return True
    
    def display_frame(self, WIN):   # Display all sprite [with .draw()]
        
        #WIN.fill(WHITE)
        self.background.update()
        WIN.blit(self.background.image, (self.background.pos_x, self.background.pos_y))
        self.wall.draw(WIN)
        print(self.background.pos_x, self.background.pos_y)

        pygame.display.flip()



###################################



def main():
    # initialize all set ups
    pygame.init()
    pygame.mixer.init()

    # initialize display
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Shooting Star: INTERGALACTIC FRONTIER")

    # variables
    clock = pygame.time.Clock()

    # constructs game class
    game = Game()

    '''game loop'''
    RUN = True
    while RUN:

        clock.tick(FPS)
        RUN = game.process_events()
        game.display_frame(WIN)

    pygame.quit() #Exit while loop if game.process_events() returns False

main()  #execute main program