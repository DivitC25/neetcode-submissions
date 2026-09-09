# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversalDict = {}
        queue = deque()
        queue.append((root, 0))


        while len(queue) > 0:
            currNode, currDepth = queue.popleft()
            if currDepth in traversalDict:
                traversalDict[currDepth].append(currNode.val)
            else:
                traversalDict[currDepth] = [currNode.val]
            if currNode.left:
                newDepth = currDepth + 1
                queue.append((currNode.left, newDepth))
            if currNode.right:
                newDepth = currDepth + 1
                queue.append((currNode.right, newDepth))
        
        return list(traversalDict.values())

            




        