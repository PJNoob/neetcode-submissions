# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = tail1 = curr = head
        dummy = ListNode(-1)
        dummy.next = curr

        while(fast and fast.next):
            tail1 = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        head1 = head
        head2 = self.reverse(mid)

        temp1,temp2 = head1, head2

        while(temp1.next and temp2.next):
            temp1 = temp1.next
            curr.next = temp2
            curr = curr.next
            temp2 = temp2.next
            curr.next = temp1
            curr = curr.next

        head = dummy.next
        
            
    
    def reverse(self,head: Optional[ListNode]):
        prev = None
        curr = head

        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev