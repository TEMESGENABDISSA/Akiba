total = 0
EvenCount = 0
OddCount = 0
numbers = []

for i in range(10):
    number = int(input("Insert a number:"))
    numbers.append(number)

    total = total + number

    if number % 2 == 0:
        EvenCount += 1
    else:
        OddCount += 1

average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print(f"This is the sum: {total}")
print(f"This is the average: {average}")
print(f"Even numbers: {EvenCount}")
print(f"Odd numbers: {OddCount}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")