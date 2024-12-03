def areaOfCircle(radius):       # Function for area calculation
    area = 3.14 * radius * radius
    return area
rad = int(input("ENTER RADIUS : "))
area = areaOfCircle(rad)   # Function Calling
print("Area ->" , area )