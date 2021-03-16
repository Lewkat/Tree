import turtle
from pymunk.vec2d import Vec2d

Minimum_branch_length = 5


window = turtle.Screen()
t1 = turtle.Turtle()
t1.pensize(3)
t1.setheading(90)
t1.color("red")
t2 = turtle.Turtle()
t2.pensize(3)
t2.setheading(90)
t2.color("blue")
window.bgcolor("black")
Stamps = 0

def fractal(t, z, branch_length, shorten_by, angle):
    p1 = t1.pos()
    p2 = t2.pos()
    global Stamps
    if branch_length > Minimum_branch_length:

        t.forward(branch_length)
        z.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        z.right(angle)
        fractal(t, z, new_length, shorten_by, angle)

        t.right(angle * 2)
        z.left(angle * 2)
        fractal(t, z, new_length, shorten_by, angle)

        t.left(angle)
        z.right(angle)
        t.backward(branch_length)
        z.backward(branch_length)
        p1 = t1.pos()
        p2 = t2.pos()

    elif branch_length == 5:

            t1.stamp()
            t2.stamp()
            Stamps = Stamps + 1
            print(Stamps)
            if Stamps == 256:
                raise SystemExit
            #print(p1)
            #print(p2)
            #if p1 == Vec2d(70.80,141.29) and p2 == Vec2d(-70.80,141.29):
            #    raise SystemExit




fractal(t1, t2, 50, 5, 30)
turtle.mainloop()
window.exitonclick()
