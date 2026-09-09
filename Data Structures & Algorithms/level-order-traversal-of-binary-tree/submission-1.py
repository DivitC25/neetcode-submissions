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
        queue.append((root, [root]))


        while len(queue) > 0:
            currNode, currPath = queue.popleft()
            if len(currPath) in traversalDict:
                traversalDict[len(currPath)].append(currNode.val)
            else:
                traversalDict[len(currPath)] = [currNode.val]
            if currNode.left:
                newPath = currPath + [currNode.left.val]
                queue.append((currNode.left, newPath))
            if currNode.right:
                newPath = currPath + [currNode.right.val]
                queue.append((currNode.right, newPath))
        
        return list(traversalDict.values())

            




        