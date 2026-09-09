# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root, subRoot):
        if (not root and subRoot) or (root and not subRoot):
            return False
        if not root and not subRoot:
            return True
        if root.val != subRoot.val:
            return False
        
        left = self.sameTree(root.left, subRoot.left)
        right = self.sameTree(root.right, subRoot.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
        

        