# Start with prev = None because after reversing the list, the original first node will become the last node, so its next should point to None.
# Set curr = head because we start processing the linked list from the first node.
# Traverse the list while curr is not None so that we process every node exactly once.
# Store the next node in nxt using nxt = curr.next because we are about to change curr.next, and we don't want to lose the rest of the linked list.
# Reverse the current node's pointer using curr.next = prev, making the current node point backward instead of forward.
# Move prev to curr because the current node has now become the first node of the reversed portion.
# Move curr to nxt so that we can continue processing the remaining original list.
# Repeat this process until curr becomes None, meaning every node has been reversed.
# Return prev because prev is now pointing to the new head of the reversed linked list.

# Time Complexity: O(n) — every node is visited exactly once.
# Space Complexity: O(1) — only three pointers (prev, curr, nxt) are used.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
