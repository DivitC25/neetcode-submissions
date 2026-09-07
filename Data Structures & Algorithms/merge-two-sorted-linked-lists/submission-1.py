# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2

        if not one:
            return two
        elif not two:
            return one

        if one.val > two.val:
            head = ListNode(two.val, None)
            two = two.next
        else:
            head = ListNode(one.val, None)
            one = one.next

        prev = head
        
        
        while one and two:
            if one.val > two.val:
                prev.next = ListNode(two.val)
                prev = prev.next
                two = two.next
            elif one.val < two.val:
                prev.next = ListNode(one.val)
                prev = prev.next
                one = one.next
            else:
                prev.next = ListNode(one.val)
                prev = prev.next
                prev.next = ListNode(two.val)
                prev = prev.next
                one = one.next
                two = two.next

        if one:
            while one:
                prev.next = ListNode(one.val)
                prev = prev.next
                one = one.next
        else:
            while two:
                prev.next = ListNode(two.val)
                prev = prev.next
                two = two.next
        
        return head
                

                    
        


        