# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0
        
        multiplier = 1
        while l1:
            a += (multiplier * l1.val)
            multiplier *= 10
            l1 = l1.next
        
        multiplier = 1
        while l2:
            b += (multiplier * l2.val)
            multiplier *= 10
            l2 = l2.next
        
        final = a + b
        newHead = ListNode(0, None)
        curr = newHead

        while final > 0:
            digit = final % 10
            curr.val = digit
            if final // 10 > 0:
                curr.next = ListNode(0, None)
            else:
                curr.next = None
            curr = curr.next
            final = final // 10
        
        return newHead

        