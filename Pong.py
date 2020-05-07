import turtle

#Window
width=1600 #800
height=1200 #600

half_width=width/2
half_height=height/2

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width, height)

#Score
score_a = 0
score_b = 0

#Objects
place_x=half_width-(width/16) ##for width 800; 350
place_y=half_height-(height/10) ##for height 600; 240

paddle_a = turtle.Turtle() #First Paddle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-place_x, 0)

paddle_b = turtle.Turtle() #Second Paddle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(place_x, 0)

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
pen.goto(0, place_y)
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

#Edge Coords
y_edge=half_height-(height/60) #default height 600;290
x_edge=half_width-(width/80) #default width 800; 390

buffer_value=50 #default 50 #half_height/6
upper_value=place_x #default 350 #half_height + 50
lower_value=upper_value-10 #default 340

#Main loop
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx) #Move ball
    ball.sety(ball.ycor() + ball.dy)

    #Edges
    if ball.ycor() > y_edge: #Top bounce
        ball.sety(y_edge)
        ball.dy *= -1

    if ball.ycor() < -y_edge: #Bottom bounce
        ball.sety(-y_edge)
        ball.dy *= -1

    if ball.xcor() > x_edge: #Right side; w/ width 800 = 390
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -x_edge: #Left side
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    #Paddles
    if (ball.xcor() < -lower_value and ball.xcor() > -upper_value) and (ball.ycor() < paddle_a.ycor() + buffer_value and ball.ycor() > paddle_a.ycor() -buffer_value):
        ball.setx(-lower_value)
        ball.dx *= -1

    if (ball.xcor() > lower_value and ball.xcor() < upper_value) and (ball.ycor() < paddle_b.ycor() + buffer_value and ball.ycor() > paddle_b.ycor() -buffer_value):
        ball.setx(lower_value)
        ball.dx *= -1
