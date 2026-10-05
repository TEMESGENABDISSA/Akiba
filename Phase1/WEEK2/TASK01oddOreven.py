numbers=int(input("Enter number:"))
if numbers == 0:
    print("The number is zero, and even")
elif numbers % 2 == 0:
    print(f"{numbers} is an even number")
else:
    print(f"{numbers} is an odd number.")