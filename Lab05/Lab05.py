# lab05vst.py
# Student version of the Lab05 assignment.
import turtle
WIDTH = 980
HEIGHT = 630

def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def main():
    screen = turtle.Screen()
    screen.setup(1000, 660)
    screen.setworldcoordinates(0, 660, 1000, 0)
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    # Draw the rectangle
    draw_line(t, 10, 10, 10 + WIDTH, 10)
    draw_line(t, 10 + WIDTH, 10, 10 + WIDTH, 10 + HEIGHT)
    draw_line(t, 10 + WIDTH, 10 + HEIGHT, 10, 10 + HEIGHT)
    draw_line(t, 10, 10 + HEIGHT, 10, 10)


    # Draw bottom-left corner
    x1 = 990
    y1 = 640
    x2 = 10
    y2 = 640
    for i in range(50):
        draw_line(t, x1, y1, x2, y2)
        x1 -= 19
        y2 -= 12

    # bottom right
    x1 = 10
    y1 = 10
    x2 = 990
    y2 = 10
    for i in range(50):
        draw_line(t, x1, y1, x2, y2)
        x1 -= 19
        y2 -= 12


    # Draw top-right corner
    # Draw top-left corner
    screen.update()
    screen.mainloop()

main()