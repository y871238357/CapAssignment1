from turtle import *


def draw_spiderMan():
    speed(13)  # Painting speed control
    bgcolor("Dark blue")
    pensize(9)
    penup()
    goto(0, 50)
    pendown()
    circle(-140)
    penup()
    goto(10, 60)
    pendown()
    circle(-120)
    penup()
    goto(20, 70)
    pendown()
    fillcolor("#3366cc")
    begin_fill()
    circle(-100)
    end_fill()
    
 
print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for my art creation: ")
    try:
        a = eval(a)

        if a == 1:
            draw_spiderMan()
        else:
            print("Please input the value 1")
    except:
        print("Please input the value 1")


