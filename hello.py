
import pygame
import time
import sys
import random
pygame.init()
#color
white=(255,255,255)
black=(0,0,0)
grey=(119,118,110)
red=(200,0,0)
bright_red=(255,0,0)
green=(0,200,0)
bright_green=(0,255,0)
blue=(0,0,255)
window_width=800
window_hight=600
l=[]
#display surface
wd=pygame.display.set_mode((window_width,window_hight))
carimg=pygame.image.load('Screenshot (209).jpg')
car1=pygame.transform.scale(carimg,(100,100))
clock=pygame.time.Clock()

def message(mess,colour,size,x,y):
     font=pygame.font.SysFont(None,size)
     screen_text=font.render(mess,True,colour)
     wd.blit(screen_text,(x,y))
     pygame.display.update()
def load(name,x_pos,y_pos):
    v = pygame.image.load(name)
    wd.blit(v, (x_pos, y_pos))
    pygame.display.update()
def button(x,y,w,h,mess,mess_color,actc,noc,size,tx,ty,func):
    mouse = pygame.mouse.get_pos()
    click=  pygame.mouse.get_pressed()
    if x < mouse[0] < x+w and y < mouse[1] < y+h:

        pygame.draw.rect(wd, actc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func()

    else:
        pygame.draw.rect(wd, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()
def quit1():
    pygame.quit()
    quit()

def game_intro():

  load('background 1.png', 0, 0)
  gameintro=False
  while gameintro==False:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gameintro = True
            game_over=True

    window_width = 800
    window_hight = 600


    message('MAIN MENU',green,100,(window_width/2 - 220),100)
    button(100, 400, 70, 30, 'GO!', white, bright_red, red,25,106,406,gameloop)
    button(600, 400, 70, 30, 'QUIT', white, bright_green, green,25,606,406,quit1)

    pygame.display.update()



  pygame.display.update()

def back():
    blue_strip=pygame.image.load('road.png')
    img=pygame.transform.scale(blue_strip,(100,600))
    wd.blit(img,(0,0))
    wd.blit(img,(700,0))
def crash(x):
    if x<90  or x+90>700:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('game_over', True, white)
        wd.blit(screen_text, (250, 280))
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for j in pygame.event.get():
            if j.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def car_crash(x,y,y_en,x_en):

    if x<x_en+57<x+150 and (y<y_en+100<y+100 or y<y_en<y+100):
        message('CRASHED!', red, 100, 250, 280)
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()




def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    wd.blit(screen_text, (0, 0))
    pygame.display.update()

def other_car(y_en):
    enmy1=pygame.image.load('Screenshot (209).jpg')
    enmy=pygame.transform.scale(enmy1,(70,100))
    global  x_en
    if y_en==0:
      x_en=random.randrange(100,600)
      l.clear()
      l.append(x_en)
    else:
      x_en=l[0]
    wd.blit(enmy,(x_en,y_en))
    pygame.display.update()


def gameloop():

     x = 300
     y = 400
     x_change = 0
     y_change = 0
     global game_over
     game_over=False

     count = 0
     y_en=0
     while game_over==False:
         for i in pygame.event.get():
                 if i.type==pygame.QUIT:
                     game_over=True
                 if i.type==pygame.KEYDOWN:
                     if i.key==pygame.K_LEFT:
                         x_change=-10
                     elif i.key==pygame.K_RIGHT:
                         x_change=+10
                 if i.type==pygame.KEYUP:
                     if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                         x_change=0

         x+=x_change


         wd.fill(grey)

         back()
         wd.blit(car1, (x, y))
         if y_en>600:
           y_en=0
           count += 1
         other_car(y_en)
         y_en+=10
         crash(x)
         car_crash(x,y,y_en,x_en)
         score(count)



         clock.tick(30)
         pygame.display.update()


game_intro()
pygame.quit()
quit()