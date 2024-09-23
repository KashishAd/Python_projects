#Name: Kashish Adlakha
#UID: U31221034
#Description: the program asks the user for an input for number and length of each side of the polygon and creates a polygon based on the given input. 

import turtle

tk = turtle.Turtle()
  
n = int(turtle.numinput("No. of sides",prompt="Enter number of sides of polygon",default=3,minval=3,maxval=12)) 
l = int(turtle.numinput("Length of sides",prompt="Enter length of sides of the polygon",default=50,minval=50,maxval=250)) 
a = (180*(num-2))/num

for _ in range(n):
    
    turtle.forward(l)
    
    turtle.right(180 - a)

if n==3:
    polygon="triangle"
    
elif n==4:
    polygon="quadrilateral"
    
elif n==5:
    polygon="pentagon"
    
elif n==6:
    polygon="hexagon"
    
elif n ==7:
    polygon="heptagon"
    
elif n ==8:
    polygon="octagon"
    
elif n ==9:
    polygon="nonagon"
    
elif n ==10:
    polygon="decagon"
    
elif n ==11:
    polygon="hendecagon"
    
elif n ==12:
    polygon="dodecagon"

turtle.write(polygon, font=("Verdana",15, "normal"))

turtle.Screen().exitonclick()