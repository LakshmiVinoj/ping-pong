import turtle

# screen design
ds = turtle.Screen()
ds.title("The classic Ping Pong")
ds.bgcolor("white")
ds.setup(width=800, height=600)
ds.tracer(0)

###############################################################

# player and ball design

# player 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(stretch_wid=3.5, stretch_len=0.5)
p1.color("blue")
p1.up()
p1.goto(-350, 0)

# player 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(stretch_wid=3.5, stretch_len=0.5)
p2.color("red")
p2.up()
p2.goto(350, 0)

# ball
ppball = turtle.Turtle()
ppball.speed(0)
ppball.shape("circle")
ppball.color("black")
ppball.up()
ppball.goto(0, 0)
ppball.xaxis = 0.2
ppball.yaxis = -0.2

# score board
sb = turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0,260)
sb.write("P1: 0 VS P2:0", align = "center", font=("arial", 20, "bold"))
p1_score=0 #initialising
p2_score=0 #initialising


########################################################################

# player movement

# up
def p1_up():
    y_cor = p1.ycor()
    y_cor += 19
    p1.sety(y_cor)


def p2_up():
    y_cor = p2.ycor()
    y_cor += 19
    p2.sety(y_cor)


# down
def p1_down():
    y_cor = p1.ycor()
    y_cor -= 19
    p1.sety(y_cor)


def p2_down():
    y_cor = p2.ycor()
    y_cor -= 19
    p2.sety(y_cor)


# keyboard movement
ds.listen()

# p1:
ds.onkeypress(p1_up, "a")
ds.onkeypress(p1_down, "z")

# p2
ds.onkeypress(p2_up, "k")
ds.onkeypress(p2_down, "m")

############################################################################
# game
while 1:
    ds.update()

    # ball movement
    ppball.setx(ppball.xcor() + ppball.xaxis)
    ppball.sety(ppball.ycor() + ppball.yaxis)

    # setting boundaries
    # top
    if ppball.ycor() > 290:
        ppball.sety(290)
        ppball.yaxis *= -1

    # bottom
    if ppball.ycor() < -290:
        ppball.sety(-290)
        ppball.yaxis *= -1

    # left
    if ppball.xcor() > 390:
        ppball.goto(0,0)
        ppball.xaxis *= -1
        p1_score+=1
        sb.clear()
        sb.write("P1: {} P2:{}".format(p1_score, p2_score), align="center", font=("arial", 20, "bold"))

    # right
    if ppball.xcor() < -390:
        ppball.goto(0,0)
        ppball.xaxis *= -1
        p2_score += 1
        sb.clear()
        sb.write("P1: {} P2:{}".format(p1_score, p2_score), align="center", font=("arial", 20, "bold"))

    # dealing with collisions
    if (ppball.xcor()> 340 and ppball.xcor() < 350) and (ppball.ycor() < p1.ycor() + 50 and ppball.ycor() > p2.ycor() - 40):
        ppball.setx(340)
        ppball.xaxis *= -1

    if (ppball.xcor()< -340 and ppball.xcor() > -350) and (ppball.ycor() < p1.ycor() + 50 and ppball.ycor() > p1.ycor() - 40):
        ppball.setx(-340)
        ppball.xaxis *= -1


