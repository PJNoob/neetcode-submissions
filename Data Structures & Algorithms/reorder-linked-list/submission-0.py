# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # finding the middile of the linked list
        # while fast or fast.next:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # setting the start of the second half of the list
        second = slow.next

        # break the link between the two lists
        slow.next = None

        #setting prev for reversing the linked list
        prev = None

        # reversing the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #as prev would be the head of the reversed linked list so putting second as the head
        second = prev
        #first linked list from the head
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


