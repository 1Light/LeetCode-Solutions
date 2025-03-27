# 561. Array Partition (Mode: Easy)

class Solution(object):
    
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the array so that when paired, the values at even index are smaller
        # min(a, b) = a - since a is the smallest after sorting
        nums.sort()
    
        total_sum = 0
        for i in range(0, len(nums), 2):
            total_sum += nums[i]
        
        return total_sum