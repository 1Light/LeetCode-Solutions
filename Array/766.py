# 766. Toeplitz Matrix (Mode: Easy)

class Solution(object):
    
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows - 1):  
            for j in range(cols - 1):  
                if matrix[i][j] != matrix[i + 1][j + 1]:  
                    return False  

        return True  