# 832. Flipping an Image (Mode: Easy)
# Both don't create a new matrix, so O(1) space complexity

class Solution(object):
    
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in image:
            row.reverse()
            for col in range(len(row)):
                row[col] ^= 1
        
        return image