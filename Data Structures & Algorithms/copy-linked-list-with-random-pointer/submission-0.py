"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        forwardMatchDict = {}
        backwardMatchDict = {}
        prevDict = {}
        prev = None
        curr = head
        tail = None

        while curr:
            prevDict[curr] = prev
            if curr.next == None:
                tail = curr
            prev = curr
            curr = curr.next

        newNext = None
        newHead = None
        
        while tail:
            newNode = Node(tail.val, newNext, None)
            forwardMatchDict[tail] = newNode
            backwardMatchDict[newNode] = tail
            newNext = newNode
            if prevDict[tail] == None:
                newHead = newNode
            tail = prevDict[tail]

        curr = newHead

        while curr:
            bMatch = backwardMatchDict[curr]
            oldRandom = bMatch.random
            if oldRandom == None:
                curr.random = None
            else:
                newRandom = forwardMatchDict[oldRandom]
                curr.random = newRandom
            curr = curr.next
        
        return newHead




