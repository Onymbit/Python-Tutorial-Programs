#Pong
import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong by @Onymbit")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
scoreA=0
scoreB=0

#Paddle A
paddleA=turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#Paddle B
paddleB=turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0",align="center",font=("Courier",20,"normal"))


#Functions
def paddleAUp():
  y=paddleA.ycor()
  if y>=230:
    y=250
  else:
    y+=20
  paddleA.sety(y)
def paddleADown():
  y=paddleA.ycor()
  if y<=-230:
    y=-250
  else:
    y-=20
  paddleA.sety(y)
def paddleBUp():
  y=paddleB.ycor()
  if y>=230:
    y=250
  else:
    y+=20
  paddleB.sety(y)
def paddleBDown():
  y=paddleB.ycor()
  if y<=-230:
    y=-250
  else:
    y-=20
  paddleB.sety(y)


#Keyboard Binding
wn.listen()
wn.onkeypress(paddleAUp,"w")
wn.onkeypress(paddleADown,"s")
wn.onkeypress(paddleBUp,"Up")
wn.onkeypress(paddleBDown,"Down")


#Main Game Loop
while True:
  wn.update()

  #Move Ball
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)

  #Border Checking
  if ball.ycor()>290:
    ball.sety(290)
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    ball.dy*=-1
  if ball.ycor()<-290:
    ball.sety(-290)
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    ball.dy*=-1
  if ball.xcor()>390:
    ball.goto(0,0)
    ball.dx*=-1
    scoreA+=1
    pen.clear()
    pen.write(f'Player A: {scoreA} PlayerB: {scoreB}',align="center",font=("Courier",20,"normal"))
  if ball.xcor()<-390:
    ball.goto(0,0)
    ball.dx*=-1
    scoreB+=1
    pen.clear()
    pen.write(f'Player A: {scoreA} PlayerB: {scoreB}',align="center",font=("Courier",20,"normal"))
  
  #Paddle collisions
  if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddleB.ycor()+40 and ball.ycor()>paddleB.ycor()-40):
    ball.setx(340)
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    ball.dx*=-1
  if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddleA.ycor()+40 and ball.ycor()>paddleA.ycor()-40):
    ball.setx(-340)
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    ball.dx*=-1
  
