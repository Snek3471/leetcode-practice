class Solution(object):
    def productExceptSelf(self, nums):
        retlist = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            retlist[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            retlist[i] *= postfix
            postfix *= nums[i]
        return retlist
        