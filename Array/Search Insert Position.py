# Search Insert Position (Mode: Easy)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for index, num in enumerate(nums):
            if num >= target:
                return index
        
        return len(nums)