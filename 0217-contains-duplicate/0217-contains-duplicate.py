class Solution(object):
    def containsDuplicate(self, nums):
        myhash = set()
        for n in nums:
            if n in myhash:
                return True
            myhash.add(n)
        return False
        