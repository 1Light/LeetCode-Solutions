# Two Sum (Mode: Easy)

class Solution(object):
    def twoSum(self, nums, target):

        num_to_index = {}

        # Let's say num1 + num2 = target

        for index, num1 in enumerate(nums):

            num2 = target - num1

            if num2 in num_to_index:
                return [num_to_index[num2], index]

            num_to_index[num1] = index

        return []
