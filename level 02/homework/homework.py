import turtle

screen = turtle.Screen()
screen.bgcolor("black")


def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
draw_rectangle("lightgray", -150, -100, 300, 200)


turtle.penup()
turtle.goto(-160, 100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.goto(0, 200)
turtle.goto(160, 100)
turtle.goto(-160, 100)
turtle.end_fill()

draw_rectangle("white", -30, -100, 60, 100)

draw_rectangle("blue", -100, 0, 50, 50)
draw_rectangle("blue", 50, 0, 50, 50)

turtle.penup()
turtle.goto(0, 200)
turtle.color("gold")
turtle.pendown()
turtle.dot(20)

# დასრულება
turtle.hideturtle()
screen.mainloop()
