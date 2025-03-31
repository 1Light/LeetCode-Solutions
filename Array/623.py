# 623. Add One Row to Tree (Mode: Medium)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """

        if depth == 1:
            return TreeNode(val, left=root)
        
        queue = [root]
        current_depth = 1
        
        while queue:
            if current_depth == depth - 1:
                for node in queue:
                    node.left = TreeNode(val, left=node.left)
                    node.right = TreeNode(val, right=node.right)
                return root
            
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            queue = next_level
            current_depth += 1
        
        return root
        