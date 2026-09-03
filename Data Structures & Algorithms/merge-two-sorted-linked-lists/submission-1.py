# Create a dummy node to act as a temporary starting point for the merged list.
# Create a tail pointer that always points to the last node of the merged list.
# Traverse both linked lists simultaneously while both lists still have nodes.
# Compare the values of the current nodes in list1 and list2.
# Attach the smaller node to tail.next, because the merged list must remain sorted.
# Move the corresponding list pointer forward (list1 or list2) because that node has been used.
# Move tail forward to point to the new last node in the merged list.
# Repeat the process until one of the lists becomes empty.
# Attach the remaining nodes of the non-empty list directly to tail.next, because they are already sorted.
# Return dummy.next, because dummy itself is just a placeholder and the actual merged list starts from the next node.

# Time Complexity: O(n + m) where:
# n = length of list1
# m = length of list2
# Space Complexity: O(1) extra space because no new nodes are created; existing nodes are reused.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next