
store = []

def new_product(name, price, quantity):
    if name == "":
        return 'name cannot be empty'
    elif price < 0:
        return 'price cannot be negative'
    elif quantity < 0:
        return 'quantity cannot be negative'

    for product in store:
        if name == product[0]:
            return 'product name cannot be duplicated'

    store.append([name, price, quantity])
    return store


def search_product(name):
    for product in store:
        if name == product[0]:
            return product

    return 'product not found'


def update_product_price(name, newprice):
    if newprice < 0:
        return 'price cannot be negative'

    for product in store:
        if name == product[0]:
            product[1] = newprice
            return product

    return 'product not found'


def increase_stock(name, quantity):
    if quantity < 0:
        return 'quantity cannot be negative'

    for product in store:
        if name == product[0]:
            product[2] = product[2] + quantity
            return product

    return 'product not found'


def sell_products(name, quantity):
    for product in store:
        if name == product[0]:
            if quantity < 0:
                return 'quantity cannot be negative'
            elif quantity > product[2]:
                return 'not enough stock available'
            else:
                product[2] = product[2] - quantity
                return product

    return 'product not found'


def calculate_inventory(name):
    for product in store:
        if name == product[0]:
            return product[1] * product[2]

    return 'product not found'


def calculate_total_inventory_value():
    total = 0

    for product in store:
        total = total + product[1] * product[2]

    return total


def low_stock_report(threshold=5):
    report = []

    for product in store:
        if product[2] < threshold:
            report.append(product)

    return report


print(new_product('temesgen', 300, 3))
print(new_product('chekole', 200, 2))
print(new_product('abebe', 100, 8))

print('Search:', search_product('temesgen'))
print('Update price:', update_product_price('chekole', 400))
print('Increase stock:', increase_stock('temesgen', 4))
print('Sell product:', sell_products('temesgen', 2))

print('One product value:', calculate_inventory('temesgen'))
print('Total inventory value:', calculate_total_inventory_value())
print('Low-stock report:', low_stock_report())
print('Low-stock report with threshold 3:', low_stock_report(3))

print('Final store:', store)
