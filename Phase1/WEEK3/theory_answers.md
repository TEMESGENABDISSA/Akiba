# Theory Answers

## Question 1: Function Design

If one function has 100 lines and does everything (managing products, processing sales and making reports), it gets hard to maintain. Everything is mixed together, so to understand one part you have to read all of it. If I change something in the sales part, I might break the report part without noticing.

Here is an example of a badly organized function:


def run_store(products, sales):
    for p in products:
        if p["price"] < 0:
            p["price"] = 0
        p["name"] = p["name"].strip().title()

    total = 0
    for sale in sales:
        for p in products:
            if p["name"] == sale["name"]:
                p["stock"] -= sale["qty"]
                total += p["price"] * sale["qty"]

    print("SALES REPORT")
    print("Total revenue:", total)
    for p in products:
        print(p["name"], p["stock"])


This function cleans the products, updates the stock, calculates the revenue and prints the report. That is four jobs in one place.

**Single-purpose functions**

Each function should do only one job. A good way to check is the name: if I need to say "and" to describe what the function does, it should probably be split into two functions. Small functions are easier to read because the name already tells me what happens.

**Parameters and return values**

A function should get what it needs from parameters and give the result back with `return`. In the example above, the total is only printed, so no other part of the program can use it. If the function returns the total, I can use it anywhere, for example to save it or compare it.

**Code reuse**

If the logic is inside a separate function, I can call it again whenever I need it. For example, cleaning a product name is needed when adding a product and also when searching for one. With a function I write it once, and if there is a bug I fix it in one place only. Without it, I would copy and paste the code and have to fix every copy.

**Testing and debugging**

Small functions are easy to test because I can give them simple input and check the output:


assert clean_name("  pen ") == "Pen"
assert apply_sales([{"name": "Pen", "price": 2, "stock": 10}],
                   [{"name": "Pen", "qty": 3}])[1] == 6


If a test fails, I know which function has the problem. With one big function I would have to look through all 100 lines to find the bug.

**How I would divide the program**

I would make one function for each job and then one main function that calls them:


def clean_name(name):
    return name.strip().title()

def clean_products(products):
    cleaned = []
    for p in products:
        cleaned.append({
            "name": clean_name(p["name"]),
            "price": max(p["price"], 0),
            "stock": p["stock"],
        })
    return cleaned

def apply_sales(products, sales):
    total = 0
    for sale in sales:
        for p in products:
            if p["name"] == sale["name"]:
                p["stock"] -= sale["qty"]
                total += p["price"] * sale["qty"]
    return products, total

def build_report(products, total):
    lines = ["SALES REPORT", f"Total revenue: {total}"]
    for p in products:
        lines.append(f"{p['name']}: {p['stock']} left")
    return "\n".join(lines)

def run_store(products, sales):
    products = clean_products(products)
    products, total = apply_sales(products, sales)
    print(build_report(products, total))


Now every function has one job, and `run_store` is short and easy to read: clean the products, apply the sales, print the report. If I want to change how the report looks, I only change `build_report`.



## Question 2: Mutable Data and Function Side Effects

The code from the question:


def add_item(items, item):
    items.append(item)
    return items

products = ["Pen", "Book"]
result = add_item(products, "Bag")

print(products)
print(result)


The output is:


['Pen', 'Book', 'Bag']
['Pen', 'Book', 'Bag']


**Why both results contain the added item**

Lists are mutable, which means they can be changed after they are created. When I pass `products` to the function, Python does not make a copy. The parameter `items` points to the same list in memory as `products`. So `items.append(item)` changes the original list, and the function returns that same list. This means `result` and `products` are just two names for one list. I can check it like this:


print(products is result)   # True


**How lists behave when passed to functions**

The function gets a reference to the list, not a copy. If the function changes the inside of the list (with `append`, `remove`, `sort` or `items[0] = ...`), the change is also seen outside the function. But if the function assigns a new list to the parameter, it only changes the local variable and the original is not affected:


def change_inside(items):
    items.append("X")

def reassign(items):
    items = ["new list"]

nums = [1, 2]
change_inside(nums)
print(nums)    # [1, 2, 'X']
reassign(nums)
print(nums)    # [1, 2, 'X']


**Modifying the existing list vs returning a new list**

When a function modifies the existing list, the original data is changed. This is called a side effect. When a function returns a new list, the original stays the same and I get a separate result. Also, the function in the question does both, it changes the list and returns it, which is confusing because it looks like it made a new list but it did not.

**When modifying the original is useful and when it causes problems**

It is useful when the list is very big and copying it would waste memory and time, or when the function is supposed to update the data, for example adding a product to the store's inventory.

It can cause problems when other parts of the program use the same list and do not expect it to change. Then the bug is hard to find because the change happened inside another function. It is also a problem if I still need the original data later, for example to compare before and after.

**Second example (does not modify the original list)**


def add_item(items, item):
    new_items = items.copy()
    new_items.append(item)
    return new_items

products = ["Pen", "Book"]
result = add_item(products, "Bag")

print(products)   # ['Pen', 'Book']
print(result)     # ['Pen', 'Book', 'Bag']


Here the function makes a copy first, so `products` stays the same and `result` is a new list. One thing to remember is that `.copy()` is only a shallow copy. If the list has other lists inside it, those inner lists are still shared, so for that case I would use `copy.deepcopy()`.