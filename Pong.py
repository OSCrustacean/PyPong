import turtle
import time

#Window
width=1600 #800
height=1200 #600

scale_factor = int(width/800)

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

width_stretch_factor = 5 * scale_factor
len_stretch_factor = 1 * scale_factor

paddle_a = turtle.Turtle() #First Paddle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=width_stretch_factor, stretch_len=len_stretch_factor)
paddle_a.penup()
paddle_a.goto(-place_x, 0)

paddle_b = turtle.Turtle() #Second Paddle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=width_stretch_factor, stretch_len=len_stretch_factor)
paddle_b.penup()
paddle_b.goto(place_x, 0)

default_speed = int(half_width/65)
default_dy = half_height/150

ball = turtle.Turtle() #Ball
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.shapesize(stretch_wid=width/800, stretch_len=height/600)
ball.goto(0 , 0)
ball.dx = default_speed #Speed
ball.dy = default_dy #default 2

pen = turtle.Turtle() #Pen
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, place_y)
pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", (18 * scale_factor), "normal"))

#Functions
movement=int(half_height/6) #default ~35

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

buffer_value=half_height/6 #default 50 #half_height/6
upper_value=half_height + 1.25 * buffer_value #default 350 #half_height + 50
lower_value=upper_value - half_height/15 #default 340


def paddle_a_bounce():
    if (ball.xcor() < 0 and paddle_a.xcor() - ball.xcor() > ball.dx) and (ball.ycor() < paddle_a.ycor() + buffer_value and ball.ycor() > paddle_a.ycor() - buffer_value) or (ball.xcor() < -lower_value and ball.xcor() > -upper_value) and (ball.ycor() < paddle_a.ycor() + buffer_value and ball.ycor() > paddle_a.ycor() -buffer_value):
        ball.setx(-lower_value - 1)
        if ball.dx < (half_width/16):
            ball.dx -= 1 * scale_factor
            if ball.dy > 0:
                ball.dy += (1/3) * scale_factor
            if ball.dy < 0:
                ball.dy -= (1/3) * scale_factor
        ball.dx *= -1
    #if (ball.xcor() < -lower_value and ball.xcor() > -upper_value) and (ball.ycor() < paddle_a.ycor() + buffer_value and ball.ycor() > paddle_a.ycor() -buffer_value):
        #if ball.dx > -(half_width/16):
            #ball.dx -= 1 * scale_factor
            #ball.dy += (1/3) * scale_factor
        #ball.dx *= -1
    if paddle_a.ycor() > half_height - buffer_value: #keep paddle_a from going off top edge
        paddle_a.sety(half_height - buffer_value)
    if paddle_a.ycor() < -half_height + buffer_value: #keep paddle_a from going off bottom edge
        paddle_a.sety(-half_height + buffer_value)

def paddle_b_bounce():
    if (ball.xcor() > 0 and paddle_b.xcor() - ball.xcor() < ball.dx) and (ball.ycor() < paddle_a.ycor() + buffer_value and ball.ycor() > paddle_a.ycor() - buffer_value) or (ball.xcor() > lower_value and ball.xcor() < upper_value) and (ball.ycor() < paddle_b.ycor() + buffer_value and ball.ycor() > paddle_b.ycor() -buffer_value):
        ball.setx(lower_value + 1)
        if ball.dx < (half_width/16):
            ball.dx += 1 * scale_factor
            if ball.dy > 0:
                ball.dy += (1/3) * scale_factor
            if ball.dy < 0:
                ball.dy -= (1/3) * scale_factor
        ball.dx *= -1
    #if (ball.xcor() > lower_value and ball.xcor() < upper_value) and (ball.ycor() < paddle_b.ycor() + buffer_value and ball.ycor() > paddle_b.ycor() -buffer_value):
        #ball.setx(lower_value)
        #if ball.dx < (half_width/16):
            #ball.dx += 1 * scale_factor
            #ball.dy += (4/3) * scale_factor
        #ball.dx *= -1
    if paddle_b.ycor() > half_height - buffer_value: #keep paddle_b from going off top edge
        paddle_b.sety(half_height - buffer_value)
    if paddle_b.ycor() < -half_height + buffer_value: #keep paddle_b from going off bottom edge
        paddle_b.sety(-half_height + buffer_value)

paddle_b_y = 0

def paddle_b_player():
    global paddle_b_y
    global movement
    if ball.ycor() > paddle_b.ycor() + .75 * buffer_value:
        paddle_b_y += int(half_height/36)
    if ball.ycor() < paddle_b.ycor() - .75 * buffer_value:
        paddle_b_y -= int(half_height/36)
    if paddle_b_y > half_height - buffer_value: #keep from glitching on top edge
        paddle_b_y = half_height - buffer_value
    if paddle_b_y < - half_height + buffer_value: #keep from glitching on bottom edge
        paddle_b_y = - half_height + buffer_value
    paddle_b.goto(place_x, paddle_b_y)

def paddle_functions():
    paddle_a_bounce()
    paddle_b_bounce()
    paddle_b_player()

def reset_position():
    ball.goto(0, 0)
    paddle_a.sety(0)
    paddle_b.sety(0)
    if ball.dx > 0:
        side = 1
    if ball.dx < 0:
        side = -1
    ball.dx = default_speed * side
    ball.dy = default_dy
    paddle_b_y = 0
    time.sleep(1)

#Main loop
while True:
    wn.update()

    #paddle_functions()
    ball.setx(ball.xcor() + ball.dx) #Move ball
    ball.sety(ball.ycor() + ball.dy)
    
    #Edges
    if ball.ycor() > y_edge: #Top bounce
        ball.sety(y_edge)
        ball.dy *= -1

    if ball.ycor() < -y_edge: #Bottom bounce
        ball.sety(-y_edge)
        ball.dy *= -1

    if ball.xcor() > x_edge: #Right side; w/ width 800 = 390
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", (18 * scale_factor), "normal"))
        reset_position()


    if ball.xcor() < -x_edge: #Left side
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + "  " + "Player B: " + str(score_b), align="center", font=("Courier", (18 * scale_factor), "normal"))
        reset_position()

    #Paddles
    paddle_functions()

    #End game
    if score_a > 4:
        paddle_a.goto(-place_x, 0)
        paddle_b.goto(place_x, 0)
        pen.goto(0, buffer_value)
        pen.write(("Player A wins!"), align="center", font=("Courier", (24 * scale_factor), "normal"))
        time.sleep(5)
        break

    if score_b > 4:
        paddle_a.goto(-place_x, 0)
        paddle_b.goto(place_x, 0)
        pen.goto(0, buffer_value)
        pen.write(("Player B wins!"), align="center", font=("Courier", (24 * scale_factor), "normal"))
        time.sleep(5)
        break
