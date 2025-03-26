# 892. Surface Area of 3D Shapes (Mode: Easy)

class Solution(object):
    
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        total_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    total_area += 6 * grid[i][j] - 2 * (grid[i][j] - 1)
                
                if i > 0:
                    total_area -= 2 * min(grid[i][j], grid[i-1][j]) 
                if j > 0:
                    total_area -= 2 * min(grid[i][j], grid[i][j-1])
        
        return total_area 