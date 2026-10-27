class Solution(object):
    def missingNumber(self, nums):
        store =[]
        result=[]
        greatest=len(nums) 
        small =0 
        for i in range(small,greatest +1):
            store.append(i)
        for i in store:
            if i not in nums:
               result.append(i)
        else:
                return  result [0]
