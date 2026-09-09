import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Put the first node of every non-empty linked list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Attach the smallest available node to our merged list
            curr.next = node
            curr = curr.next

            # The next node from this same linked list is now a candidate
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        

                



        