import turtle

turtle.setup(800,400)
turtle.speed(10)
turtle.penup()
turtle.goto(-300,0)
turtle.down()
turtle.seth(-40)
turtle.pensize(20)
turtle.pencolor('green')


for i in range(1,4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,45)
turtle.seth(0)
turtle.fd(40)
turtle.circle(20,190)






turtle.done()