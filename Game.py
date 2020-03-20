# import pygame module in this program 
import pygame
from time import sleep
from random import randrange as rnd
import sys
from plyer import notification
import os
import sys
import math

def main_snake():

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
            pygame.draw.rect(screen, black, [self.xpos, self.ypos, 10, points * 10])
            self.reboot = False
            self.font = pygame.font.SysFont(None, 25)
            self.snakeList = []
            self.head = []

        def moves(self, direction):

            snakeHead = []
            self.head = []
            if len(self.snakeList) > points:
                del self.snakeList[0]
            self.snakeList.append(self.head)
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
            self.head.append(self.xpos)
            self.head.append(self.ypos)
            for xny in self.snakeList:
                pygame.draw.rect(screen, black, [xny[0], xny[1], 10, 10])

        def selfcrash(self):
            for elem in self.snakeList[:-1]:
                if elem == self.head:
                    return True

        def xypos(self):  # this function just returns position of head of snake
            return self.xpos, self.ypos
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

        def born(self, tiri):
            if not tiri:
                self.fxpos = rnd(0, 790, 10)
                self.fypos = rnd(0, 590, 10) 
            else:
                pass
            pygame.draw.rect(screen, color1, [self.fxpos, self.fypos, 10, 10])

        def checklive(self):
            if self.fxpos == self.xpos and self.fxpos == self.fxpos:
                print('peace do')
                self.live = False 
            
        def fxypos(self):  # this function just returns position of head of snake
            return (self.fxpos, self.fypos)  

    # functions like global
    def is_col(the_first, the_second):
        the_first = the_first.fxypos()
        the_second = the_second.xypos()
        if the_first == the_second:
            return True
        else:
            return False

    # display setting
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Snake GAme from Nokia')

    print(type(screen.get_size()))
    clock = pygame.time.Clock()

    # creating overall game objects
    points = 1  # gamer score
    sn4ke = Snake()

    chdTo = str()  # sending keys
    fud = Food()  # fud object

    # vars
    fps = 15

    running = True
    # running till user does not press close buttons
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            chdTo = 'u'
        if pressed[pygame.K_DOWN]:
            chdTo = 'd'
        if pressed[pygame.K_RIGHT]:
            chdTo = 'r'
        if pressed[pygame.K_LEFT]:
            chdTo = 'l'
        if pressed[pygame.K_ESCAPE]:
            running = False
            mainbastau()
            # bastau.mainbastau()  

        if points > 1:
            if sn4ke.selfcrash():
                running = False

        # update anau mnau
        screen.fill(dpcolor)
        fud.born(True)
        if is_col(fud, sn4ke):
            points += 1
            fud.born(False)
        sn4ke.reborn()
        sn4ke.moves(chdTo)

        pygame.display.update()
        pygame.display.flip()
        # fps
        clock.tick(fps)
    # quitting pygame
    sn4ke.message("GAme over your score:" + str(points - 1), black, [300, 400])

    pygame.display.update()
    sleep(1)
    pygame.quit()


def mmain():
    pygame.init()

    FPS = 60

    scr_size = (width,height) = (600,400)

    clock = pygame.time.Clock()

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255 ,0, 0)

    screen = pygame.display.set_mode(scr_size)
    pygame.display.set_caption('Pong')

    def displaytext(text,fontsize,x,y,color):
        font = pygame.font.SysFont('sawasdee', fontsize, True)
        text = font.render(text, 1, black)
        textpos = text.get_rect(centerx=x, centery=y)
        screen.blit(text, textpos)

    def cpumove(cpu,ball):
        if ball.movement[0] > 0: #ensures that the CPU moves only when the ball is directed towards it
            #the extra addition of cpu.rect.height/5 ensures that the CPU will miss the ball sometimes
            if ball.rect.bottom > cpu.rect.bottom + cpu.rect.height/5:
                cpu.movement[1] = 8
            elif ball.rect.top < cpu.rect.top - cpu.rect.height/5:
                cpu.movement[1] = -8
            else:
                cpu.movement[1] = 0
        else:
            cpu.movement[1] = 0

    class Paddle(pygame.sprite.Sprite):
        def __init__(self,x,y,sizex,sizey,color):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.sizex = sizex
            self.sizey = sizey
            self.color = color
            self.image = pygame.Surface((sizex,sizey),pygame.SRCALPHA,32)
            self.image = self.image.convert_alpha()
            pygame.draw.rect(self.image,self.color,(0,0,sizex,sizey))
            self.rect = self.image.get_rect()
            self.rect.left = self.x
            self.rect.top = self.y
            self.points = 0
            self.movement = [0,0]

        def checkbounds(self):
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > height:
                self.rect.bottom = height
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width

        def update(self):
            self.rect = self.rect.move(self.movement)
            self.checkbounds()

        def draw(self):
            screen.blit(self.image,self.rect)


    class Ball(pygame.sprite.Sprite):

        def __init__(self,x,y,size,color,movement=[0,0]):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.size = size
            self.color = color
            self.movement = movement
            self.image = pygame.Surface((size,size),pygame.SRCALPHA,32)
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            pygame.draw.circle(self.image,self.color,(int(self.rect.width/2),int(self.rect.height/2)),int(size/2))
            self.rect.centerx = x
            self.rect.centery = y
            self.maxspeed = 6
            self.score = 0
            self.movement = movement

        def checkbounds(self):
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > height:
                self.rect.bottom = height
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > width:
                self.rect.right = width

        def update(self):
            if self.rect.top == 0 or self.rect.bottom == height:
                self.movement[1] = -1*self.movement[1]
            if self.rect.left == 0: 
                self.rect.centerx = width/2
                self.rect.centery = height/2
                self.movement = [rnd(-1,2,2)*4,rnd(-1,2,2)*4]
                self.score = 1

            if self.rect.right == width:
                self.rect.centerx = width/2
                self.rect.centery = height/2
                self.movement = [rnd(-1,2,2)*4,rnd(-1,2,2)*4]
                self.score = -1

            self.rect = self.rect.move(self.movement)
            self.checkbounds()

        def draw(self):
            pygame.draw.circle(self.image,self.color,(int(self.rect.width/2),int(self.rect.height/2)),int(self.size/2))
            screen.blit(self.image,self.rect)



    gameOver = False 
    paddle = Paddle(width/10,height/2,width/60,height/8,black) 
    cpu = Paddle(width - width/10,height/2,width/60,height/8,black)
    ball = Ball(width/2,height/2,12,red,[4,4]) 

    while not gameOver: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                quit()                    

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:
                    paddle.movement[1] = -8 
                elif event.key == pygame.K_DOWN: 
                    paddle.movement[1] = 8
            if event.type == pygame.KEYUP:
                paddle.movement[1] = 0
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                gameOver = True
                mainbastau()

        cpumove(cpu,ball)
        screen.fill(white)
        paddle.draw()
        cpu.draw()
        ball.draw()

        displaytext(str(paddle.points),20,width/8,25,(255,255,255))
        displaytext(str(cpu.points),20,width - width/8,25,(255,255,255))

        if pygame.sprite.collide_mask(paddle,ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*rnd(5,10)*paddle.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        if pygame.sprite.collide_mask(cpu,ball):
            ball.movement[0] = -1*ball.movement[0]
            ball.movement[1] = ball.movement[1] - int(0.1*rnd(5,10)*cpu.movement[1])
            if ball.movement[1] > ball.maxspeed:
                ball.movement[1] = ball.maxspeed
            if ball.movement[1] < -1*ball.maxspeed:
                ball.movement[1] = -1*ball.maxspeed

        if ball.score == 1:
            cpu.points += 1
            ball.score = 0
        elif ball.score == -1:
            paddle.points += 1
            ball.score = 0

        paddle.update()

        ball.update()

        cpu.update()

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

def running2f(var):
    Nu = True
    running2 = var
    display_surface = pygame.display.set_mode((600, 400))
    qten = True
    aios = True
    font = pygame.font.Font('freesansbold.ttf', 32) 
    font1 = pygame.font.Font('freesansbold.ttf', 20) 
    font2 = pygame.font.Font('freesansbold.ttf', 13)
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    red = (255, 0, 0)
    black = (0, 0, 0)
    dpcolor = (225, 225, 225)
    color1 = (100, 100, 100)
    yellow = (255, 255, 0)
    azax = 455
    azay = 350

    while running2:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running2 = False
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                mainbastau()
                running1 = False

        if Nu:
            display_surface.fill(yellow)

            text4 = font1.render("Игра на проверку знаний",True,red)
            text5 = font2.render("1.Пишется буква о: ",True,red)
            text6 = font2.render("А) Сч…тчик. ",True,red)
            text7 = font2.render("В) Поч…тный. ",True,red)
            text8 = font2.render("С) Ш…пот. ",True,red)
            text9 = font2.render("D) Ч…каться. ",True,red)
            #CORRdd

            text10 = font2.render("2.Синонимы: ",True,red)
            text11 = font2.render("А) облако, облачный.",True,red)
            text12 = font2.render("В) север, юг. ",True,red)
            text13 = font2.render("С) восхитительный, замечательный  ",True,red)
            text14 = font2.render("D) могучий, слабый  ",True,red)
            #CORRcc

            text15 = font2.render("3. Антоним к слову грусть : ",True,red)
            text16 = font2.render("А) апатия",True,red)
            text17 = font2.render("В) ненависть",True,red)
            text18 = font2.render("С) безразличие",True,red)
            text19 = font2.render("D) радость",True,red)
            #CORRdd

            text20 = font2.render("4. Фразеологизм",True,red)
            text21 = font2.render("А) козёл отпущения ",True,red)
            text22 = font2.render("В) запутать дело ",True,red)
            text23 = font2.render("С) удачное начало ",True,red)
            text24 = font2.render("D) быстро бежать ",True,red)
            #CORRaa

            text25 = font2.render("5. Ь не пишется ",True,red)
            text26 = font2.render("А) сентябр...ский  ",True,red)
            text27 = font2.render("В) звер...ский ",True,red)
            text28 = font2.render("С) октябр...ский  ",True,red)
            text29 = font2.render("D) декабр...ский  ",True,red)
            #CORRbb

            text30 = font2.render("6.Глагол повелительного наклонения  ",True,red)
            text31 = font2.render("А) знает ",True,red)
            text32 = font2.render("В) знайте ",True,red)
            text33 = font2.render("С) знать ",True,red)
            text34 = font2.render("D) узнает ",True,red)
            #CORRbb

            text35 = font1.render("Проверить",True,black)

            buttonaza = pygame.Rect(455, 350, 115, 40)

            display_surface.blit(text4,(160,20))

            display_surface.blit(text5,(40,60))
            display_surface.blit(text6,(60,80))
            display_surface.blit(text7,(60,100))
            display_surface.blit(text8,(60,120))
            display_surface.blit(text9,(60,140))

            display_surface.blit(text10,(40,170))
            display_surface.blit(text11,(60,190))
            display_surface.blit(text12,(60,210))
            display_surface.blit(text13,(60,230))
            display_surface.blit(text14,(60,250))

            display_surface.blit(text15,(40,280))
            display_surface.blit(text16,(60,300))
            display_surface.blit(text17,(60,320))
            display_surface.blit(text18,(60,340))
            display_surface.blit(text19,(60,360))

            display_surface.blit(text20,(340,60))
            display_surface.blit(text21,(360,80))
            display_surface.blit(text22,(360,100))
            display_surface.blit(text23,(360,120))
            display_surface.blit(text24,(360,140))

            display_surface.blit(text25,(340,170))
            display_surface.blit(text26,(360,190))
            display_surface.blit(text27,(360,210))
            display_surface.blit(text28,(360,230))
            display_surface.blit(text29,(360,250))

            display_surface.blit(text30,(340,280))
            display_surface.blit(text31,(360,300))
            display_surface.blit(text32,(360,320))
            display_surface.blit(text33,(360,340))
            display_surface.blit(text34,(360,360))

            pygame.draw.rect(display_surface, [255, 0, 0], buttonaza)
            display_surface.blit(text35,(460,360))

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if azax <= x <= 570 and azay <= y <= 390:
                Nu = False
                display_surface.fill(white)
                texta1 = font2.render("Ответы",True,red)
                texta11 = font2.render("1.D",True,red)
                texta22 = font2.render("2.C",True,red)
                texta33 = font2.render("3.D",True,red)
                texta44 = font2.render("4.A",True,red)
                texta55 = font2.render("5.B",True,red)
                texta66 = font2.render("6.B",True,red)

                display_surface.blit(texta1,(40,60))
                display_surface.blit(texta11,(60,80))
                display_surface.blit(texta22,(60,100))
                display_surface.blit(texta33,(60,120))
                display_surface.blit(texta44,(60,140))
                display_surface.blit(texta55,(60,160))
                display_surface.blit(texta66,(60,180))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            Nu = True

        pygame.display.update()

def running1f(var):
    running1 = var
    display_surface = pygame.display.set_mode((600, 400))
    qten = True
    aios = True
    font = pygame.font.Font('freesansbold.ttf', 32) 
    font1 = pygame.font.Font('freesansbold.ttf', 20) 
    font2 = pygame.font.Font('freesansbold.ttf', 13)
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    red = (255, 0, 0)
    black = (0, 0, 0)
    dpcolor = (225, 225, 225)
    color1 = (100, 100, 100)
    yellow = (255, 255, 0)
    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                mainbastau()
                running1 = False
        display_surface.fill((255, 255, 255))
        if qten:
            text36 = font2.render("Химические загрязнители",True,black)
            text37 = font2.render("могут вызывать острые",True,red)
            text38 = font2.render("отравления,",True,blue)
            text39 = font2.render("болезни.",True,blue)

            text40 = font2.render("Различные пластиковые",True,green)
            text41 = font2.render("контейнеры и трубочки",True,black)
            text42 = font2.render("являются врагами",True,blue)
            text43 = font2.render("экологии.",True,red)

            text44 = font2.render("Во-первых,",True,blue)
            text45 = font2.render("не",True,black)
            text46 = font2.render("бросать мусор",True,red)
            text47 = font2.render("повсюду.",True,black)
            
            display_surface.blit(text36,(10,20))
            display_surface.blit(text37,(195,20))
            display_surface.blit(text38,(362,20))
            display_surface.blit(text39,(450,20))

            display_surface.blit(text40,(10,50))
            display_surface.blit(text41,(185,50))
            display_surface.blit(text42,(360,50))
            display_surface.blit(text43,(495,50))

            display_surface.blit(text44,(10,80))
            display_surface.blit(text45,(90,80))
            display_surface.blit(text46,(110,80))
            display_surface.blit(text47,(210,80))
            pygame.display.update()
            sleep(4)
            qten = False
        display_surface.fill(yellow)
        textau = font.render("Какое слово было красным?",True,black)
        display_surface.blit(textau,(30,20))
        but1 = pygame.Rect(100, 120, 120, 40)
        but2 = pygame.Rect(350, 120, 120, 40)
        but3 = pygame.Rect(100, 290, 120, 40)
        but4 = pygame.Rect(350, 290, 120, 40)

        but1x = 100
        but1y = 120

        but2x = 350
        but2y = 120

        but3x = 100
        but3y = 290

        but4x = 350
        but4y = 290

        tex1 = font2.render("Контейнер",True,blue)
        tex2 = font2.render("Экология",True,blue)
        tex3 = font2.render("Болезни",True,blue)
        tex4 = font2.render("Враг",True,blue)
        pygame.draw.rect(display_surface, [255, 0, 0], but1)
        pygame.draw.rect(display_surface, [255, 0, 0], but2)
        pygame.draw.rect(display_surface, [255, 0, 0], but3)
        pygame.draw.rect(display_surface, [255, 0, 0], but4)
        display_surface.blit(tex1,(125,130))
        display_surface.blit(tex2,(375,130))
        display_surface.blit(tex3,(130,300))
        display_surface.blit(tex4,(390,300))
        if aios:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if but2x <= x <= 470 and but2y <= y <= 160:
                    print("ooo")
                    print("ooo")
                    notification.notify(
                        title='Notification)',
                        message='Your answer is correct',
                        app_icon='ph.ico',
                        timeout=6,)
                    aios = False

                elif but1x <= x <= 220 and but1y <= y <= 160:
                    notification.notify(
                        title='Notification)',
                        message='Your answer is not correct',
                        app_icon='ph.ico',
                        timeout=6,)
                    aios = False

                elif but3x <= x <= 220 and but3y <= y <= 330:
                    notification.notify(
                        title='Notification)',
                        message='Your answer is not correct',
                        app_icon='ph.ico',
                        timeout=6,)
                    aios = False

                elif but4x <= x <= 640 and but4y <= y <= 330:
                    notification.notify(
                        title='Notification)',
                        message='Your answer is not correct',
                        app_icon='ph.ico',
                        timeout=6,)
                    aios = False
        pygame.display.update()

def mainbastau():
    # activate the pygame library 
    # initiate pygame and give permission 
    # to use pygame's functionality. 
    pygame.init() 

    Nu = True
    # define the RGB value for white, 
    # green, blue colour . 
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    red = (255, 0, 0)
    black = (0, 0, 0)
    dpcolor = (225, 225, 225)
    color1 = (100, 100, 100)
    yellow = (255, 255, 0)

    # assigning values to X and Y variable 
    X = 600
    Y = 400

    one_rectx = 30
    one_recttop = 300

    two_rectx = 170
    two_recttop = 300

    three_rectx = 310
    three_recttop = 300

    four_rectx = 450
    four_recttop = 300

    # create the display surface object 
    # of specific dimension..e(X, Y). 
    display_surface = pygame.display.set_mode((X, Y)) 

    # set the pygame window name 
    pygame.display.set_caption('GAME') 

    start_screen = True

    running1 = False
    running2 = False
    runningame1 = False
    runningame2 = False

    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    font = pygame.font.Font('freesansbold.ttf', 32) 
    font1 = pygame.font.Font('freesansbold.ttf', 20) 
    font2 = pygame.font.Font('freesansbold.ttf', 13)

    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render('Game from r1chter1 and iMAGA', True, green, blue) 
    text2 = font1.render("Test1",True,black)
    text111 = font1.render("Test2",True,black)
    text3 = font1.render("Ping-Pong",True,black)
    text222 = font1.render("Snake",True,black)

    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect() 

    # set the center of the rectangular object. 
    textRect.center = (X // 2, 100) 

    button = pygame.Rect(30, 300, 110, 40)
    button11 = pygame.Rect(170, 300, 110, 40)
    button2 = pygame.Rect(310, 300, 110, 40)
    button22 = pygame.Rect(450, 300, 110, 40)
    qten = True
    aios = True
    # infinite loop 
    while start_screen: 

        # completely fill the surface object 
        # with white color 
        display_surface.fill(white) 

        # copying the text surface object 
        # to the display surface object 
        # at the center coordinate. 

        pygame.draw.rect(display_surface, [255, 0, 0], button)
        pygame.draw.rect(display_surface, [255, 0, 0], button11)
        pygame.draw.rect(display_surface, [255, 0, 0], button2)
        pygame.draw.rect(display_surface, [255, 0, 0], button22)

        display_surface.blit(text, textRect)
        display_surface.blit(text2,(60,310))
        display_surface.blit(text111,(200,310))
        display_surface.blit(text222,(335,310))
        display_surface.blit(text3,(455,310))

        # iterate over the list of Event objects 
        # that was returned by pygame.event.get() method. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen = False
                running1 = False
                running2 = False
                runningame1 = False
                runningame2 = False
                return False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if one_rectx <= x <= 140 and one_recttop <= y <= 340:
                start_screen = False
                running1f(True)
                running2 = False
                runningame1 = False

            elif two_rectx <= x <= 280 and two_recttop <= y <= 340:
                start_screen = False
                running2f(True)
                running1 = False
                runningame1 = False
                runningame2 = False

            elif three_rectx <= x <= 420 and three_recttop <= y <= 340:
                start_screen = False
                runningame1 = True
                runningame2 = False
                running1 = False
                running2 = False

            elif four_rectx <= x <= 560 and four_recttop <= y <= 340:
                start_screen = False
                runningame2 = True
                runningame1 = False
                running1 = False
                running2 = False

        pygame.display.update()

    while runningame1:
        main_snake()
        runningame1 = False

    while runningame2:
        mmain()
        runningame2 = False

    pygame.quit()
    sys.exit

mainbastau()