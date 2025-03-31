# 832. Flipping an Image (Mode: Easy)

class Solution(object):
    
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in image:
            row.reverse()
            row[:] = [1 - x for x in row]
        
        return image
        