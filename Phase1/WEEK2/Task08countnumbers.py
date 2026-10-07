number = int(input("Enter positive number:"))
evencount = 0
oddcount = 0
sum = 0
 
for i in range(1, number + 1):
     sum = sum + i
     if i % 2 == 0:
      evencount = evencount + 1
     else:
      oddcount = oddcount + 1

print(f"Sum of the numbers: {sum}")
print(f"Number of even numbers: {evencount}")
print(f"Number of odd numbers: {oddcount}")
