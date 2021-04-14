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
def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

# draw polypies with various number of sides
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
sky = turtle.Turtle()

move(sky, -200)
pie(sky, 5, 60, 70)

move(sky, 150)
pie(sky, 6, 60, 60)

move(sky, 150)
pie(sky, 7, 60, 52)

sky.hideturtle()
turtle.mainloop()