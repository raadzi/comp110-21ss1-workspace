from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
#makes leo
leo.forward(50)
leo.left(30)
leo.right(40)
#leo is moving
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1
#leo does this movement 4 times
leo.penup()
leo.goto(45, 60)
leo.pendown()
#leo goes to this point without drawing on the paper
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
#the last one sets both the pen and fill color
leo.speed(50)
#leo is a runner hes a track star
leo.hideturtle()
#leo goes into hiding
done()