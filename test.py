import turtle

sc=turtle.Screen()
sc.title("Spongebob")
sc.setup(1500,700)
sc.bgcolor("#FFFFFF")


spongebobcharacter=turtle.Turtle()
spongebobcharacter.pu()
spongebobcharacter.color("black")
spongebobcharacter.fillcolor("yellow")
spongebobcharacter.begin_fill()
spongebobcharacter.goto(-250,175)
spongebobcharacter.pd()

#################
#face
x=-200
for i in range(5):
    spongebobcharacter.goto(x,165)
    x+=50
    spongebobcharacter.goto(x,175)
    x+=50
#print(spongebobcharacter.position())
spongebobcharacter.rt(90)
y=125
for i in range(5):
    spongebobcharacter.goto(240,y)
    y-=50
    spongebobcharacter.goto(250,y)
    y-=50
#print(spongebobcharacter.position())
spongebobcharacter.rt(90)
x=200
for i in range(5):
    spongebobcharacter.goto(x,-315)
    x-=50
    spongebobcharacter.goto(x,-325)
    x-=50
#print(spongebobcharacter.position())
spongebobcharacter.rt(90)
y=-275
for i in range(5):
    spongebobcharacter.goto(-240,y)
    y+=50
    spongebobcharacter.goto(-250,y)
    y+=50
spongebobcharacter.end_fill()

#################
#eye
#right eye

spongebobcharacter.up()
spongebobcharacter.setheading(0)
spongebobcharacter.goto(100,-30)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("white")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(70)
spongebobcharacter.end_fill()

spongebobcharacter.up()
spongebobcharacter.goto(100,-5)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("blue")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(40)
spongebobcharacter.end_fill()

spongebobcharacter.up()
spongebobcharacter.goto(100,15)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("black")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(20)
spongebobcharacter.end_fill()


#left eye
spongebobcharacter.up()
spongebobcharacter.goto(-100,-30)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("white")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(70)
spongebobcharacter.end_fill()

spongebobcharacter.up()
spongebobcharacter.goto(-100,-5)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("blue")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(40)
spongebobcharacter.end_fill()

spongebobcharacter.up()
spongebobcharacter.goto(-100,15)
spongebobcharacter.pd()
spongebobcharacter.fillcolor("black")
spongebobcharacter.begin_fill()
spongebobcharacter.circle(20)
spongebobcharacter.end_fill()


#mouse
spongebobcharacter.up()
spongebobcharacter.goto(-125,-100)
spongebobcharacter.setheading(-60)
spongebobcharacter.pd()
spongebobcharacter.circle(150,120)

turtle.done()