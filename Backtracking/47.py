# Permutation || (Mode: Medium)

class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # list to add permutations
        result = []

        # sort list to gather duplicates
        nums.sort()

        # create used list to check status
        used = [False] * len(nums)

        def backtrack(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue
                
                # here, the only case where the nums[i] is not used is iteration reaches nums[i-1]
                # is if the code initially used nums[i] as the start node and then saw every other path
                # hence, it backtracked out of it and is now trying other elements different from nums[i]
                # if we were to not set the code block below, we would be setting nums[i-1] as the start node
                # since nums[i] = nums[i-1], this would cause duplication in path
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False
        
        backtrack([])
        return result