number = input("Enter a number: ")

sum = 0
i = 0

while i < len(number):
    sum = sum + int(number[i])
    i = i + 1

print(sum)