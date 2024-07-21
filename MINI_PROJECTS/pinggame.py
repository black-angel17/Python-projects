import turtle
import time

wn = turtle.Screen()

wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#main this open the screenn infinite
#now i need to update the screen for some time

#pad A

pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.shapesize(stretch_len=1,stretch_wid=5)
pad_a.color("white")
pad_a.penup()
pad_a.goto(-350 , 0)

#pad B

pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.shapesize(stretch_len=1,stretch_wid=5)
pad_b.color("white")
pad_b.penup()
pad_b.goto(+350 , 0)



#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.05
ball.dy =0.05

#to move pad a
def pad_b_up():
    y = pad_b.ycor()
    y+=20
    pad_b.sety(y)
def pad_b_down():
    y = pad_b.ycor()
    y-=20
    pad_b.sety(y)

def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


#keyboard binds
wn.listen()
wn.onkeypress(pad_a_up, 'w')
wn.onkeypress(pad_a_down, 's')
wn.onkeypress(pad_b_up, 'Up')
wn.onkeypress(pad_b_down, 'Down')



while True:
    wn.update()
    #update ball location coordinations

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check corner
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy* -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if  ball.xcor() > 390:
        ball.setx(390)
        ball.dx = ball.dx* -1

    if  ball.xcor() < -390:
        ball.setx(-390)
        ball.dx = ball.dx* -1

    if ball.xcor() > 340 :
        ball.dx = ball.dy * -1
    if ball.ycor() > 200:
        ball.dy = ball.dy * -1