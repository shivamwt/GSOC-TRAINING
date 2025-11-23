# Day 3 — Calculator with negative & decimal number support

a = input("Enter first number: ")
b = input("Enter second number: ")

# Smarter input validation using try-except
try:
    a = float(a)
    b = float(b)
except ValueError:
    print("Invalid input! Please enter a valid number (positive, negative, or decimal).")
    exit()

print("\nResults:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Safe division
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible (b is zero)")
