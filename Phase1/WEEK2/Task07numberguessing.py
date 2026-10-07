secretnumber = 17
count = 0

while count < 5:
    number = int(input("Enter a number: "))

    if number == secretnumber:
        print("You won the game")
        break

    elif count == 4:
        print("You failed")
        break

    else:
        count = count + 1
        print("Try again")