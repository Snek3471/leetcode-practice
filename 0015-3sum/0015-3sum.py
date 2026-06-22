class Solution(object):
    def threeSum(self, nums):
        retlist = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            k = i + 1
            j = len(nums) - 1
            while (k < j):
                if (n + nums[k] + nums[j] < 0):
                    k += 1
                elif (n + nums[k] + nums[j] > 0):
                    j -= 1
                elif (n + nums[k] + nums[j] == 0):
                    retlist.append([n, nums[k], nums[j]])
                    k += 1
                    while (nums[k] == nums[k - 1] and k < j):
                        k += 1
        return retlist
        