import math

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return abs(n1 * n2) // gcd(n1, n2)

def percentage(n1, n2):
    return (n1 / n2) * 100

def sine(angle):
    return math.sin(angle)

def cosine(angle):
    return math.cos(angle)

def tangent(angle):
    if math.cos(angle) == 0:
        return "Error: Tan undefined (cosine is 0)"
    return math.tan(angle)

while True:

    print("\nFollowing is the index:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Least Common Multiple (LCM)")
    print("7. Greatest Common Divisor (GCD)")
    print("8. Percentage")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("0. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 0:
        print("Exiting the calculator.")
        break

    if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

    if choice == 1:
        print(f"Result: {addition(n1, n2)}")
    elif choice == 2:
        print(f"Result: {subtraction(n1, n2)}")
    elif choice == 3:
        print(f"Result: {multiplication(n1, n2)}")
    elif choice == 4:
        print(f"Result: {division(n1, n2)}")
    elif choice == 5:
        print(f"Result: {modulus(n1, n2)}")
    elif choice == 6:
        print(f"Result: {lcm(n1, n2)}")
    elif choice == 7:
        print(f"Result: {gcd(n1, n2)}")
    elif choice == 8:
        print(f"Result: {percentage(n1, n2)}%")

        # Perform trigonometric operations (sin, cos, tan) - user input angle in degrees
    elif choice == 9:
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle_deg)
        print(f"sin({angle_deg}°) = {sine(angle_rad)}")
    elif choice == 10:
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle_deg)
        print(f"cos({angle_deg}°) = {cosine(angle_rad)}")
    elif choice == 11:
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle_deg)
        print(f"tan({angle_deg}°) = {tangent(angle_rad)}")

    else:
        print("Invalid choice, please try again.")
