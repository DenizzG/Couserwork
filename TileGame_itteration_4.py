import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (150, 150, 255)
YELLOW = (255, 255, 0)

pygame.init()

size = (1300, 1000)
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background = background.convert()
pygame.display.set_caption("Tile Game")

#font = pygame.font.Font('freesansbold.ttf', 40)
#text = font.render("ASKFJHBSDGBLKSBGKJSNG", True, RED, RED)
#textRect = text.get_rect()
#textRect.center = (1150, 1080)


class Award(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([35, 35])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, color, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.bullets = 500
        self.points = 0
        self.health = 100
        self.money = 0
        self.score = 0
        self.keys = 0
        self.rect.y = 500
        self.rect.x = 500

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self, wall):
        self.rect.x += self.change_x  # move left/right
        block_hit_list = pygame.sprite.spritecollide(self, wall_group,
                                                     False)  # Did this update caue the player to collide with a wall

        for block in block_hit_list:
            if self.change_x > 0:  # if the player went right then change its right side coordinates tot eh left side of the walls coordinates
                self.rect.right = block.rect.left
            if self.change_x < 0:  # same for left
                self.rect.left = block.rect.right

        award_hit_list = pygame.sprite.spritecollide(self, award_group, False)

        for award in award_hit_list:
            player_one.score = player_one.score + 1
            player_one.points = player_one.points + 1
            level_delete()
            level_setup(levels[player_one.points])

        self.rect.y += self.change_y  # move up/down

        block_hit_list = pygame.sprite.spritecollide(self, wall_group,
                                                     False)  # Did this update caue the player to collide with a wall

        for block in block_hit_list:
            if self.change_y > 0:  # same for up
                self.rect.bottom = block.rect.top
            if self.change_y < 0:  # same for down
                self.rect.top = block.rect.bottom


levels = []

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXX                X",
    "X X XXXXXX     XXXXXX   X",
    "X        XX    XXXXXX   X",
    "XXXXX    XX             X",
    "XXXXX    XX  XXX XXX    X",
    "XXXXX    XX  XX  XXX    X",
    "X        XX     XXXX    X",
    "X  XXX    XXXXXXXXX     X",
    "X  XX                   X",
    "X      XXXXX            X",
    "X         XXXXXX        X",
    "X    XXXX  XXXX     X   X",
    "X    XXXX       XX XX   X",
    "X              XXX XX   X",
    "X      XXXXXXXXXX      XX",
    "X      X           XXXXXX",
    "X      X         XXXXXXXX",
    "X  XXXXXXXXXXXXXXX  A   X",
    "X     X                 X",
    "XXXX  X  XX             X",
    "X     X  XX             X",
    "X  XXXX  XX             X",
    "X        XX             X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                       X",
    "X   XXXXXXXXXXXXXX      X",
    "X    XXXXXXXXXXXX       X",
    "X     XXXXXXXXXX        X",
    "X     XXXXXXXXXX        X",
    "X     XXXXXXXXXX        X",
    "X     XXXXXXXXXX        X",
    "X                       X",
    "X                    P  X",
    "X                       X",
    "X      XXXXXXXXXX       X",
    "X                       X",
    "X     A                 X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                       X",
    "X    P             X    X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X          XXXXXXXX     X",
    "X                       X",
    "X               XXX     X",
    "X               X X     X",
    "X               XXX     X",
    "X                  A    X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "X                       X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

award_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

award_one = Award(900, 900, YELLOW)
player_one = Player(WHITE, 35, 35)

all_sprites_group.add(award_one)
award_group.add(award_one)
all_sprites_group.add(player_one)
player_group.add(player_one)

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)


def level_setup(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = x * 40
            screen_y = y * 40

            if character == ("X"):
                wall = Wall(screen_x, screen_y, RED)
                all_sprites_group.add(wall)
                wall_group.add(wall)

            if character == ("P"):
                player_one.rect.y = screen_y
                player_one.rect.x = screen_x

            if character == ("A"):
                award_one.rect.y = screen_y
                award_one.rect.x = screen_x


def level_delete():
    for wall in wall_group:
        wall_group.remove(wall)
        all_sprites_group.remove(wall)


done = False

# initialise player and put into groups


level_setup(levels[0])  # sets up the game
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_one.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player_one.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0, 5)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_one.changespeed(5, 0)
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(-5, 0)
            if event.key == pygame.K_UP:
                player_one.changespeed(0, 5)
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0, -5)

    # --- Game logic should go here
    player_one.update(wall_group)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    Health = 'Health: ' + str(player_one.health)
    Score = 'Score: ' + str(player_one.score)
    Money = 'Money: ' + str(player_one.money)
    Bullets = 'Bullets: ' + str(player_one.bullets)



    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprites_group.draw(screen)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Health, True, WHITE)
    screen.blit(text, [1010, 10])
    text = font.render(Score, True, WHITE)
    screen.blit(text, [1010, 50])
    text = font.render(Bullets, True, WHITE)
    screen.blit(text, [1010, 90])
    text = font.render(Money, True, WHITE)
    screen.blit(text, [1010, 130])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()