# 832. Flipping an Image (Mode: Easy)
# Slower as it creates a new list and assigns it to the row[:] for every row

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
        