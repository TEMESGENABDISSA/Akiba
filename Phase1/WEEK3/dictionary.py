# students = {
#     "abebe": 85,
#     "alemu": 90,
#     "hana": 95
# }

# name= input("Enter student name:")
# name=name.lower()
# if name in students:
#  print('grade',students[name])
# else:
#  print(' name is not found')

# products ={
#  'apple':200,
#  "orange":900
  
# }
# product=input("insert product name ")
# product =product.lower()
# if product in products:
#         print("prices", products[product])
# else:
#         print('product not found')

n = int(input())

phone_book = {}

for i in range(n):
    name, phone = input().split()
    phone_book[name] = phone

search_name = input()
if search_name in phone_book:
    print(phone_book[search_name])
else:
    print("Not found")

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        missing = []
        newnums = []

        for number in range(len(nums) + 1):
            if number not in nums:
                missing.append(number)
                return missing[0]

            else:
                newnums.append(number)

        return False

    
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        store = []
        result = []

        greatest_number = len(nums)
        smallest_number = 0

        for i in range(smallest_number, greatest_number + 1):
            store.append(i)

        for i in store:
            if i not in nums:
                result.append(i)

        return result[0]
