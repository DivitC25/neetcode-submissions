# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevDict = {}
        tail = None
        prev = None
        curr = head

        while curr:
            prevDict[curr] = prev
            if curr.next == None:
                tail = curr
            prev = curr
            curr = curr.next
        
        counter = 1

        while counter < n:
            tail = prevDict[tail]
            counter += 1
        
        if prevDict[tail] == None:
            return tail.next

        repPrevious = prevDict[tail]
        repNext = tail.next
        repPrevious.next = repNext
        tail = repPrevious

        while prevDict[tail]:
            tail = prevDict[tail]

        return tail
            


        