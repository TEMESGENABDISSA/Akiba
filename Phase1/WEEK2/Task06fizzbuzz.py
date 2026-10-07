start = int(input("Enter starting number"))
End = int(input("Enter ending number "))

for i in range(start, End + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FizzBuzz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
    else:
        print(i)