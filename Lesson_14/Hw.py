import turtle
screen = turtle.Screen()
screen.bgcolor("blue")
screen.setup(300, 400)
polygon = turtle.Turtle()

ns = 4
side_length = 100
angle = (400-40) / ns

for i in range (ns):
    polygon.forward(side_length)
    polygon. right(angle)
turtle.done()