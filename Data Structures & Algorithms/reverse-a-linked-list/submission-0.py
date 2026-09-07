# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prevNode = None
        startNode = None
        while currNode:
            newNode = ListNode(currNode.val)
            if prevNode:
                newNode.next = prevNode
            prevNode = newNode
            startNode = newNode
            if currNode.next:
                currNode = currNode.next
            else:
                return startNode
    
            
        

        