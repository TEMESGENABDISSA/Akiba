
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b == c:
    print("All numbers are equal.")
elif a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")