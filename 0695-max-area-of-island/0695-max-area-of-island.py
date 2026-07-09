class Solution(object):
    def maxAreaOfIsland(self, grid):
        # All this is the same as the count island question
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        maxarea = 0 
        
        # Small change here, return area 
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                # Base case, returns 0
                return 0
            # Sets the cell to 0 to avoid recurrence 
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                # Keeps adding on 1 until everything exits
                area += dfs(r + dr, c + dc)

            # Returns the final area 
            return area
        
        # Small change here too, just find the max
        for r in range(rows):
            for c in range(cols):
                # Find the area of a specific island
                area = dfs(r, c)
                # Use max function to get the max
                maxarea = max(maxarea, area)
        
        return maxarea
        