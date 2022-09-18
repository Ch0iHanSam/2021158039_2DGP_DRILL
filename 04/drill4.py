import turtle

count = 4
count_2 = 2
count_3 = 2

while(count>0):
    turtle.forward(500)
    turtle.left(90)
    count-=1

while(count_2>0):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    count_2-=1

turtle.forward(100)

while(count_3>0):
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    count_3-=1

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.exitonclick()
