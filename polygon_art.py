import turtle
import random

class polygon:
    def __init__():
        pass
    def draw_polygon(num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def drawing_polygon(numside_val1,numside_val2):
        for i in range(1,25):
            # draw a polygon at a random location, orientation, color, and border line thickness
            num_sides = random.randint(numside_val1, numside_val2) # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = polygon.get_new_color()
            border_size = random.randint(1, 10)
            polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

    def drawing_polygon2(numside_val1,numside_val2):
        for i in range(1,25):
            # draw a polygon at a random location, orientation, color, and border line thickness
            num_sides = random.randint(numside_val1, numside_val2) # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = polygon.get_new_color()
            border_size = random.randint(1, 10)
            polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

            # specify a reduction ratio to draw a smaller polygon inside the one above
            reduction_ratio = 0.618
            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            size *= reduction_ratio

            # draw the second polygon embedded inside the original 
            polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            size *= reduction_ratio

            polygon.draw_polygon(num_sides, size, orientation, location, color, border_size)

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
if choice == 1:
    polygon.drawing_polygon(3,3)

elif choice == 2:
    polygon.drawing_polygon(4,4)

elif choice == 3:
    polygon.drawing_polygon(5,5)

elif choice == 4:
    polygon.drawing_polygon(3,5)

elif choice == 5:
    polygon.drawing_polygon2(3,3)

elif choice == 6:
    polygon.drawing_polygon2(4,4)

elif choice == 7:
    polygon.drawing_polygon2(5,5)

elif choice == 8:
    polygon.drawing_polygon2(3,5)
elif choice == 9:
    polygon.drawing_polygon2(3,5)
    polygon.drawing_polygon(3,5)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
