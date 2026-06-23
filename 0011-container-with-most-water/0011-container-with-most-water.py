class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxInLoop = 0
            if (height[i] <= height[j]):
                maxArea = max(maxArea, height[i] * (j - i)) 
                i += 1
            elif (height[j] < height[i]):
                maxArea = max(maxArea, height[j] * (j - i))
                j -= 1
        return maxArea
        