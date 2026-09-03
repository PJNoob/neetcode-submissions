# Start two pointers at the head: slow moves one node at a time, while fast moves two nodes at a time.
# If there is no cycle, fast will eventually reach None because it will reach the end of the linked list.
# If there is a cycle, both pointers will eventually enter the cycle.
# Inside the cycle, fast will catch up to slow because fast is moving two steps while slow is moving one step.
# If slow == fast, both pointers are at the same node, which proves that a cycle exists.
# The condition while fast and fast.next ensures that we can safely move fast two nodes forward without accessing None.
# If the loop ends without slow == fast, fast reached the end, so there is no cycle.

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False