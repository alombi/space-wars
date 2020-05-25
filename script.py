# code by alombi
import os
print(os.path.abspath("."))
import random
import time
import pygame
pygame.init()

clock = pygame.time.Clock()

level = 1

health = 100
alive = True
if level > 5:
    health2 = 100
    alive2 = True
else:
    health2 = 100
    alive2 = False


# creating window
screen = pygame.display.set_mode((1380, 740))
pygame.display.set_caption('SpaceWars')

bg = pygame.image.load('bg.png')
characterLeft= pygame.image.load('characterLeft.png')
characterRight= pygame.image.load('characterRight.png')
alien = pygame.image.load('enemy.png')
alien2 = pygame.image.load('enemy.png')

left = False
right = True

# setting classes

# PLAYER
class player(object):
    def __init__(self, vel, width, height, x, y):
        self.vel = vel
        self.width = width
        self.height = height
        self.x = x
        self.y = y - height - vel
        self.hitbox = (self.x - 2, self.y -5, 55, 50)
    def draw(self, screen):
        if left == True:
            screen.blit(characterLeft, (self.x, self.y))
            self.hitbox = (self.x - 2, self.y -5, 55, 50)
        else:
            screen.blit(characterRight, (self.x, self.y))
            self.hitbox = (self.x - 2, self.y -5, 55, 50)


# BULLLETS
class ammo(object):
    def __init__(self, x, y, facing, radius, color):
        self.x = x
        self.y = y
        self.facing = facing
        self.radius = radius
        self.color = color
        self.vel = 30 * facing
    def draw(self, screen):
        pygame.draw.circle(screen,self.color, (self.x, self.y), self.radius)


# ENEMIES
class enemy(object):
    def __init__(self, x, y, width, height, end, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = vel
        self.path = [self.x, self.end]
        self.hitbox = (self.x - 2, self.y -5, 55, 60)
    def draw(self, screen):
        self.move()
        screen.blit(alien, (self.x, self.y))
        self.hitbox = (self.x - 2, self.y -5, 55, 60)
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
    def hit(self):
        print('hit')

class enemyVert(object):
    def __init__(self, x, y, width, height, end, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = vel
        self.path = [self.y, self.end]
        self.hitbox = (self.x - 2, self.y -5, 55, 60)
    def draw(self, screen):
        self.move()
        screen.blit(alien2, (self.x, self.y))
        self.hitbox = (self.x - 2, self.y -5, 55, 60)
    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.y - self.vel > self.path[0]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
    def hit(self):
        print('hit')




# function for creating display
def reloadScreen():
    screen.blit(bg, (0, 0))
    text = fontSmall.render('Level ' + str(level), 1, (255, 255, 255))
    screen.blit(text, (1250, 10))
    text = fontTitle.render('SpaceWars', 2, (255, 255, 255))
    screen.blit(text, (600, 20))
    rocket.draw(screen)
    if alive is True:
        aim.draw(screen)
    if alive2 is True:
            aim2.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

var1 = 1 * random.randrange(40, 700)
varVert = 1 * random.randrange(200, 1300)

fontSmall = pygame.font.SysFont('comicsans', 35, True, False)
fontTitle = pygame.font.SysFont('comicsans', 50, True, False)
fontAlert = pygame.font.SysFont('comicsans', 70, True, False)

if level is 1:
    aim = enemy(50, var1, 30, 30, 1300, 20)
else:
    pass
if level is 5:
    aim2 = enemyVert(varVert, 20, 30, 30, 600, 20)
else:
    pass
rocket = player(35, 50, 50, 100, 500)
bullets = []

# loop
run = True
clock.tick(27)
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        # hits
        if bullet.x < aim.hitbox[0] + (aim.width / 2) and bullet.x > aim.hitbox[0] - (aim.width / 2):
            if bullet.y < aim.hitbox [1] + (aim.height * 2) and bullet.y > aim.hitbox[1] - (aim.height * 2):
                bullets.pop(bullets.index(bullet))
                aim.hit()
                health = health - 10
                if health == 0:
                    alive = False
        if level >= 5:
            if bullet.x < aim2.hitbox[0] + (aim2.width / 2) and bullet.x > aim2.hitbox[0] - (aim2.width / 2):
                if bullet.y < aim2.hitbox [1] + (aim2.height * 2) and bullet.y > aim2.hitbox[1] - (aim2.height * 2):
                    bullets.pop(bullets.index(bullet))
                    aim2.hit()
                    health2 = health2 - 10
                    if health2 == 0:
                        alive2 = False
        # shoots
        if bullet.x < 1420 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    # collision
    if rocket.x < aim.hitbox[0] + (aim.width / 2) and rocket.x > aim.hitbox[0] - (aim.width / 2):
        if rocket.y < aim.hitbox [1] + (aim.height * 2) and rocket.y > aim.hitbox[1] - (aim.height * 2):
            text = fontAlert.render('Wasted!', 1, (255, 255, 255))
            screen.blit(text, (600, 350))
            pygame.display.update()
            time.sleep(3)
            reloadScreen()
            print('YOU LOSE')
            break
    if level >= 5:
        if rocket.x < aim2.hitbox[0] + (aim2.width / 2) and rocket.x > aim2.hitbox[0] - (aim2.width / 2):
            if rocket.y < aim2.hitbox [1] + (aim2.height * 2) and rocket.y > aim2.hitbox[1] - (aim2.height * 2):
                text = fontAlert.render('Wasted!', 1, (255, 255, 255))
                screen.blit(text, (600, 350))
                pygame.display.update()
                time.sleep(3)
                reloadScreen()
                print('YOU LOSE')
                break



                
# commands
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rocket.x > 0:
        rocket.x -= rocket.vel
        left = True
        right= False
    if keys[pygame.K_RIGHT] and rocket.x < 1400 - rocket.width - rocket.vel:
        rocket.x += rocket.vel
        left = False
        right= True
    if keys[pygame.K_UP] and rocket.y > 0:
        rocket.y -= rocket.vel
    if keys [pygame.K_DOWN] and rocket.y < 800 - rocket.height - rocket.vel:
        rocket.y += rocket.vel
    if keys [pygame.K_SPACE]:
        if left == True:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(ammo(round(rocket.x + rocket.width), round(rocket.y + rocket.height), facing, 4, (255, 204, 0)))

    if alive is False and alive2 is False:
        health = 100
        health2 = 100
        level = level + 1
        aim = enemy(50, 900, 30, 30, 1300, 20 + (7 * level))
        aim2 = enemyVert(varVert, 500, 30, 30, 600, 20)
        for bullet in bullets:
            bullet.x =1000
        pygame.display.update()
        reloadScreen()
        text = fontAlert.render('New level!', 1, (255, 255, 255))
        screen.blit(text, (550, 300))
        print(level)
        if level < 5:
            alive = True
            alive2 = False
        else:
            alive = True
            alive2 = True
        pygame.display.update()

        time.sleep(2)
        reloadScreen()
        time.sleep(1)
        aim = enemy(50, random.randrange(40, 700), 30, 30, 1300, 20 + (7 * level))
        if level >= 5:
            aim2 = enemyVert(random.randrange(100, 1300), 20, 30, 30, 600, 20 + (7 * level))
    reloadScreen()


pygame.quit()
