# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        def helper(node):
            nonlocal traversal
            if not node or len(traversal) == k:
                return
            
            helper(node.left)
            if len(traversal) == k:
                return
            traversal.append(node.val)
            helper(node.right)
        
        helper(root)
        return traversal[-1]

            

        