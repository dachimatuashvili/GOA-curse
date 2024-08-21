from turtle import *


#we want to paint a house

#step 1: draw a square
speed(3)
width(5)
color("purple")
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")

begin_fill()

right(150)
forward(200)
left(120)
forward(200)

end_fill()

#drawing the windows
penup()
goto(40, 150)
pendown()
color("blue")
begin_fill()
right(150)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(150, 150)
pendown()
forward(10)
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(20)
end_fill()
exitonclick()