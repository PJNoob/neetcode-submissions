# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # created a dummy node with '0' value and head as the next node
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # we can't directlty put right = head + n as this is a linked list not a list
        while n > 0 and right:
            right = right.next
            n -= 1

        # reaching the desired node
        while right:
            left = left.next
            right = right.next

        # deleting the nth node from the end
        left.next = left.next.next

        return dummy.next
