# Two Sum IV - Input is a BST (Mode: Easy)

class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """

        checked = set()

        def dfs(node):
            if not node:
                return False
            
            if k - node.val in checked:
                return True
            
            checked.add(node.val)
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
