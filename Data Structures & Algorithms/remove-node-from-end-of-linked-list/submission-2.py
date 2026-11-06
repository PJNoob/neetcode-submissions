# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        dummyNode = ListNode()
        slow = dummyNode
        slow.next = head

        # while(n != 1):
        #     n = n - 1
        #     fast = fast.next
        for i in range(1,n):
            fast = fast.next

        while(fast):
            if(fast.next is None):
                slow.next = slow.next.next
            slow = slow.next
            fast = fast.next

        return dummyNode.next


