# 744. Find Smallest Letter Greater Than Target (Mode: Easy)

class Solution(object):
    
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        # Binary search initialization
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left % len(letters)]