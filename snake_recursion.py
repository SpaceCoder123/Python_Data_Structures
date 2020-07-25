import turtle
myTurtle=turtle.Turtle()
my_winddow=turtle.Screen()
def draw_spiral(my_turtle,line_length):
    if line_length>0:
        myTurtle.forward(line_length)
        myTurtle.right(90)
        draw_spiral(myTurtle,line_length-5)


print(draw_spiral(myTurtle,100))

my_winddow.exitonclick()