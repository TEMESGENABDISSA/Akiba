class Solution(object):
    def containsDuplicate(self, nums):
        newvalues = set(nums)

        if len(newvalues) < len(nums):
            return True
        else:
            return False