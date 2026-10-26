
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
