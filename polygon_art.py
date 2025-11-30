import turtle
import random

class Polygon: 
    def __init__(self,range1,range2):
        self.num_sides = random.randint(range1, range2) # triangle, square, or pentagon
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

class Drawing_polygon(Polygon):

    def __init__(self,range1,range2):
        super().__init__(range1,range2)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def reposition(self):
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
    def main_drawing(self):
        self.draw_polygon()
        self.reposition
    def sub_drawing(self):
        self.draw_polygon()
        self.reposition()
        self.size *= self.reduction_ratio
        self.draw_polygon()
        self.reposition()
        self.size *= self.reduction_ratio
        self.draw_polygon()
        self.reposition()

choice = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
if choice == '1':
    for i in range(25):
        p = Drawing_polygon(3,3)
        p.main_drawing()
    turtle.done()
elif choice == '2':
    for i in range(25):
        p = Drawing_polygon(4,4)
        p.main_drawing()
    turtle.done()
elif choice == '3':
    for i in range(25):
        p = Drawing_polygon(5,5)
        p.main_drawing()
    turtle.done()
elif choice == '4':
    for i in range(25):
        p = Drawing_polygon(3,5)
        p.main_drawing()
    turtle.done()
elif choice == '5':
    for i in range(25):
        p = Drawing_polygon(3,3)
        p.sub_drawing()
    turtle.done()
elif choice == '6':
    for i in range(25):
        p = Drawing_polygon(4,4)
        p.sub_drawing()
    turtle.done()
elif choice == '7':
    for i in range(25):
        p = Drawing_polygon(5,5)
        p.sub_drawing()
    turtle.done()
elif choice == '8':
    for i in range(25):
        p = Drawing_polygon(3,5)
        p.sub_drawing()
    turtle.done()
elif choice == '9':
    for i in range(15):
        p = Drawing_polygon(3,5)
        p.sub_drawing()

    for i in range(15):
        p = Drawing_polygon(3,5)
        p.main_drawing()
    turtle.done()  

