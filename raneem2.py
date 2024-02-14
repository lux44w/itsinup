import math

def calculate_area(shape):
    if shape == "square":
        side_length = float(input("Enter the side length of the square: "))
        area = side_length ** 2
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
    elif shape == "triangle":
        base = float(input("Enter the length of the triangle base: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
    else:
        print("Unsupported geometric shape")
        return None

    return area

def main():
    shape = input("Enter the name of the geometric shape (square, circle, rectangle, triangle): ")
    area = calculate_area(shape)

    if area is not None:
        print(f"The area is: {area}")

if __name__ == "__main__":
    main()
