class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxArea = 0
        maxL = height[l]
        maxR = height[r]
        
        while l < r:
            if (maxL < maxR):
                l += 1
                maxL = max(maxL, height[l])
                maxArea += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxArea += maxR - height[r]
                
        return maxArea
        