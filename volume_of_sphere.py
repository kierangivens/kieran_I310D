import math

value1 = 30
value2 = 40

def calculate_volume_of_sphere(radius):
    volume = (radius * math.pi) * 4/3

    print(f"Volume of sphere is {volume}")

calculate_volume_of_sphere(value1)