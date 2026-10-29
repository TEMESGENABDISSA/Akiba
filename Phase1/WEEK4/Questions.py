# Week 4 - Mutability, References and Memory
# Name: Temesgen Abdissa

import sys

# ---------- Question 1 ----------
print("Question 1")

# list is mutable so we can change it directly
my_list = [1, 2, 3]
print("list before:", my_list, id(my_list))
my_list.append(4)
print("list after:", my_list, id(my_list))
# the id is the same, so it is still the same list

# string is immutable, it cannot be changed
my_string = "hello"
print("string before:", my_string, id(my_string))
my_string = my_string + " world"
print("string after:", my_string, id(my_string))
# the id is different now, python made a new string

# ---------- Question 2 ----------
print()
print("Question 2")

a = [10, 20, 30]
b = a              # b just points to the same list as a
c = [10, 20, 30]   # c is a new list that looks the same

print(a is b)   # True, same list
print(a is c)   # False, different lists
print(a == c)   # True, the values are the same

# ---------- Question 3 ----------
print()
print("Question 3")

numbers = [1, 2, 3]
values = numbers   # not a copy, both names use the same list
values.append(4)

print(numbers)   # [1, 2, 3, 4]
print(values)    # [1, 2, 3, 4]
# numbers changed too because it is the same list

# fixed version, using copy()
numbers = [1, 2, 3]
values = numbers.copy()
values.append(4)

print(numbers)   # [1, 2, 3]
print(values)    # [1, 2, 3, 4]

# ---------- Question 4 ----------
print()
print("Question 4")

def update_list(items):
    items.append(100)

scores = [50, 60, 70]
update_list(scores)
print(scores)   # [50, 60, 70, 100]
# the function got the same list so the original changed

# new version that does not change the original
def new_list(items):
    result = items + [100]   # + makes a new list
    return result

scores = [50, 60, 70]
updated = new_list(scores)
print(scores)    # [50, 60, 70]
print(updated)   # [50, 60, 70, 100]

# ---------- Question 5 ----------
print()
print("Question 5")

data = [1, 2, 3]
other = data   # two names for one list

# getrefcount shows how many names point to the list
# it always shows 1 extra because of the function call, so I minus 1
print("names before del:", sys.getrefcount(data) - 1)

del data   # this only removes the name data
print("other still works:", other)
print("names after del:", sys.getrefcount(other) - 1)

del other  # now nothing points to the list so python deletes it