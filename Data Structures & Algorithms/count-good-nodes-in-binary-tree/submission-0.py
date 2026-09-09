# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        gCount = 0
        queue.append((root, root.val))

        while len(queue) > 0:
            currNode, currMax = queue.popleft()
            if currNode.val >= currMax:
                gCount += 1
            newMax = max(currNode.val, currMax)

            if currNode.left:
                queue.append((currNode.left, newMax))
            if currNode.right:
                queue.append((currNode.right, newMax))
        
        return gCount