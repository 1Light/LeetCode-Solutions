# 594. Longest Harmonious Subsequence (Mode: Easy)

class Solution(object):
    
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
    
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        max_length = 0
        
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
        
        return max_length