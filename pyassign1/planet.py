import math
import turtle       
wn = turtle.Screen() 
sun = turtle.Turtle()
sun.shape("circle")
sun.shapesize(5)
sun.color("orange")
merc = turtle.Turtle()
venu = turtle.Turtle()
eart = turtle.Turtle()
mars = turtle.Turtle()
satu = turtle.Turtle()
jupi = turtle.Turtle()
merc.shape("circle")
venu.shape("circle")
eart.shape("circle")
mars.shape("circle")
satu.shape("circle")
jupi.shape("circle")
merc.penup()
venu.penup()
eart.penup()
mars.penup()
satu.penup()
jupi.penup()
merc.setpos(100,0)
venu.setpos(150,0)
eart.setpos(200,0)
mars.setpos(250,0)
satu.setpos(340,0)
jupi.setpos(450,0)
merc.pendown()
venu.pendown()
eart.pendown()
mars.pendown()
satu.pendown()
jupi.pendown()
def draw(name, a, e, i,color,size):
    name.color(color)
    name.shapesize(size)
    b = a * ( 1 - e ** 2 ) ** 0.5
    name.setx((a * math.cos(i / 100)))
    name.sety((b * math.sin(i / 100)))
for i in range(0,628):
    draw(merc, 100, 0.5, 6*i ,"silver",0.5)
    draw(venu, 150, 0.7, 5*i ,"yellow",1)
    draw(eart, 200, 0.8, 4*i ,"blue",1.5)
    draw(mars, 250, 0.3, 3*i ,"red",1.2)
    draw(satu, 340, 0.8, 2*i ,"black",2.7)
    draw(jupi, 450, 0.6, i ,"grey",3)