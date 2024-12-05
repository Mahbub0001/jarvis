import turtle
import time

# Create screen and set properties
screen = turtle.Screen()
screen.title("Bangladesh Flag Animation")
screen.bgcolor("white")
screen.setup(width=800, height=500)

# Create the turtle object for drawing
flag = turtle.Turtle()
flag.speed(3)  # Adjust the speed for animation

def draw_rectangle():
    """Draw the green rectangle for the flag background."""
    flag.penup()
    flag.goto(-200, 100)  # Top-left corner of the rectangle
    flag.pendown()
    flag.color("green")
    flag.begin_fill()
    for _ in range(2):
        flag.forward(400)  # Rectangle width
        flag.right(90)
        flag.forward(200)  # Rectangle height
        flag.right(90)
    flag.end_fill()

def draw_circle():
    """Draw the red circle in the center of the flag."""
    flag.penup()
    flag.goto(0,-100 )  # Center of the rectangle
    flag.setheading(90)  # Point turtle upwards
    flag.forward(50)  # Move turtle to top of the circle
    flag.setheading(0)  # Reset heading to default
    flag.pendown()
    flag.color("red")
    flag.begin_fill()
    flag.circle(60)  # Circle radius
    flag.end_fill()

# Animation sequence
def animate_flag():
    """Create an animation effect for the flag drawing."""
    draw_rectangle()
    time.sleep(1)  # Pause to display the rectangle
    draw_circle()

# Run the animation
animate_flag()

# Finish the drawing
flag.hideturtle()
screen.mainloop()
