words = input("Enter a word: ").strip().lower()
reverse = ""
for letter in words:
    reverse = letter + reverse

print("Word:", words)
print("Reverse:", reverse)

if words == reverse:
    print(f"{words} is a palindrome")
else:
    print(f"{words} is not a palindrome")