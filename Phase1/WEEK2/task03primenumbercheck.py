# numbers={0,1,3,4,5,7,10}

# for number in numbers:
#     if number==0 or number==1:
#         print(f"{number} is not prime")
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(f"{number} is not prime")
#                 break
#         else:
#             print(f"{number} is prime")

            # Or, if we want the number to be entered by the user.
number = int(input("Enter the number: "))

if number == 0 or number == 1:
    print(f"{number} is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
