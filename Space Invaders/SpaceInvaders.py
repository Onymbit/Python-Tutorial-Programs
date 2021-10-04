import pygame as pg
import random
import math
from pygame import mixer
#Initiliaze Pygame
pg.init()
speed=100

#Create Screen
screen=pg.display.set_mode((800,600))

#Background
background=pg.image.load("background.png")

#Background Music
mixer.music.load("background.wav")
mixer.music.play(-1)
#Title and Icon
pg.display.set_caption("Space Invaders")
icon=pg.image.load("ufo.png")
pg.display.set_icon(icon)

#Player
playerImg=pg.image.load("player.png")
playerX=370
playerY=480
playerDX=0
playerD=0.15*speed
def player(x,y):
  screen.blit(playerImg,(x,y))

#Bullet: ready(no bullet on screen, fire(bullet is moving)
bulletImg=pg.image.load("bullet.png")
bulletX=0
bulletY=480
bulletDX=0
bulletDY=playerD*2
bulletState="ready"

def fire_bullet(x,y):
  global bulletState
  bulletState="fire"
  screen.blit(bulletImg,(x+16,y+10))

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyDY=[]
enemyDX=[]
enemyD=[]
numOfEnemies=6
for i in range(numOfEnemies):
  enemyImg.append(pg.image.load("enemy.png"))
  enemyX.append(random.randint(3,736))
  enemyY.append(random.randint(50,150))
  enemyDY.append(40)
  enemyDX.append(0.1*speed)
  enemyD.append(0.1*speed)
def enemy(x,y,i):
  screen.blit(enemyImg[i],(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
  distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
  if distance <27:
    return True
  else:
    return False

#Score
scoreValue=0
font=pg.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def showScore(x,y):
  score=font.render(f'Score: {scoreValue}',True,(255,255,255))
  screen.blit(score,(x,y))

#Game Over Text
overFont=pg.font.Font('freesansbold.ttf',64)

def game_over_text():
  over_text=overFont.render('GAME OVER',True,(255,255,255))
  screen.blit(over_text,(200,250))
#Game Loop
running=True
while running:

  screen.fill((0,0,0))
  screen.blit(background,(0,0))
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
    
    if event.type==pg.KEYDOWN:
      if event.key==pg.K_a:
        playerDX+=-playerD
      if event.key==pg.K_d:
        playerDX+=playerD
      if event.key==pg.K_SPACE:
        if bulletState=="ready":
          bulletSound=mixer.Sound('laser.wav')
          bulletSound.play()
          bulletX=playerX
          fire_bullet(bulletX,bulletY)
    if event.type==pg.KEYUP:
      if event.key==pg.K_a:
        playerDX+=playerD
      if event.key==pg.K_d:
        playerDX+=-playerD

  
  playerX+=playerDX



  #Bullet Movement
  if bulletY <= -32:
    bulletState="ready"
    bulletY=480
  if bulletState == "fire":
    fire_bullet(bulletX,bulletY)
    bulletY-=bulletDY
  
  for i in range(numOfEnemies):

    #Game Over
    if enemyY[i]>440:
      for j in range(numOfEnemies):
        enemyY[j]=2000
      game_over_text()
      break


    enemyX[i]+=enemyDX[i]
    if enemyX[i]<=0:
      enemyDX[i]=enemyD[i]
      enemyY+=enemyDY
    if enemyX[i]>=736:
      enemyDX[i]=-enemyD[i]
      enemyY[i]+=enemyDY[i]
    collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    if collision:
      explosionSound=mixer.Sound('explosion.wav')
      explosionSound.play()
      bulletY=480
      bulletState="ready"
      scoreValue+=1
      enemyX[i]=random.randint(3,736)
      enemyY[i]=random.randint(50,150)
    enemy(enemyX[i],enemyY[i],i)

  if playerX<=0:
    playerX=0
  if playerX>=736:
    playerX=736

  player(playerX,playerY)
  showScore(textX,textY)
  pg.display.update()
pg.quit()
