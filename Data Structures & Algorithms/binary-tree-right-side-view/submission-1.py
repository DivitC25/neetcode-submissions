# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        visible = []
        q.append((root, 0))
        currDepth = 0
        prevNode = None

        while len(q) > 0:
            currNode, depth = q.popleft()
            if prevNode:
                if depth > currDepth:
                    currDepth = depth
                    visible.append(prevNode.val)
            prevNode = currNode
            if currNode.left:
                q.append((currNode.left, depth + 1))
            if currNode.right:
                q.append((currNode.right, depth + 1))
            if len(q) == 0:
                visible.append(currNode.val)

        
        return visible

        