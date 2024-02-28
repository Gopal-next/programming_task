''' Write a Python function calculate_area that takes two parameters: length and width. It 
should calculate and return the area of a rectangle. However, add a condition: if the length
is equal to the width, return "This is a square!" instead of the area. Then, write a program to
input values for length and width from the user and call the calculate_area function to
display either the area or the message. '''

def calculate_area(length, breadth):
    if length == breadth:
        return "This is a square!"
    else:
        return length * breadth

length = int(input("Enter the length of a rectangle : "))
breadth = int(input("Enter the breadth of rectangle : "))

area = calculate_area(length, breadth)
print(area)