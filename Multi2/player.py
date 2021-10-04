import pygame as pg
class Player():
  def __init__(self,x,y,width,height,color):
    self.y=y
    self.x=x
    self.width=width
    self.height=height
    self.color=color
    self.rect=(x,y,width,height)
    self.vel=3

  def draw(self,win):
    pg.draw.rect(win,self.color,self.rect)
  def move(self):
    keys=pg.key.get_pressed()
    
    if keys[pg.K_a]:
      self.x-=self.vel
    if keys[pg.K_d]:
      self.x+=self.vel  
    if keys[pg.K_w]:
      self.y-=self.vel
    if keys[pg.K_s]:
      self.y+=self.vel
    
    self.update()
    
  def update(self):
    self.rect=(self.x,self.y,self.width,self.height)