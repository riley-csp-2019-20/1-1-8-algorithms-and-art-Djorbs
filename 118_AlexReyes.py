import turtle as trtl 
t = trtl.Turtle()
turtles = []
turt_shapes = ["turtle", "turtle", "turtle", "turtle", "turtle", "turtle"] 
angle = 30
#Makes the lines
for boop in turt_shapes:
    t = trtl.Turtle(shape=boop)
    turtles.append(t)
    t.speed(180)
    t.setheading(angle)
    t.pensize(8)
    t.forward(150)
    angle += 60
#Readys turtles to make the angles
for t in turtles:
    t.penup()
    t.right(180)
    t.forward(70)
    t.right(180)
#Draws the angles
for a in turtles:
    a.pendown()
    a.right(45)
    a.forward(70)
    a.right(180)
    a.forward(70)
    a.left(270)
    a.forward(70)
    a.left(180)
for b in turtles:
    b.forward(70)
    b.right(45)
    b.forward(80)


    





wn = trtl.Screen()
wn.mainloop()