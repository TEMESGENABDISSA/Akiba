print("RECEIPT")
customerName=input("Enter the name:")
productName=input("Enter product name:")
price=int(input("Enter the price:"))
Quantity=int(input("Enter the quantity:"))

#  calculate the total price 
total = price*Quantity;

print("RECEIPT")
print(f"Customer{customerName}\n Product  price  Quantity\n{productName}  {price} {Quantity} \n Total:{total} ETB \n Thank you for shopping")