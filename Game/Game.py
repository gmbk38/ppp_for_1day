from os import kill
import pygame
import random
import time
from Textures import Textures
from Functions import Menu as Menu
from Functions import Lives as Lives
from Functions import Live_control as Live_control


#Движение спрайта в бок
#Бессметритие от "Спрайта"
#Cпрайт стреляет


WIDTH = 600
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def filler():
    x = random.randint (0,255)
    y = random.randint (0,255)
    z = random.randint (0,255)
    return ((x,y,z))

count_enemy = 0

def bot_spawner(period):

    global lives
    global count_enemy

    if int(time.time() - period) < 0.5:
        return period
    else:
        e = Enemy()
        all_sprites.add(e)
        enemy.add(e)
        period = time.time()
        lives += 1
        count_enemy += 1
        return period

    if int(time.time() - period) < 15:
        return period
    else:
        boss = Mini_boss()
        all_sprites.add(boss)
        mini_boss.add(boss)
        period = time.time()
        return period

def texture_finder(num):
    num = int(num)
    if num == 0:
        texture = Textures.zero
    elif num == 1:
        texture = Textures.one
    elif num == 2:
        texture = Textures.two
    elif num == 3:
        texture = Textures.three
    elif num == 4:
        texture = Textures.four
    elif num == 5:
        texture = Textures.five
    elif num == 6:
        texture = Textures.six
    elif num == 7:
        texture = Textures.seven
    elif num == 8:
        texture = Textures.eight
    elif num == 9:
        texture = Textures.nine
    return texture

def Counter(counter):
    counter = str(counter)
    for i in range (0,len(counter)):
        specific_num = counter[i]
        specific_tex = texture_finder(specific_num)
        specific_tex = specific_tex.convert_alpha()
        screen.blit(specific_tex,(130 - 40*(len(counter)-1-i),60))
    return True

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship fight")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        global lvl_control
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = Textures.first_form
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        # if keystate[pygame.K_UP]:
        #     self.speedy = -10
        # if keystate[pygame.K_DOWN]:
        #     self.speedy = 10
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - 100:
            self.rect.y = HEIGHT - 100
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        global lvl_control

        # e = Enemy_for_boss(mini_boss.shoot_x_pos(),mini_boss.shoot_y_pos())
        # all_sprites.add(e)
        # enemy.add(e)
        
        if lvl_control == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif lvl_control == 2:
            bullet = Bullet_lvl2_left(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet_lvl2_right(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif lvl_control == 3:
            fire= Bullet_lvl3(self.rect.centerx, self.rect.top)
            all_sprites.add(fire)
            bullets.add(fire)

class Enemy_for_boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = Textures.bullet_3
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 3

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y < 10:
            self.rect.y = 10
            self.speedy = 1
        if self.rect.y > HEIGHT - 60:
            self.rect.y = HEIGHT - 60
            self.speedy = -1
        if self.rect.right > WIDTH - 10:
            self.rect.right = WIDTH - 10
            self.speedx = -1
        if self.rect.left < 10:
            self.rect.left = 10
            self.speedx = 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 75))
        self.image = Textures.enemy_1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = -1*random.randint(0,100)
        self.speedx = 0
        self.speedy = 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y < 10:
            self.rect.y = 10
            self.speedy = random.randint(1,3)
        if self.rect.right > WIDTH - 10:
            self.rect.right = WIDTH - 10
            self.speedx = -1
        if self.rect.left < 10:
            self.rect.left = 10
            self.speedx = 1

        if lvl_control == 1:
            self.image = Textures.enemy_1
        elif lvl_control == 2:
            self.image = Textures.enemy_2
        elif lvl_control == 3:
            self.image = Textures.enemy_3

boss_kill = 0

def boss_killer_func():
    global boss_kill
    boss_kill += 15
    player.image = Textures.third_form
    return boss_kill



class Mini_boss(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = Textures.star
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(10,HEIGHT - 400)
        self.lives = 1
        self.speedx = 0
        self.speedy = 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH - 10:
            self.rect.right = WIDTH - 10
            self.speedx = 0 #------------------------
        if self.rect.left < 10:
            self.rect.left = 10
            self.speedx = 0 #------------------------

        if self.lives == 0:
            boss_kill = 15
            self.kill()
            boss_killer_func()

    def shoot_x_pos(self):
        return self.rect.x

    def shoot_y_pos(self):
        return self.rect.y


# class Boss_Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((30, 30))
#         self.image = Textures.bullet_1
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x
#         self.speedy = 5
#         self.speedx = 0

#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.bottom > 600:
#             self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = Textures.bullet_1
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5
        self.speedx = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Bullet_lvl2_left(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = Textures.bullet_2l
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -3
        self.speedx = -3

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()

class Bullet_lvl2_right(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = Textures.bullet_2r
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -3
        self.speedx = 3

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()

class Bullet_lvl3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image = Textures.bullet_3
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -2
        self.speedx = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
me = pygame.sprite.Group()
enemy = pygame.sprite.Group()
bullets = pygame.sprite.Group()

mini_boss = Mini_boss()
player = Player()
me.add(player)
all_sprites.add(player)
# all_sprites.add(mini_boss)

#for i in range(10):
#    e = Enemy()
#    all_sprites.add(e)
#    enemy.add(e)

period = time.time()
period_to_spawn_boss = random.randint(1,10)

counter = 0
lvl_control = 1
lives = 5

running = True
while running:
    clock.tick(FPS)

    if lives == 0:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # if  count_enemy == 5:
    #     all_sprites.add(mini_boss) 

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_d]:
        player.shoot()

    if lvl_control == 1 and boss_kill == 0:
            player.image = Textures.first_form
            background = Textures.screen_1
    elif lvl_control == 2:
            player.image = Textures.second_form
            background = Textures.screen_2
    elif lvl_control == 3:
            player.image = Textures.third_form
            background = Textures.screen_3


    # if keystate[pygame.K_l]:
    #     if counter >= 1000 and lvl_control == 1:
    #         counter -= 1000
    #         lvl_control = 2
    #     elif lvl_control == 2 and counter >= 10000:
    #         counter -= 10000
    #         lvl_control = 3
    
    period = bot_spawner(period)

    all_sprites.update()

    touch = pygame.sprite.groupcollide(me, enemy, False, True)
    if touch:
        if boss_kill != 0:
            boss_kill -= 1
        else:
            lives -= 1
        e1 = Enemy()
        e2 = Enemy()
        e3 = Enemy()
        enemy.add(e1)
        enemy.add(e2)
        enemy.add(e3)
        all_sprites.add(e1)
        all_sprites.add(e2)
        all_sprites.add(e3)

    boss_touch = pygame.sprite.spritecollide(mini_boss, me, False)
    if boss_touch:
        mini_boss.lives = 0

    boss_touch = pygame.sprite.spritecollide(mini_boss, bullets, True)
    if boss_touch:
        mini_boss.lives -= 1
    
    if lvl_control < 2:
        hits = pygame.sprite.groupcollide(bullets, enemy, True, True)
        if hits:
            counter += random.randint(1,10)
    elif lvl_control == 2:
        hits = pygame.sprite.groupcollide(bullets, enemy, True, True)
        if hits:
            counter += 10
    else:
        hits = pygame.sprite.groupcollide(bullets, enemy, False, True)
        if hits:
            counter += 10

    #screen.fill(YELLOW)

    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    Counter(counter)
    # Menu(screen)
    lives = Live_control(lives)
    Lives(screen, lives)
    pygame.display.flip()

pygame.quit()