# Day 4 — Loops (for + while)

# 1) Print numbers 1 to 10 using for loop
print("\nNumbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")

# 2) Print multiplication table using for loop
num = int(input("\n\nEnter a number for multiplication table: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3) Sum of numbers until user enters 0 using while loop
print("\nEnter numbers to add (enter 0 to stop):")
total = 0
while True:
    x = float(input("Enter number: "))
    if x == 0:
        break
    total += x

print("\nTotal Sum =", total)
