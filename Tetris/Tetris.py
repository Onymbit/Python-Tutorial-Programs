import pygame as pg
import random
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pg.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
 
 
class Piece(object):
  def __init__(self,x,y,shape):
    self.x=x
    self.y=y
    self.shape=shape
    self.color=shape_colors[shapes.index(shape)]
    self.rotation=0
 
def create_grid(locked_positions={}):
  grid=[[(0,0,0) for _ in range(10)] for _ in range(20)]

  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if(j,i) in locked_positions:
        c=locked_positions[(j,i)]
        grid[i][j]=c
  return grid
 
def convert_shape_format(shape):
  positions=[]
  format1=shape.shape[shape.rotation%len(shape.shape)]

  for i,line in enumerate(format1):
    row=list(line)
    for j,column in enumerate(row):
      if column== '0':
        positions.append((shape.x+j,shape.y+i))
  for i,pos in enumerate(positions):
    positions[i]=(pos[0]-2,pos[1]-4)
  return positions
 
def valid_space(shape, grid):
  accepted_pos=[[(j,i) for j in range(10) if grid[i][j]==(0,0,0)] for i in range(20)]
  accepted_pos=[j for sub in accepted_pos for j in sub]

  formatted=convert_shape_format(shape)

  for pos in formatted:
    if pos not in accepted_pos:
      if pos[1]>-1:
        return False
  return True
 
def check_lost(positions):
  for pos in positions:
    x,y=pos
    if y<1:
      return True
  return False

 
def get_shape():
  return Piece(5,0,random.choice(shapes))
 
def draw_text_middle(text, size, color, surface):
  font=pg.font.SysFont('comicsans',size,bold=True)
  label=font.render(text,1,color)

  surface.blit(label,(top_left_x+play_width/2-(label.get_width()/2),top_left_y+play_height/2-label.get_height()/2))
   
def draw_grid(surface, grid):
  sx=top_left_x
  sy=top_left_y
  for i in range(len(grid)):
    pg.draw.line(surface,(128,128,128),(sx,sy+i*block_size),(sx+play_width,sy+i*block_size))
    for j in range(len(grid[i])+1):
      pg.draw.line(surface,(128,128,128),(sx+j*block_size,sy),(sx+j*block_size,sy+play_height))

  
 
def clear_rows(grid, locked):
  inc =0
  for i in range(len(grid)-1,-1,-1):
    row=grid[i]
    if (0,0,0) not in row:
      inc+=1
      ind=i
      for j in range(len(row)):
        try:
          del locked[(j,i)]
        except:
          continue
  if inc>0:
    for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
      x,y=key
      if y<ind:
        newKey=(x,y+inc)
        locked[newKey]=locked.pop(key)
  return inc

 
def draw_next_shape(shape, surface):
  font=pg.font.SysFont('comicsans',30)
  label=font.render("Next Shape:",1,(255,255,255))

  sx=top_left_x+play_width+50
  sy=top_left_y+play_height/2-100
  format1=shape.shape[shape.rotation%len(shape.shape)]
  
  for i,line in enumerate(format1):
    row=list(line)
    for j,column in enumerate(row):
      if column=='0':
        pg.draw.rect(surface,shape.color,(sx+j*block_size,sy+i*block_size,block_size,block_size))
  surface.blit(label,(sx+int(block_size/3),sy-block_size))
def update_score(score):
  t_score=max_score()
  with open('scores.txt','w') as f:
    if t_score>score:
      f.write(str(t_score))
    else:
      f.write(str(score))
def max_score():
  with open('scores.txt','r') as f:
    lines=f.readlines()
    score=int(lines[0].strip())
  return score

 
def draw_window(surface,grid,score,last_score):
  surface.fill((0,0,0))
  pg.font.init()
  font=pg.font.SysFont('comicsans',60)
  label=font.render('Tetris',True,(255,255,255))
  surface.blit(label,(top_left_x + play_width/2-label.get_width()/2,30))
  
  font=pg.font.SysFont('comicsans',30)
  label=font.render(f'Score: {score}',1,(255,255,255))

  sx=top_left_x+play_width+70
  sy=top_left_y+play_height/2+60
  
  surface.blit(label,(sx,sy))

  label=font.render(f'High Score: {last_score}',1,(255,255,255))

  sx=top_left_x-200
  sy=top_left_y+play_height/2+60
  surface.blit(label,(sx,sy))
  
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      pg.draw.rect(surface,grid[i][j],(top_left_x+j*block_size,top_left_y+i*block_size,block_size,block_size),0)

  pg.draw.rect(surface,(255,0,0),(top_left_x,top_left_y,play_width,play_height),4)

  draw_grid(surface,grid)
  
 
def main(win):
  last_score=max_score()
  locked_positions={}
  grid=create_grid(locked_positions)

  change_piece=False
  run=True
  current_piece=get_shape()
  next_piece=get_shape()
  clock=pg.time.Clock()
  fall_time=0
  fall_speed=0.27
  level_time=0
  score=0

  while run:
    grid=create_grid(locked_positions)
    fall_time+=clock.get_rawtime()
    level_time+=clock.get_rawtime()
    clock.tick()
    
    if level_time/1000>5:
      level_time=0
      if fall_speed>0.12:
        fall_speed-=0.005

    if fall_time/1000>fall_speed:
      fall_time=0
      current_piece.y+=1
      if not(valid_space(current_piece,grid)) and current_piece.y>0:
        current_piece.y-=1
        change_piece=True


    for event in pg.event.get():
      if event.type==pg.QUIT:
        run=False
        pg.display.quit()
        
      if event.type==pg.KEYDOWN:
        if event.key==pg.K_a:
          current_piece.x-=1
          if not valid_space(current_piece,grid):
            current_piece.x+=1
        if event.key==pg.K_d:
          current_piece.x+=1
          if not valid_space(current_piece,grid):
            current_piece.x-=1
        if event.key==pg.K_w:
          current_piece.rotation+=1
          if not valid_space(current_piece,grid):
            current_piece.rotation-=1

        if event.key==pg.K_s:
          current_piece.y+=1
          if not valid_space(current_piece,grid):
            current_piece.y-=1
    
    shape_pos=convert_shape_format(current_piece)

    for i in range(len(shape_pos)):
      x,y=shape_pos[i]
      if y>-1:
        grid[y][x]=current_piece.color
    if change_piece:
      for pos in shape_pos:
        p=(pos[0],pos[1])
        locked_positions[p]=current_piece.color
      current_piece=next_piece
      next_piece=get_shape()
      change_piece=False
      score+=clear_rows(grid,locked_positions)*10

    
    draw_window(win,grid,score,last_score)
    draw_next_shape(next_piece,win)
    pg.display.update()
    if check_lost(locked_positions):
      draw_text_middle("YOU LOST!",80,(255,255,255),win)
      pg.display.update()
      pg.time.delay(1500)
      run=False
      update_score(score)
  

def main_menu(win):
  run=True
  while run:
    win.fill((0,0,0))
    draw_text_middle('Press Any Key To Play',60,(255,255,255),win)
    pg.display.update()
    for event in pg.event.get():
      if event.type==pg.QUIT:
        run=False
      if event.type==pg.KEYDOWN:
        main(win)
  pg.display.quit()

win=pg.display.set_mode((s_width,s_height))
pg.display.set_caption('Tetris')
icon=pg.image.load('tetris.png')
#<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
pg.display.set_icon(icon)
main_menu(win)  # start game


