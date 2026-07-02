class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Set to keep track of duplicate characters. 
        slice = set()
        l = 0
        r = 0
        res = 0 
        # Standard loop. 
        for r in range(len(s)):
            # Removes characters from the left until the right
            # one can be inserted in the set. 
            while s[r] in slice:
                slice.remove(s[l])
                # Increments left pointer accordingly. 
                l += 1
            # Adds right most pointer after removing whats necessary. 
            slice.add(s[r])
            # Finding the max length. Adds 1 because of 0 based indexing. 
            res = max(res, r - l + 1)
        return res
        