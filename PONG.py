import turtle
win=turtle.Screen()
win.title("PONG-Made By Ishan")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)
#Paddle A code
PadA=turtle.Turtle()
PadA.speed(0)
PadA.shape("square")
PadA.color("blue")
PadA.penup()
PadA.goto(-350,0)
PadA.shapesize(stretch_wid=5,stretch_len=1)
#Paddle A code
PadB=turtle.Turtle()
PadB.speed(0)
PadB.shape("square")
PadB.color("red")
PadB.penup()
PadB.goto(350,0)
PadB.shapesize(stretch_wid=5,stretch_len=1)
#Ball Code
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx=1.1
Ball.dy=1.1
magic_marker = turtle.Turtle() 

FONT = ("Arial", 12, "bold")

def paddleAup():
    y=PadA.ycor()
    y+=30
    PadA.sety(y)

def paddleAdown():
    y=PadA.ycor()
    y-=30
    PadA.sety(y)

def paddleBup():
    y=PadB.ycor()
    y+=30
    PadB.sety(y)

def paddleBdown():
    y=PadB.ycor()
    y-=20
    PadB.sety(y)

win.listen()
win.onkeypress(paddleAup,"w")
win.onkeypress(paddleAdown,"s")
win.onkeypress(paddleAup,"Up")
win.onkeypress(paddleAdown,"Down")

while True:
    win.update()
    turtle.write("PONG", move=False, align="left", font=("Arial", 8, "normal"))
    #magic_marker.write("PONG", align="top", font=FONT)
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)
    


    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1

    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1

    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx*=-1

    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx*=-1

    if (Ball.xcor()>340 and Ball.xcor()<350) and (Ball.ycor()<PadB.ycor()+40 and Ball.ycor() > PadB.ycor()-50):
        Ball.setx(340)
        Ball.dx*=-1

    if(Ball.xcor()>340):
        paddleBup()

   
 


