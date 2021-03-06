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


class Outline(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self):
        if b1_health < 1:
            for outline in outline_group:
                outline_group.remove(outline)
                all_sprites_group.remove(outline)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Banner(pygame.sprite.Sprite):

    def __init__(self, x, y, Width):
        super().__init__()
        self.width = Width
        self.image = pygame.Surface([self.width, 30])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):

        self.width = b1_health * 20
        if b1_health > 1:
            self.image = pygame.Surface([self.width, 30])
            self.image.fill(PURPLE)

        if b1_health < 1:
            for banner in banner_group:
                banner_group.remove(banner)
                all_sprites_group.remove(banner)


class EnemyShooter(pygame.sprite.Sprite):
    speed_x = 0
    speed_y = 0

    def __init__(self, x, y, color, oldy, oldx):
        super().__init__()
        self.image = pygame.Surface([38, 38])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.timer = 1500
        self.direction_x = 1
        self.direction_y = 1
        self.randomX = random.choice([1, 0, -1])
        self.randomY = random.choice([1, 0, -1])
        self.oldY = oldy
        self.oldX = oldx
        self.health = 2

    def speed(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self):
        if self.health == 0:
            enemy_group.remove(self)
            all_sprites_group.remove(self)
            player_one.score += 2

        self.speed(3* self.randomX, 3 * self.randomY)

        now = pygame.time.get_ticks()
        if now - player_one.timer > 2000:
            player_one.cooldown = 1
            player_one.timer = pygame.time.get_ticks()

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

        enemy_hit_list = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        for enemy in enemy_hit_list:
            if player_one.cooldown == 1:

                player_one.health -= 10
                player_one.cooldown = 0

        while self.randomY == 0 and self.randomX == 0:
            self.randomX = random.choice([1, 0, -1])
            self.randomY = random.choice([1, 0, -1])
        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        if wall_hit_list:
            self.randomX = random.choice([1, 0, -1])
            self.randomY = random.choice([1, 0, -1])
            self.rect.x = self.oldX
            self.rect.y = self.oldY

        self.oldX = self.rect.x
        self.oldY = self.rect.y

class Boss(pygame.sprite.Sprite):
    speed_x = 0
    speed_y = 0

    def __init__(self, x, y, color, oldy, oldx):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.timer = 1500
        self.direction_x = 1
        self.direction_y = 1
        self.randomX = random.choice([1, 0, -1])
        self.randomY = random.choice([1, 0, -1])
        self.oldY = oldy
        self.oldX = oldx
        self.health = 25
        self.timer = pygame.time.get_ticks()
        self.cooldown = 0

    def speed(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self):
        if self.health == 0:
            enemy_group.remove(self)
            all_sprites_group.remove(self)
            player_one.score += 10
        global b1_health
        b1_health = self.health

        self.speed(3 * self.randomX, 3 * self.randomY)
        now = pygame.time.get_ticks()

        if now - self.timer > 10000:
            self.cooldown = 1
            self.timer = pygame.time.get_ticks()
        if self.cooldown == 1:
            for count in range(1,5):
                minion = EnemyShooter(self.rect.x, self.rect.y, PURPLE, self.rect.x, self.rect.y)
                enemy_group.add(minion)
                all_sprites_group.add(minion)

            self.cooldown = 0

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
            if now1 - player_one.timer >= 1999:
                player_one.color = RED
                player_one.image.fill(player_one.color)

        if player_one.cooldown == 1:
            player_one.color = WHITE
            player_one.image.fill(player_one.color)

        if now - player_one.timer > 2000:
            player_one.cooldown = 1
            player_one.timer = pygame.time.get_ticks()

        enemy_hit_list = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        for enemy in enemy_hit_list:
            if player_one.cooldown == 1:
                player_one.health -= 10
                player_one.cooldown = 0

        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)

        if wall_hit_list:
            self.randomX = random.choice([1, 0, -1])
            self.randomY = random.choice([1, 0, -1])
            while self.randomY == 0 and self.randomX == 0:
                self.randomX = random.choice([1, 0, -1])
                self.randomY = random.choice([1, 0, -1])
            self.rect.x = self.oldX
            self.rect.y = self.oldY

        self.oldX = self.rect.x
        self.oldY = self.rect.y


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
        self.health = 1

    def speed(self, x):
        self.rect.x += x
        self.speed_x = x

    def changespeed(self, x):
        self.speed(self.speed_x + x)


    def update(self):
        if self.health == 0:
            enemy_group.remove(self)
            all_sprites_group.remove(self)
            player_one.score += 1
        if self.direction == 1:
            self.speed(3)
        if self.direction == -1:
            self.speed(-3)

        now = pygame.time.get_ticks()
        if now - player_one.timer > 2000:
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
        self.health = 1

    def speed(self, y):
        self.rect.y += y
        self.speed_y = y

    def changespeed(self, y):
        self.speed(self.speed_y + y)


    def update(self):
        if self.health == 0:
            enemy_group.remove(self)
            all_sprites_group.remove(self)
            player_one.score += 1

        if self.direction == 1:
            self.speed(3)
        if self.direction == -1:
            self.speed(-3)

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




class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color, direction):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.available = 1
        self.direction_bullet = direction

    def speed(self, direction):
        if self.direction_bullet == 1:
            self.rect.x += 9
        if self.direction_bullet == -1:
            self.rect.x += -9
        if self.direction_bullet == 2:
            self.rect.y += 9
        if self.direction_bullet == -2:
            self.rect.y += -9
    def update(self):
        self.speed(self.direction_bullet)

        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)
        if wall_hit_list:
            bullet_group.remove(self)
            all_sprites_group.remove(self)

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_group, False)
        for enemy in enemy_hit_list:
            enemy.health += -1
            bullet_group.remove(self)
            all_sprites_group.remove(self)




class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, color, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.bullets = 80
        self.points = 0
        self.health = 100
        self.money = 0
        self.score = 0
        self.keys = 0
        self.timer = pygame.time.get_ticks()
        self.cooldown = 0
        self.rect.y = 500
        self.rect.x = 500
        self.direction_player = 1
        self.availableBullet = 1

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

        if player_one.health == 0:
            for sprites in all_sprites_group:
                all_sprites_group.remove(sprites)
            screen.fill(BLACK)
            end = 'GAME OVER'
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render(end, True, RED)
            screen.blit(text, [650, 500])


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

outline_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
banner_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
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
                enemy = EnemyShooter(screen_x, screen_y, PURPLE, screen_y, screen_x)
                all_sprites_group.add(enemy)
                enemy_group.add(enemy)

            if character == ("@"):
                boss_one = Boss(screen_x, screen_y, WHITE, screen_y, screen_x)
                all_sprites_group.add(boss_one)
                enemy_group.add(boss_one)
                boss_group.add(boss_one)
                bossHealth = Banner(250, 35, 500)
                all_sprites_group.add(bossHealth)
                banner_group.add(bossHealth)
                outline_top = Outline(WHITE,240,25,520,10)
                outline_bottom = Outline(WHITE,240, 65,520,10)
                outline_right = Outline(WHITE,240, 25, 10, 50)
                outline_left = Outline(WHITE,750, 25, 10, 50)
                outline_group.add(outline_right)
                outline_group.add(outline_left)
                outline_group.add(outline_top)
                outline_group.add(outline_bottom)
                all_sprites_group.add(outline_top)
                all_sprites_group.add(outline_bottom)
                all_sprites_group.add(outline_right)
                all_sprites_group.add(outline_left)




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
                player_one.direction_player = -1
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(5, 0)
                player_one.direction_player = 1
            if event.key == pygame.K_UP:
                player_one.changespeed(0, -5)
                player_one.direction_player = -2
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0, 5)
                player_one.direction_player = 2
            if event.key == pygame.K_SPACE:
                if player_one.bullets > 0:
                    if player_one.availableBullet == 1:
                        bul = Bullet(player_one.rect.x + 15, player_one.rect.y + 15, WHITE, player_one.direction_player)
                        player_one.availableBullet = 0
                        bullet_group.add(bul)
                        all_sprites_group.add(bul)



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_one.changespeed(5, 0)
            if event.key == pygame.K_RIGHT:
                player_one.changespeed(-5, 0)
            if event.key == pygame.K_UP:
                player_one.changespeed(0, 5)
            if event.key == pygame.K_DOWN:
                player_one.changespeed(0, -5)
            if event.key == pygame.K_SPACE:
                if player_one.bullets > 0:
                    player_one.availableBullet = 1
                    player_one.bullets += -1

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
    banner_group.draw(screen)

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