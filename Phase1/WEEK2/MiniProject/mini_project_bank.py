
# ============================
# AKIBA BANK ACCOUNT SYSTEM
# ============================

# Step 1: Initialize variables
balance = 1000
correct_pin = 1234
attempts = 0
transactions = 0
logged_in = False

# Step 2: PIN authentication
print("===== AKIBA BANK =====")

while attempts < 3:
    pin = input("Enter your PIN: ")

    # Validate that the PIN contains digits
    if not pin.isdigit():
        attempts += 1
        print("Invalid PIN. Enter numbers only.")

    elif int(pin) == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        logged_in = True
        break

    else:
        attempts += 1
        print("Incorrect PIN.")
        print(f"Attempts remaining: {3 - attempts}")

# Step 3: Lock the account after 3 incorrect attempts
if not logged_in:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

else:
    # Step 4: Display the menu repeatedly
    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        # Option 1: Check balance
        if choice == "1":
            print(f"Your current balance is: {balance} Birr")
            print(f"Transactions made: {transactions}")

        # Option 2: Deposit money
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    print("Invalid amount. Enter a positive amount.")

                else:
                    balance += amount
                    transactions += 1
                    print("Deposit successful!")
                    print(f"Your new balance is: {balance:g} Birr")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Option 3: Withdraw money
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount. Enter a positive amount.")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance -= amount
                    transactions += 1
                    print("Withdrawal successful!")
                    print(f"Your new balance is: {balance:g} Birr")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Option 4: Exit
        elif choice == "4":
            print(f"Transactions made: {transactions}")
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            break

        # Handle invalid menu options
        else:
            print("Invalid option.")
            print("Please choose a valid option.")
