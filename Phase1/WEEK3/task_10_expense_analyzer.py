
# SECTION 1: STORE AND ADD EXPENSES

Expenses = []

def add_expenses(description, catagory, amount):
    if amount < 0:
        return 'amount cannot be negative'
    else:
        expense = {
            "description": description,
            "category": catagory,
            "Amount": amount,
        }

        Expenses.append(expense)
        return expense

print(add_expenses('lunch', 'food', 230))
print(add_expenses('dinner', 'tea', 300))
print(add_expenses('lunch', "food", 400))
print(Expenses)



# SECTION 2: CALCULATE TOTAL EXPENSES


def calculate_total_expenses():
    total = 0

    for i in Expenses:
        total = total + i["Amount"]

    return total

print("totalexpenses:", calculate_total_expenses())



# SECTION 3: CALCULATE SPENDING BY CATEGORY


def calculate_spending_by_category():
    category_totals = {}

    for i in Expenses:
        category = i["category"]
        amount = i["Amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals

print("Spending by category:", calculate_spending_by_category())



# SECTION 4: FIND THE LARGEST EXPENSE


def largest_expense():
    if len(Expenses) == 0:
        return None

    largest = Expenses[0]['Amount']

    for i in Expenses:
        if i["Amount"] > largest:
            largest = i["Amount"]

    return largest

print(largest_expense())



# SECTION 5: FIND EXPENSES ABOVE A THRESHOLD


def expenses_above_threshold(threshold):
    store_matching = []

    for i in Expenses:
        if i['Amount'] > threshold:
            store_matching.append(i['Amount'])

    return store_matching

print(expenses_above_threshold(200))



# SECTION 6: CALCULATE CATEGORY PERCENTAGES


def calculate_categories_percentage():
    calculated_categories = calculate_spending_by_category()
    total_expense = calculate_total_expenses()
    percentages = {}

    if total_expense == 0:
        return percentages

    for category in calculated_categories:
        percentage = (
            calculated_categories[category] / total_expense
        ) * 100

        percentages[category] = round(percentage, 2)

    return percentages

print(calculate_categories_percentage())



# SECTION 7: FIND THE HIGHEST-SPENDING CATEGORY


def highest_spending_category():
    category = calculate_spending_by_category()

    if len(category) == 0:
        return None

    highest_category = None
    highest_amount = 0

    for i in category:
        if category[i] > highest_amount:
            highest_amount = category[i]
            highest_category = i

    return highest_category, highest_amount

print("The highest category is:", highest_spending_category())



# SECTION 8: GENERATE THE EXPENSE REPORT


def Expense_Report():
    total = calculate_total_expenses()
    Number_Expenses = len(Expenses)
    largest = largest_expense()
    spending = calculate_spending_by_category()
    percentage = calculate_categories_percentage()
    highest = highest_spending_category()

    report = {
        "Total Expenses": total,
        "Number of Expenses": Number_Expenses,
        "Largest Expense": largest,
        "Spending by category": spending,
        "Category Percentages": percentage,
        "Highest Spending Category": highest
    }

    #  report 
 
    print("          EXPENSE REPORT")
    
    print(f"Total Expenses: {total} Birr")
    print(f"Number of Expenses: {Number_Expenses}")

    if largest is not None:
        print(f"Largest Expense: {largest} Birr")
    else:
        print("Largest Expense: No expenses recorded")

    print("\n--- Spending by Category ---")

    for category, amount in spending.items():
        print(f"{category.title()}: {amount} Birr")

    print("\n Category Percentages")

    for category, percent in percentage.items():
        print(f"{category.title()}: {percent}%")

    print("\n Highest Spending Category ")

    if highest is not None:
        print(f"Category: {highest[0].title()}")
        print(f"Total: {highest[1]} Birr")
    else:
        print("No categories available")

    return report

print(Expense_Report())


     