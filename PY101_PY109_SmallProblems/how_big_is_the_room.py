
length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

def area(length, width):
    area_meter = length * width
    area_feet = area_meter * 10.7639
    return area_meter, area_feet

area_meter, area_feet = area(length, width)

print(f"The area of the room is {area_meter} square meters ({area_feet} square feet).")