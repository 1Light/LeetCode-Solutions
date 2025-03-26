# 441. Arranging Coins (Mode: Easy)

class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2

            # coins_needed is the sum of coins until the row 'mid'
            coins_needed = (mid * (mid + 1)) // 2
            
            # if equal, it means all the rows until and including the row 'mid' can be filled
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right