# Area Calculator
# Put Your Name Here
# Put the Date Here

choice=input("What do you want to find the area of? Choose 1 for rectangle, 2 for circle, or 3 for triangle.")
if choice=='1':
    rectangle_width=float(input("What is the width of your rectangle?"))
    rectangle_height=float(input("What is the length of your rectangle?"))
    print("The area of your rectangle is", rectangle_width*rectangle_height)
elif choice=='2':
    circle_radius=float(input("What is the radius of your circle?"))
    print("The area of your circle is", circle_radius*3.14**2)
else:
    triangle_base=float(input("What is the base of your triangle?"))
    triangle_height=float(input("What is the height of your triangle?"))
    print("The area of your triangle is", 0.5*triangle_base*triangle_height)
   
