# test1: Shopping items and subtotal

items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5},
    {"name": "Book", "price": 45, "quantity": 7}
]

def calculate_subtotal(items):
    total = 0

    for item in items:
       
        if item["price"] < 0 or item["quantity"] < 0:
            return "Price or quantity cannot be negative"
       
        total += item["price"] * item["quantity"]
    
    return total
# test 
subtotal = calculate_subtotal(items)
print("Subtotal", subtotal, "Birr")

#  Calculate the discount

def calculate_discount(subtotal):
    if subtotal < 0:
        return "Subtotal cannot be negative"

    if subtotal >= 3000:
        discount = subtotal * 0.10
    elif subtotal >= 1000:
        discount = subtotal * 0.05
    else:
        discount = 0

    return discount

# Tets2
print("Discount on 500 Birr:", calculate_discount(500))
print("Discount on 2000 Birr:", calculate_discount(2000))
print("Discount on 4000 Birr:", calculate_discount(4000))

# step: Calculate tax

def calculate_tax(amount, tax_rate):
    if amount < 0:
        return "Amount cannot be negative"

    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Tax rate must be between 0 and 100.")

    tax = amount * (tax_rate / 100)

    return tax


# Test 3
print("Tax on 1000 Birr at 15%:", calculate_tax(1000, 15))
print("Tax on 500 Birr at 10%:", calculate_tax(500, 10))

#  Generate the receipt

def generate_receipt(items, tax_rate):
    
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)

    final_amount = discounted_amount + tax

    receipt = {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }

    return receipt

# test 4
receipt = generate_receipt(items, 15)

print("Receipt dictionary:", receipt)