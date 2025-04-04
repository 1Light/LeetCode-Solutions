# 463. Island Perimeter (Mode: Easy)

class Solution(object):
    
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        perimeter = 0
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    if i == 0 or grid[i-1][j] == 0:  # check top
                        perimeter += 1
                    if i == len(grid) - 1 or grid[i+1][j] == 0:  # check bottom
                        perimeter += 1
                    if j == 0 or grid[i][j-1] == 0:  # check left
                        perimeter += 1
                    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:  # check right
                        perimeter += 1
        
        return perimeter