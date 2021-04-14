import turtle


def triangle(t, n, length1, length2, turn):
    ''' 
    This is mainly
    for drawing
    t = turtle
    n = number of triangle
    length1 = length of the leg
    length2 = length of the base
    turn = angle when turning (degrees)
    '''
    for i in range(n):
        sky.fd(length1)
        sky.lt(turn)
        sky.fd(length2)
        sky.lt(turn)
        sky.fd(length1)
        sky.lt(180)


def pie(t, n, length1, length2):
    ''' 
    All the calculations
    are calculated here.
    Note (We're using an icosceles triangle)
    t = turtle
    n = number of triangle
    length1 = length of the leg
    length2 = length of the base 
    '''
    angle = 360 / n  # finding the top angle of the triangle
    degree = (180 - angle) / 2  # finding the bottom angle of the traingle
    turn = 180 - degree  # how much the turtle should turn
    triangle(t, n, length1, length2, turn)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


sky = turtle.Turtle()

move(sky, -200)
pie(sky, 5, 60, 70)

move(sky, 150)
pie(sky, 6, 60, 60)

move(sky, 150)
pie(sky, 7, 60, 52)

sky.hideturtle()
turtle.mainloop()