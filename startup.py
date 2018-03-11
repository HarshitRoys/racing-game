import pygame
from pygame.locals import *
import time
import random
import sys
import os
os.getcwd()
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
crash_Sound=pygame.mixer.Sound("crash.ogg")
pygame.mixer.music.load("music.ogg")
display_width=800
display_height=600
clock=pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS']="50,50"
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
car_width=56
gray=(128,128,128)
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('CAR GAME')
carimg=pygame.image.load("car7.jpg")
background=pygame.image.load("download12.jpg").convert()
start_page_background=pygame.image.load("background.jpg")
start_page_background1=pygame.image.load("background2.jpg")
strip=pygame.image.load("strip.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
pause=False


def things_dodged(count,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("DODGED:"+ str(count),True, black)
    score=font.render('SCORE:'+str(score),True,red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))


def things(thing_startx,thing_starty,obs):
    if obs==0:
        obstacle_image=pygame.image.load('car.jpg')
    elif obs==1:
        obstacle_image=pygame.image.load('car1.jpg')
    elif obs==2:
        obstacle_image=pygame.image.load('car2.jpg')
    elif obs==3:
        obstacle_image=pygame.image.load('car3.jpg')
    elif obs==4:
        obstacle_image=pygame.image.load('car4.jpg')
    elif obs==5:
        obstacle_image=pygame.image.load('car5.jpg')
    elif obs==6:
        obstacle_image=pygame.image.load('car6.jpg')
    elif obs==7:
        obstacle_image=pygame.image.load('car7.jpg')
    elif obs==8:
        obstacle_image=pygame.image.load('car8.jpg')
    elif obs==9:
        obstacle_image=pygame.image.load('car.jpg')
    gamedisplay.blit(obstacle_image,(thing_startx,thing_starty))


def car(x,y):
    gamedisplay.blit(carimg,(x,y))


def text_object(text,font):
    TextSurface=font.render(text,True,black)
    return TextSurface,TextSurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect=text_object(text,largetext)
    TextRect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def  crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_Sound)
    pygame.draw.rect(gamedisplay,bright_green,(650,400,100,50))
    pygame.draw.rect(gamedisplay,bright_green,(60,400,100,50))
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    textsurf,textrect=text_object("<<<<",smalltext)
    textrect.center=(110,425)
    gamedisplay.blit(textsurf,textrect)
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    atextsurf,atextrect=text_object(">>>>",smalltext)
    atextrect.center=(700,425)
    gamedisplay.blit(atextsurf,atextrect)
    message_display('OUCH!!!')
    pygame.draw.rect(gamedisplay,green,(700,300,60,60))
    pygame.draw.rect(gamedisplay,red,(42,300,60,60))


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                count_down()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="unpause":
                unpaused()
            elif action=="pause":
                paused()

    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_object(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(textsurf,textrect)



def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(start_page_background1,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_object("This is an car game in which you need dodge the coming cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_object("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplay.blit(TextSurf,TextRect)
        gamedisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_object("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_object("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_object("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_object("B : BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        ptextSurf,ptextRect=text_object("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_object("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplay.blit(sTextSurf,sTextRect)
        gamedisplay.blit(stextSurf,stextRect)
        gamedisplay.blit(hTextSurf,hTextRect)
        gamedisplay.blit(atextSurf,atextRect)
        gamedisplay.blit(rtextSurf,rtextRect)
        gamedisplay.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause= False


def paused():
    global pause
    pygame.mixer.music.pause()
    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplay.blit(start_page_background1,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)



def artificial_set():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.7)
    gamedisplay.blit(background,(0,0))
    gamedisplay.blit(background,(0,200))
    gamedisplay.blit(background,(0,400))
    gamedisplay.blit(background,(700,0))
    gamedisplay.blit(background,(700,200))
    gamedisplay.blit(background,(700,400))
    gamedisplay.blit(strip,(400,100))
    gamedisplay.blit(strip,(400,200))
    gamedisplay.blit(strip,(400,300))
    gamedisplay.blit(strip,(400,400))
    gamedisplay.blit(strip,(400,100))
    gamedisplay.blit(strip,(400,500))
    gamedisplay.blit(strip,(400,0))
    gamedisplay.blit(strip,(400,600))
    gamedisplay.blit(yellow_strip,(120,200))
    gamedisplay.blit(yellow_strip,(120,0))
    gamedisplay.blit(yellow_strip,(120,100))
    gamedisplay.blit(yellow_strip,(680,100))
    gamedisplay.blit(yellow_strip,(680,0))
    gamedisplay.blit(yellow_strip,(680,200))
    gamedisplay.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))
    pygame.draw.rect(gamedisplay,bright_green,(650,400,100,50))
    pygame.draw.rect(gamedisplay,bright_green,(60,400,100,50))
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    textsurf,textrect=text_object("<<<<",smalltext)
    textrect.center=(110,425)
    gamedisplay.blit(textsurf,textrect)
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    atextsurf,atextrect=text_object(">>>>",smalltext)
    atextrect.center=(700,425)
    gamedisplay.blit(atextsurf,atextrect)
    pygame.draw.rect(gamedisplay,green,(700,300,60,60))
    pygame.draw.rect(gamedisplay,red,(42,300,60,60))
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    textsurf,textrect=text_object("B",smalltext)
    textrect.center=(75,325)
    gamedisplay.blit(textsurf,textrect)
    smalltext=pygame.font.Font("freesansbold.ttf",30)
    textsurf,textrect=text_object("G",smalltext)
    textrect.center=(730,325)
    gamedisplay.blit(textsurf,textrect)

def count_down():
    countdown=True
    pygame.mixer.music.play(-1)
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplay.fill(gray)
            artificial_set()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            artificial_set()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            artificial_set()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            artificial_set()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()



def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(start_page_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_object("CAR GAME",largetext)
        TextRect.center=(400,100)
        gamedisplay.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)



def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.7)
    x1=(display_width*0.45)
    y1=(display_height*0.8)
    thing_speed=9
    obs=0
    x_change=0
    y_change=0
    thing_startx=random.randrange(200,(display_width-200))
    thing_starty=-750
    thing_width=56
    thing_height=125
    dodged=0
    score=0
    level=0
    x2=7
    fps=120
    gamexit=False
    while not gamexit:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_a:
                    thing_speed=thing_speed+1
                if event.key==pygame.K_b:
                    thing_speed=thing_speed-3
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        gamedisplay.fill(gray)
        rel_x=x2 % background.get_rect().width
        gamedisplay.blit(background,(0,rel_x - background.get_rect().width))
        gamedisplay.blit(background,(700,rel_x - background.get_rect().width))
        if rel_x<800:
            gamedisplay.blit(background,(0,rel_x))
            gamedisplay.blit(background,(700,rel_x))
            gamedisplay.blit(strip,(400,rel_x))
            gamedisplay.blit(strip,(400,rel_x+100))
            gamedisplay.blit(strip,(400,rel_x+200))
            gamedisplay.blit(strip,(400,rel_x+300))
            gamedisplay.blit(strip,(400,rel_x+400))
            gamedisplay.blit(strip,(400,rel_x+500))
            gamedisplay.blit(strip,(400,rel_x-100))
            gamedisplay.blit(yellow_strip,(120,rel_x-200))
            gamedisplay.blit(yellow_strip,(120,rel_x+20))
            gamedisplay.blit(yellow_strip,(120,rel_x+30))
            gamedisplay.blit(yellow_strip,(680,rel_x-100))
            gamedisplay.blit(yellow_strip,(680,rel_x+20))
            gamedisplay.blit(yellow_strip,(680,rel_x+30))

        x2+=thing_speed
        pause=True
        thing_starty-=(thing_speed/4)
        things(thing_startx,thing_starty,obs)
        thing_starty+=thing_speed
        car(x,y)
        things_dodged(dodged,score)

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 60+100>mouse[0]>60 and 400+50>mouse[1]>400:
            pygame.draw.rect(gamedisplay,green,(60,400,100,50))
            if click[0]==1:
                x_change-=1
            elif click[0]==0:
                x_change=0
        else:
            pygame.draw.rect(gamedisplay,bright_green,(60,400,100,50))
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurf,textrect=text_object("<<<<",smalltext)
        textrect.center=(110,425)
        gamedisplay.blit(textsurf,textrect)
        if 650+100>mouse[0]>650 and 400+50>mouse[1]>400:
            pygame.draw.rect(gamedisplay,green,(650,400,100,50))
            if click[0]==1:
                x_change=5
            elif click[0]==0:
                x_change=0
        else:
            pygame.draw.rect(gamedisplay,bright_green,(650,400,100,50))
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurf,textrect=text_object(">>>>",smalltext)
        textrect.center=(700,425)
        gamedisplay.blit(textsurf,textrect)
        if 700+60>mouse[0]>700 and 300+60>mouse[1]>300:
            pygame.draw.rect(gamedisplay,green,(700,300,60,60))
            if click[0]==1:
                thing_speed=thing_speed+0.5
            elif click[0]==0:
                thing_speed=thing_speed
        else:
            pygame.draw.rect(gamedisplay,green,(700,300,60,60))
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurf,textrect=text_object("G",smalltext)
        textrect.center=(730,325)
        gamedisplay.blit(textsurf,textrect)
        if 42+60>mouse[0]>42 and 300+60>mouse[1]>300:
            pygame.draw.rect(gamedisplay,red,(42,300,60,60))
            if click[0]==1:
                thing_speed=thing_speed-0.5
            elif click[0]==0:
                thing_speed=thing_speed
        else:
            pygame.draw.rect(gamedisplay,red,(42,300,60,60))
        smalltext=pygame.font.Font("freesansbold.ttf",30)
        textsurf,textrect=text_object("B",smalltext)
        textrect.center=(75,325)
        gamedisplay.blit(textsurf,textrect)

        if x>display_width-(car_width+110) or x<110:
            crash()
        if thing_starty>display_height:
            thing_starty=0-thing_height
            y1=-10
            thing_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,10)
            dodged=dodged+1
            score=dodged*10
            if int(dodged) % 10==0:
                level=level+1
                thing_speed=thing_speed+2
                largetext=pygame.font.Font('freesansbold.ttf',100)
                TextSurf,TextRect=text_object("LEVEL "+str(level),largetext)
                TextRect.center=((display_width/2),(display_height/2))
                gamedisplay.blit(TextSurf,TextRect)
                pygame.display.update()
                time.sleep(2)
        if y<thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                crash()

        button("PAUSE",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
button()
count_down()
game_loop()
pygame.quit()
quit()
