# importing turtle 
import turtle
import random   


# creating turtle object
t = turtle.Turtle()
t.speed('fastest')
# changing the color
t.color("blue")

# drawing circle
t.penup()
t.goto(-350, 0)
t.pendown()
list_of_colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
i = 0
turtle.tracer(0)
while True:
    t.color(random.choice(list_of_colors))
    t.forward(1)
    t.circle(100)
    t.left(1)
    if i % 100 == 0:
        turtle.update()
    if i % 1000==0:
        t.forward(30)
    i += 1
    x = t.xcor()
    y = t.ycor()
    if x > 400 or x < -400 or y > 400 or y < -400:
        break
# displaying the window
turtle.done()