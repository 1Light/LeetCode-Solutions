# 654. Maximum Binary Tree (Mode: Medium)

class Solution(object):
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        if not nums:
            return None
        
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        root = TreeNode(max_val)
        
        root.left = self.constructMaximumBinaryTree(nums[:max_index])  
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return root