class Solution(object):
    def twoSum(self, nums, target):
        myhash = {}

        for i, n in enumerate(nums): 
            if (target - n) in myhash:
                return [myhash[target - n], i]
            myhash[n] = i
        