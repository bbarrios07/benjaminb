import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Geometric Cat")

# Create and configure the turtle
cat = turtle.Turtle()
cat.speed(2)
cat.color("orange")
cat.fillcolor("orange")

# Draw the cat's head
cat.penup()
cat.goto(-20, 0)  # Moved head closer to body
cat.pendown()
cat.begin_fill()
cat.circle(30)  # Head
cat.end_fill()

# Draw the ears
cat.penup()
cat.goto(-20, 50)  # Left ear
cat.pendown()
cat.begin_fill()
cat.setheading(115)
for _ in range(3):
    cat.forward(25)
    cat.left(120)
cat.end_fill()

cat.penup()
cat.goto(10, 50)  # Right ear
cat.pendown()
cat.begin_fill()
cat.setheading(115)
for _ in range(3):
    cat.forward(25)
    cat.left(120)
cat.end_fill()

# Draw eyes
cat.penup()
cat.goto(-35, 25)  # Left eye
cat.pendown()
cat.color("black")
cat.begin_fill()
cat.circle(3)
cat.end_fill()

cat.penup()
cat.goto(-15, 25)  # Right eye
cat.pendown()
cat.begin_fill()
cat.circle(3)
cat.end_fill()

# Draw nose
cat.penup()
cat.goto(-25, 20)
cat.pendown()
cat.color("pink")
cat.begin_fill()
cat.circle(2)
cat.end_fill()

# Draw whiskers
cat.color("black")
# Left whiskers
cat.penup()
cat.goto(-35, 20)
cat.setheading(180)
cat.pendown()
cat.forward(15)  # Left whisker 1

cat.penup()
cat.goto(-35, 18)
cat.pendown()
cat.forward(15)  # Left whisker 2

# Right whiskers
cat.penup()
cat.goto(-15, 20)
cat.setheading(0)
cat.pendown()
cat.forward(15)  # Right whisker 1

cat.penup()
cat.goto(-15, 18)
cat.pendown()
cat.forward(15)  # Right whisker 2

cat.color("orange")  # Return to orange color for body
# Draw the body
cat.penup()
cat.goto(-20, 0)  # Connect to head
cat.pendown()
cat.begin_fill()
cat.setheading(0)
cat.forward(80)  # Body length
cat.right(90)
cat.forward(40)  # Body height
cat.right(90)
cat.forward(80)
cat.right(90)
cat.forward(40)
cat.end_fill()

# Draw the tail
cat.penup()
cat.goto(60, 0)
cat.pendown()
cat.begin_fill()
cat.setheading(45)
cat.circle(30, 90)
cat.end_fill()

# Draw front paws
# Front paw
cat.penup()
cat.goto(-10, -40)
cat.setheading(270)
cat.pendown()
cat.begin_fill()
cat.forward(20)
cat.circle(5, 180)
cat.forward(20)
cat.end_fill()

# Back paw
cat.penup()
cat.goto(50, -40)
cat.setheading(270)
cat.pendown()
cat.begin_fill()
cat.forward(20)
cat.circle(5, 180)
cat.forward(20)
cat.end_fill()

# Hide the turtle and keep the window open
cat.hideturtle()
turtle.done()