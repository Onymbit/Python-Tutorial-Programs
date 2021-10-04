import numpy as np
import pygame as pg
import math

ROW_COUNT=6
COLUMN_COUNT=7
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)


def create_board():
  board= np.zeros((ROW_COUNT,COLUMN_COUNT))
  return board

def drop_piece(board,row,col,piece):
  board[row][col]=piece
def is_valid_location(board,col):
  return board[ROW_COUNT-1][col]==0
def get_next_open_row(baord,col):
  for r in range(ROW_COUNT):
    if board[r][col]==0:
      return r
def print_board(board):
  print(np.flip(board,0))

def winning_move(board,piece):
  for c in range(COLUMN_COUNT-3):
    for r in range(ROW_COUNT):
      if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
        return True
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT-3):
      if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
        return True
  for c in range(COLUMN_COUNT-3):
    for r in range(ROW_COUNT-3):
      if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
        return True 
  for c in range(COLUMN_COUNT-3):
    for r in range(3,ROW_COUNT):
      if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
        return True     

def draw_board(board):
  for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT):
      pg.draw.rect(screen,BLUE,(c*SQUARE_SIZE,r*SQUARE_SIZE+SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
      if board[-(r+1)][c]==0:
        pg.draw.circle(screen,BLACK,(int(c*SQUARE_SIZE+SQUARE_SIZE/2),int(r*SQUARE_SIZE+SQUARE_SIZE*3/2)),RADIUS)
      elif board[-(r+1)][c]==1:
        pg.draw.circle(screen,RED,(int(c*SQUARE_SIZE+SQUARE_SIZE/2),int(r*SQUARE_SIZE+SQUARE_SIZE*3/2)),RADIUS)
      elif board[-(r+1)][c]==2:
        pg.draw.circle(screen,YELLOW,(int(c*SQUARE_SIZE+SQUARE_SIZE/2),int(r*SQUARE_SIZE+SQUARE_SIZE*3/2)),RADIUS)

board=create_board()
game_over=False
#print_board(board)
turn=True

pg.init()
SQUARE_SIZE=100
width=COLUMN_COUNT*SQUARE_SIZE
height=(ROW_COUNT+1)*SQUARE_SIZE
RADIUS=int(SQUARE_SIZE/2-5)
screen=pg.display.set_mode((width,height))
draw_board(board)
pg.display.update()
font=pg.font.Font('freesansbold.ttf',75)

while not game_over:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      pg.quit()
    if event.type==pg.MOUSEMOTION:
      x=event.pos[0]
      pg.draw.rect(screen,BLACK,(0,0,width,SQUARE_SIZE))
      if turn:
        pg.draw.circle(screen,RED,(x,int(SQUARE_SIZE/2)),RADIUS)
      else:
        pg.draw.circle(screen,YELLOW,(x,int(SQUARE_SIZE/2)),RADIUS)
    if event.type==pg.MOUSEBUTTONDOWN:
      #Ask Player 1
      if turn:
        col=int(math.floor(x/SQUARE_SIZE))
        if is_valid_location(board,col):
          row=get_next_open_row(board,col)
          drop_piece(board,row,col,1)
          turn= not turn
          pg.draw.rect(screen,BLACK,(0,0,width,SQUARE_SIZE))
          if turn:
            pg.draw.circle(screen,RED,(x,int(SQUARE_SIZE/2)),RADIUS)
          else:
            pg.draw.circle(screen,YELLOW,(x,int(SQUARE_SIZE/2)),RADIUS)
        if winning_move(board,1):
          pg.draw.rect(screen,BLACK,(0,0,width,SQUARE_SIZE))
          label=font.render("Player 1 wins!!",True,(255,255,255))
          screen.blit(label,(80,10))
          game_over=True
      #Ask Player 2
      else:
        col=int(math.floor(x/SQUARE_SIZE))
        if is_valid_location(board,col):
          row=get_next_open_row(board,col)
          drop_piece(board,row,col,2)
          turn= not turn
          pg.draw.rect(screen,BLACK,(0,0,width,SQUARE_SIZE))
          if turn:
            pg.draw.circle(screen,RED,(x,int(SQUARE_SIZE/2)),RADIUS)
          else:
            pg.draw.circle(screen,YELLOW,(x,int(SQUARE_SIZE/2)),RADIUS)
        if winning_move(board,2):
          pg.draw.rect(screen,BLACK,(0,0,width,SQUARE_SIZE))
          label=font.render("Player 1 wins!!",True,(255,255,255))
          screen.blit(label,(80,10))
          game_over=True

      #print_board(board)
  draw_board(board)
  pg.display.update()
  if game_over:
    pg.time.wait(3000)
pg.quit()
  
