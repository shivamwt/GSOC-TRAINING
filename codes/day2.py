# Day 2 — Operators & Input Validation

# Take 2 numbers from user
a = input("Enter first number: ")
b = input("Enter second number: ")

# Input validation
if not a.isdigit() or not b.isdigit():
    print("Invalid input! Please enter numbers only.")
    exit()

a = int(a)
b = int(b)

print("\nResults:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Prevent division by zero
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible (b is zero)")
