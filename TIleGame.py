import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50,50,255)
score = 0

 
pygame.init()
 
size = (1000, 1000)
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background = background.convert()
pygame.display.set_caption("Tile Game")


class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x



class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    global wall_group
    
    def __init__(self, color, width, height):
    
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = 500
        self.rect.x = 500
    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    def update(self, walls):
        self.rect.x += self.change_x #move left/right
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False) # Did this update caue the player to collide with a wall
        
        for block in block_hit_list:
            if self.change_x > 0: # if the player went right then change its right side coordinates tot eh left side of the walls coordinates
                self.rect.right = block.rect.left
            if self.change_x < 0: #same for left
                self.rect.left = block.rect.right

        self.rect.y += self.change_y #move up/down
        block_hit_list = pygame.sprite.spritecollide(self, wall_group, False) # Did this update caue the player to collide with a wall
        
        for block in block_hit_list:
            if self.change_y > 0: #same for up
                self.rect.bottom = block.rect.top
            if self.change_y < 0: #same for down
                self.rect.top = block.rect.bottom


levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X   XXXX                X",
"X P XXXXXXXXXXXX        X",
"X        XXXX           X",
"XXXXX    XXXX           X",
"XXXXX    XXXXXXXXX      X",
"XXXXX    XXXXXXXXX      X",
"X        XXXXXXXX       X",
"X          XXXX         X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X      XXXXXXXX         X",
"X      XXXXXXXX         X",
"X      XXXXXXXX         X",
"X      XXXXXXXX         X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"X                       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

player_one = Player(WHITE, 35, 35)
all_sprites_group.add(player_one)
player_group.add(player_one)

levels.append(level_1)

def level_setup(level):
    for y in range(len(level)):
       for x in range(len(level[y])):
           character = level[y][x]
           screen_x = x * 40
           screen_y = y * 40

           if character == ("X"):
               wall = Wall(screen_x, screen_y,RED)
               all_sprites_group.add(wall)
               wall_group.add(wall)

           if character == ("P"):
                player_one.rect.y = screen_y
                player_one.rect.x = screen_x 
               
           

   
done = False



#initialise player and put into groups


level_setup(levels[1])  # sets up the game

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_one.changespeed(-5,0)
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(5,0)
            if event.key == pygame.K_UP:
                player_one.changespeed(0,-5)
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0,5)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_one.changespeed(5,0)
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(-5,0)
            if event.key == pygame.K_UP:
                player_one.changespeed(0,5)
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0,-5)

                
 
    # --- Game logic should go here
    player_one.update(wall_group)
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    all_sprites_group.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
