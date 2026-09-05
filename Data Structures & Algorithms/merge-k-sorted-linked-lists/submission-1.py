# Time complexity = O(k log k) + O(N log k) = O(N log k)
# Space complexity = o(k)

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    # Function to merge k sorted linked lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Create a dummy node to act as the starting point of our result list
        dummy = ListNode()

        # Keep a pointer called 'current' that tells us where to add the next node
        current = dummy

        # Create an empty min-heap
        # The heap will always contain the smallest available node from each list
        heap = []

        # Go through every linked list along with its index
        for i, node in enumerate(lists):

            # Check if the current linked list is not empty
            if node:

                # Add the first node of the linked list to the min-heap
                # node.val -> value used for comparison
                # i        -> list index, used to break ties when values are equal
                # node     -> actual linked-list node
                heapq.heappush(heap, (node.val, i, node))

        # Continue until there are no nodes left in the heap
        while heap:

            # Remove the node with the smallest value from the min-heap
            # val  -> value of the node
            # i    -> index of the linked list this node belongs to
            # node -> actual linked-list node
            val, i, node = heapq.heappop(heap)

            # Attach the smallest node to the end of our result linked list
            current.next = node

            # Move current forward to the node we just added
            current = current.next

            # Check if the node we just removed has another node after it
            if node.next:

                # Add the next node from the same linked list to the heap
                # This keeps the smallest available node from that list in the heap
                heapq.heappush(heap, (node.next.val, i, node.next))

        # dummy itself is an extra node, so return the actual first node of the result
        return dummy.next
