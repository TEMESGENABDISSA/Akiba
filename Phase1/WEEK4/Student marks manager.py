# Student Marks Manager


# list of student marks
original = [75, 80, 65, 90, 85]

# shared reference, this is the same list with a second name
shared = original

# copy of the list, this one is a separate list
copied = original.copy()

# add a new mark to the copy only
copied.append(95)

# show all the lists
print("Original marks:", original)
print("Shared reference:", shared)
print("Copied marks:", copied)

print()

# is checks if it is the same list, == checks if the values are equal
print("Original and shared reference are identical:", original is shared)
print("Original and copied lists have equal values:", original == copied)
print("Original and copied lists are identical:", original is copied)