print("Currency Exchange Desk")
usd=int(input("Enter currecny in USD:"))
exchange_rate = 150
Exchange = usd*exchange_rate
print("==============================\nCURRENCY EXCHANGE\n==============================")
print(f" USD amount:{usd}\n Exchange Rate: 1 USD = 150 ETB \n ETB Amount:{Exchange} ETB")

# to allow the user to enter their own exchange rate 

NewExchange=int(input("Enter your new exchgange rate"))
Exchange=usd*NewExchange
print(f"Exchange Rate: 1 USD = {NewExchange} ETB \n ETB Amount:{Exchange} ETB")