import pygame
import random
import math
import csv,os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 100, 255)
GREY1 = (230,230,230)
GREY2 = (190,190,190)
GREY3 = (150,150,150)
GREY4 = (120,120,120)
GREY5 = (100,100,100)
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


class Award(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([35, 35])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.color = color

    def update(self):
        if player_one.keys == 3:
            award_one.color = YELLOW
        award_one.image.fill(award_one.color)

class Keyz(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([20, 20])
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

class EnemyShooter(pygame.sprite.Sprite):
    speed_x = 0
    speed_y = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.timer = 1500
        self.direction_x = 1
        self.direction_y = 1
        self.randomX = 1
        self.randomY = 1

    def speed(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self):

        self.speed(3* self.randomX, 3 * self.randomY)

        now = pygame.time.get_ticks()
        if now - player_one.timer > 1500:
            player_one.cooldown = 1
            player_one.timer = pygame.time.get_ticks()

        enemy_hit_list = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        for enemy in enemy_hit_list:
            if player_one.cooldown == 1:

                player_one.health -= 10
                player_one.cooldown = 0



        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        for wall in wall_hit_list:

            if self.rect.top == wall.rect.bottom:
                self.rect.top = wall.rect.bottom
            if self.rect.bottom == wall.rect.top:
                self.rect.bottom = wall.rect.top
            if self.rect.right == wall.rect.left:
                self.rect.right = wall.rect.left
            if self.rect.left == wall.rect.right:
                self.rect.left = wall.rect.right

            self.randomX = random.choice([1, 0, -1])
            self.randomY = random.choice([1, 0, -1])
            while self.randomY == 0 and self.randomX == 0:
                self.randomX = random.choice([1, 0, -1])
                self.randomY = random.choice([1, 0, -1])


class EnemyX(pygame.sprite.Sprite):
    speed_x = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.timer = 1500
        self.direction = 1

    def speed(self, x):
        self.rect.x += x
        self.speed_x = x

    def changespeed(self, x):
        self.speed(self.speed_x + x)


    def update(self):

        if self.direction == 1:
            self.speed(3)
        if self.direction == -1:
            self.speed(-3)

        now = pygame.time.get_ticks()
        if now - player_one.timer > 1500:
            player_one.cooldown = 1
            player_one.timer = pygame.time.get_ticks()

        enemy_hit_list = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        for enemy in enemy_hit_list:
            if player_one.cooldown == 1:

                player_one.health -= 10
                player_one.cooldown = 0


        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        if wall_hit_list:
           if self.direction == -1 and wall_hit_list:
                self.direction = 1
           elif self.direction == 1 and wall_hit_list:
                self.direction = -1


class EnemyY(pygame.sprite.Sprite):
    speed_y = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.timer = 1500
        self.direction = 1

    def speed(self, y):
        self.rect.y += y
        self.speed_y = y

    def changespeed(self, y):
        self.speed(self.speed_y + y)


    def update(self):

        if self.direction == 1:
            self.speed(3)
        if self.direction == -1:
            self.speed(-3)

        now2 = pygame.time.get_ticks()
        now = pygame.time.get_ticks()

        if player_one.cooldown == 0:
            now1 = pygame.time.get_ticks()

            if now1 - player_one.timer >= 200:
                player_one.color = RED
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 400:
                player_one.color = BLUE
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 600:
                player_one.color = GREEN
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 800:
                player_one.color = RED
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 1000:
                player_one.color = GREEN
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 1200:
                player_one.color = BLUE
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 1400:
                player_one.color = RED
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 1600:
                player_one.color = GREEN
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 1800:
                player_one.color = BLUE
                player_one.image.fill(player_one.color)
            if now1 - player_one.timer >= 2000:
                player_one.color = RED
                player_one.image.fill(player_one.color)


        if now - player_one.timer > 2000:
            player_one.cooldown = 1
            player_one.timer = pygame.time.get_ticks()

        if player_one.cooldown == 1:
            player_one.color = WHITE
            player_one.image.fill(player_one.color)


        enemy_hit_list = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        if enemy_hit_list:
            if player_one.cooldown == 1:

                player_one.health -= 10
                player_one.cooldown = 0


        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        if wall_hit_list:
           if self.direction == -1 and wall_hit_list:
                self.direction = 1
           elif self.direction == 1 and wall_hit_list:
                self.direction = -1




class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([10, 10])
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
        self.timer = pygame.time.get_ticks()
        self.cooldown = 0
        self.rect.y = 500
        self.rect.x = 500

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
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
            if player_one.keys == 3:
                award_one.color = YELLOW
                player_one.score = player_one.score + 1
                player_one.points = player_one.points + 1
                level_delete()
                level_setup(levels[player_one.points])
            else:
                award_one.color = BLUE

        keys_hit_list = pygame.sprite.spritecollide(self, keys_group, True)

        for keyss in keys_hit_list:
            player_one.keys = player_one.keys + 1


        self.rect.y += self.change_y  # move up/down

        block_hit_list = pygame.sprite.spritecollide(self, wall_group,
                                                     False)  # Did this update caue the player to collide with a wall

        for block in block_hit_list:
            if self.change_y > 0:  # same for up
                self.rect.bottom = block.rect.top
            if self.change_y < 0:  # same for down
                self.rect.top = block.rect.bottom


levels = []

#Reading teh level files
for root, dirs, files in os.walk("Levels"):
    for file in files:
        temp_counter = 0
        temp_array = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]

        #Open csv file
        with open("Levels/" + file) as csvfile:
            csvreader = csv.reader(csvfile)

            for row in csvreader:
                temp_string = ""
                for letter in row:
                    temp_string += letter
                temp_array[temp_counter] = temp_string
                temp_counter += 1

            levels.append(temp_array)

enemy_group = pygame.sprite.Group()
keys_group = pygame.sprite.Group()
award_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

award_one = Award(900, 900, BLUE)
player_one = Player(WHITE, 35, 35)

all_sprites_group.add(award_one)
award_group.add(award_one)
all_sprites_group.add(player_one)
player_group.add(player_one)



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

            if character == ("R"):
                award_one.rect.y = screen_y
                award_one.rect.x = screen_x

            if character == ("K"):
                key = Keyz(screen_x, screen_y, YELLOW)
                all_sprites_group.add(key)
                keys_group.add(key)

            if character == ("A"):
                enemy = EnemyX(screen_x, screen_y, GREEN)
                all_sprites_group.add(enemy)
                enemy_group.add(enemy)

            if character == ("B"):
                enemy = EnemyY(screen_x, screen_y, GREEN)
                all_sprites_group.add(enemy)
                enemy_group.add(enemy)

            if character == ("S"):
                enemy = EnemyShooter(screen_x, screen_y, PURPLE)
                all_sprites_group.add(enemy)
                enemy_group.add(enemy)

def level_delete():
    for wall in wall_group:
        wall_group.remove(wall)
        all_sprites_group.remove(wall)

    for enemy in enemy_group:
        enemy_group.remove(enemy)
        all_sprites_group.remove(enemy)

    player_one.keys = 0
    award_one.color = BLUE


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
    all_sprites_group.update()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    Health = 'Health: ' + str(player_one.health)
    Score = 'Score: ' + str(player_one.score)
    Money = 'Money: ' + str(player_one.money)
    Bullets = 'Bullets: ' + str(player_one.bullets)
    Keys_text = 'Keys: ' + str(player_one.keys)




    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprites_group.draw(screen)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Health, True, BLUE)
    screen.blit(text, [1010, 10])
    text = font.render(Score, True, WHITE)
    screen.blit(text, [1010, 130])
    text = font.render(Bullets, True, BLUE)
    screen.blit(text, [1010, 50])
    text = font.render(Money, True, WHITE)
    screen.blit(text, [1010, 210])
    text = font.render(Keys_text, True, WHITE)
    screen.blit(text, [1010, 170])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()