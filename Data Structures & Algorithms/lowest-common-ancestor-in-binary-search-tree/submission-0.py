# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trace(self, root, target):
        if root == target:
            return [root]
        elif root.val > target.val:
            return [root] + self.trace(root.left, target)
        else:
            return [root] + self.trace(root.right, target)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pTrace = self.trace(root, p)
        qTrace = self.trace(root, q)

        for i in range(min(len(pTrace), len(qTrace)) - 1, -1, -1):
            if pTrace[i] == qTrace[i]:
                return pTrace[i]


        