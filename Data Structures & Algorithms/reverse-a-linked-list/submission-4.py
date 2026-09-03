# Stiver

# Reach the end of the linked list recursively by calling self.reverseList(head.next).
# The base case is when there is only one node left, or the list is empty: head == None or head.next == None.
# At the base case, return that last node because it will become the newHead of the reversed list.
# While recursion is returning, head.next is the node that comes immediately after the current node.
# Store that next node in prev using prev = head.next.
# Reverse the connection using prev.next = head, so instead of head → prev, we now have prev → head.
# Break the old connection using head.next = None, otherwise you would create a cycle.
# Keep returning newHead because the last node of the original list is now the first node of the reversed list.

# Time: O(n) — every node is visited once.
# Space: O(n) — due to the recursive call stack.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if (head == None or head.next == None):
            return head

        newHead = self.reverseList(head.next)
        prev = head.next
        prev.next = head
        head.next = None
        return newHead