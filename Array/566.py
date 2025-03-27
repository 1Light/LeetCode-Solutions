# 566. Reshape the Matrix (Mode: Easy)

class Solution(object):

    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        m, n = len(mat), len(mat[0])
    
        # check if reshape is possible
        if m * n != r * c:
            return mat
        
        # flatten mat into a 1D list
        flat_list = [elem for row in mat for elem in row]
        
        # create the reshaped matrix
        reshaped_matrix = []
        
        for i in range(r):
            # (ic) to (i+1)c inorder to include the last column when slicing
            reshaped_matrix.append(flat_list[i*c : (i+1)*c])
        
        return reshaped_matrix
            