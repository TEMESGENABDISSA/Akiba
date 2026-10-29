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
