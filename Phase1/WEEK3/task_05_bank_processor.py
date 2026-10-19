
amount = 1000

# Store successful transactions
transactions = []

# Daily withdrawal limit
daily_withdrawal_limit = 3000
total_withdrawn_today = 0


def deposit_money(amount, money):
   
    if money <= 0:
        return "Enter positive values"
    else:
        balance = amount + money
    return balance

deposit = 300
result = deposit_money(amount, deposit)

if isinstance(result, (int, float)):
    amount = result
    print("Your deposited money is", amount)

    # Record the successful deposit
    record = {
        "type": "deposit",
        "amount": deposit,
        "balance_after": amount
    }
    transactions.append(record)
else:
    print(result)


def withdraw_money(amount, money):
    if money <= 0:
        return "Enter a positive number"
    elif money > amount:
        return "INSUFFICIENT Amount"
    else:
        balance = amount - money
    return balance

withdrawal = 300
result = withdraw_money(amount, withdrawal)

if isinstance(result, (int, float)):
    amount = result
    print("Your balance after withdrawal is", amount)

    # Record the successful withdrawal
    record = {
        "type": "withdrawal",
        "amount": withdrawal,
        "balance_after": amount
    }
    transactions.append(record)
else:
    print(result)

# print(withdraw_money(amount, -200))
# print(withdraw_money(amount, 20))

def check_balance(balance):
    return balance

print("Current balance:", check_balance(amount))


# Record a successful transaction
def record_transaction(transaction_type, money, balance):

    transaction = {
        "type": transaction_type,
        "amount": money,
        "balance_after": balance
    }

    transactions.append(transaction)

    return transaction


# Generate transaction summary
def generate_summary():

    total_deposited = 0
    total_withdrawn = 0

    for transaction in transactions:

        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]

        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n----- TRANSACTION SUMMARY -----")
    print("Total deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Final balance:", check_balance(amount))

    print("\nTransaction History:")

    for transaction in transactions:
        print(transaction)


# Main banking program
while True:

    print("\n----- BANK MENU -----")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        money = float(input("Enter deposit amount: "))

        result = deposit_money(amount, money)

        if isinstance(result, (int, float)):
            amount = result
            record_transaction("deposit", money, amount)
            print("Deposit successful!")
            print("Current balance:", amount)
        else:
            print(result)

    elif choice == "2":

        money = float(input("Enter withdrawal amount: "))

        if money <= 0:
            print("Enter a positive number")

        elif money > amount:
            print("INSUFFICIENT Amount")

        elif money > daily_withdrawal_limit - total_withdrawn_today:
            print("Daily withdrawal limit exceeded")

        else:
            result = withdraw_money(amount, money)

            if isinstance(result, (int, float)):
                amount = result
                total_withdrawn_today += money
                record_transaction("withdrawal", money, amount)
                print("Withdrawal successful!")
                print("Current balance:", amount)
                print("Remaining daily withdrawal allowance:",
                      daily_withdrawal_limit - total_withdrawn_today)
            else:
                print(result)

    elif choice == "3":

        print("Current balance:", check_balance(amount))

    elif choice == "4":

        generate_summary()

    elif choice == "5":

        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")
