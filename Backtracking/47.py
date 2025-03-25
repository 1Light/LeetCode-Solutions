# Permutation || (Mode: Medium)

class Solution(object):
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        permutation = []
        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1
        
        def backtrack():

            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for n in count:
                if count[n] > 0:
                    permutation.append(n)
                    count[n] -= 1

                    backtrack()

                    count[n] += 1
                    permutation.pop()
        
        backtrack()
        return result
