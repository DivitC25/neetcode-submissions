# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        self.helper(root)
        return root

    


        