# Subsets II (Mode: Medium)

class Solution(object):
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        def backtrack(start, current_subset):
            result.append(list(current_subset))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)

                current_subset.pop()
        
        backtrack(0, [])
        return result
