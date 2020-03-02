# Bismillah
import pygame
import time
from random import randrange as rnd


# initialize pygame
pygame.init()
# defualt colors
dpcolor = (225, 225, 225)
black = (0, 0, 0)
color1 = (100, 100, 100)
# creating class


class Snake:
    def __init__(self):
        super().__init__()
        self.xpos = 390
        self.ypos = 290
        pygame.draw.rect(screen, black, [self.xpos, self.ypos, 10, 10])
        self.reboot = False
        self.font = pygame.font.SysFont(None, 25)

    def moves(self, direction):
        if self.reboot:  # when snake goes abroad of screen
            pygame.draw.rect(screen, black, [self.lastX, self.lastY, 10, 10])
            self.reboot = False
        else:  # in other situations
            if direction == 'l':
                self.xpos -= 10
            elif direction == 'r':
                self.xpos += 10
            elif direction == 'u':
                self.ypos -= 10
            elif direction == 'd':
                self.ypos += 10
        pygame.draw.rect(screen, black, [self.xpos, self.ypos, 10, 10])

    def xypos(self):  # this function just returns position of head of snake
        return print(self.xpos, self.ypos)
# when snake goes abroad, snake respawn on opposite side.
# like there is no boundaries

    def reborn(self):
        if self.xpos > 790:
            self.lastY = self.ypos
            self.lastX = 0
            self.xpos = 0
            self.reboot = True
        elif self.xpos < -10:
            self.lastY = self.ypos
            self.xpos = 790
            self.lastX = 790
            self.reboot = True
        elif self.ypos > 590:
            self.lastX = self.xpos
            self.lastY = 0
            self.ypos = 0
            self.reboot = True
        elif self.ypos < -10:
            self.lastX = self.xpos
            self.lastY = 590
            self.reboot = True
            self.ypos = 590

    def message(self, text, color, coor):
        screen_text = self.font.render(text, True, color)
        screen.blit(screen_text, [coor[0], coor[1]])

# class food


class Food(Snake):
    def __init__(self):
        super().__init__()
        self.fxpos = rnd(0, 790, 10)
        self.fypos = rnd(0, 590, 10) 

    def born(self, live):
        self.live = live
        if not self.live:
            pygame.draw.rect(screen, color1, [self.fxpos, self.fypos, 10, 10])

    def checklive(self):
        if self.fxpos == self.xpos and self.fxpos == self.fxpos:
            print('peace do')
            self.live = False 
        
    def fxypos(self):  # this function just returns position of head of snake
        return print(self.fxpos, self.fypos)    

# display setting
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake GAme from Nokia')
print(type(screen.get_size()))
clock = pygame.time.Clock()

# creating overall game objects
sn4ke = Snake()
chdTo = str()  # sending keys
points = int()  # gamer score
fud = Food()  # fud object

# vars
fps = 15
xpos = int()
ypos = int()
fxpos = int()
fypos = int()
e_var = bool()

running = True
# running till user does not press close buttons
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        print('u')
        chdTo = 'u'
    if pressed[pygame.K_DOWN]:
        print('d')
        chdTo = 'd'
    if pressed[pygame.K_RIGHT]:
        print('r')
        chdTo = 'r'
    if pressed[pygame.K_LEFT]:
        print('l')
        chdTo = 'l'
    if pressed[pygame.K_ESCAPE]:
        running = False
    

    # update anau mnau
    screen.fill(dpcolor)
    sn4ke.reborn()
    sn4ke.moves(chdTo)
    fud.born(False)

    pygame.display.update()
    pygame.display.flip()
    # fps
    clock.tick(fps)
# quitting pygame
sn4ke.message("GAme over your score:" + str(points), black, [300, 400])
pygame.display.update()
time.sleep(0.5)
pygame.quit()
