"Williams_Timothy_TPW_1.7.3"
##9.9.2026 -- practice for user input and calculation, Exercise name: Area of a Room
##Solved in 8 lines using a function and calling for variables that were set to floating point values
width = 0.
length = 0.
def room_area(width, length):
    width = input("What is the width of the room in meters?: ", )
    length = input("What is the length of the room in meters?: ", )
    area = float(width)*float(length)
    print("The area of your room is equal to: ", area, "sq. meters")
    return
room_area(width, length)