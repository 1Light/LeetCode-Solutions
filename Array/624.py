# 624. Maximum Distance in Arrays (Mode: Medium)

class Solution(object):
    
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        max_distance = 0

        for i in range(1, len(arrays)):
            first, last = arrays[i][0], arrays[i][-1]

            max_distance = max(max_distance, abs(max_val - first), abs(min_val - last))

            min_val = min(min_val, first)
            max_val = max(max_val, last)

        return max_distance
        