import turtle

#Window
width=800
height=600

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width, height)

#Score
score_a = 0
score_b = 0

#Objects
place_y=(width/2)-(width/16)
place_x=(height/2)-(height/10)

paddle_a = turtle.Turtle() #First Paddle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-place_y, 0)

paddle_b = turtle.Turtle() #Second Paddle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(place_y, 0)

ball = turtle.Turtle() #Ball
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0 , 0)
ball.dx = 6 #Speed
ball.dy = 2

pen = turtle.Turtle() #Pen
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, place_x)
pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

#Functions
movement=35

def paddle_a_up():
    y = paddle_a.ycor()
    y += movement
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= movement
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += movement
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= movement
    paddle_b.sety(y)

#Key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main loop
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx) #Move ball
    ball.sety(ball.ycor() + ball.dy)

    #Edges
    if ball.ycor() > 290: #Top bounce
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290: #Bottom bounce
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #Right side
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390: #Left side
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
