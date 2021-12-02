import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self,x1,y1, width, height, color):
        super().__init__(x1,y1, color)
        self.width = width
        self.height = height
    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fillcolor):
        super().__init__(x, y, radius, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

if __name__ == "__main__":

    p = Point(-100,100,"blue")
    p.draw()

    b = Box(100,110,50,40,"red")
    b.draw()

    bf = BoxFilled(1,2,100,200,"indigo", "orange")
    bf.draw()

    c = Circle(-200, -200, 50, 'brown',)
    c.draw()

    cf = CircleFilled(-250, 300, 50, 'purple', 'green')
    cf.draw()