# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        temp = dummyNode
        c1 = list1
        c2 = list2

        while(c1 and c2):
            if(c1 and c1.val <= c2.val):
                temp.next = c1
                temp = temp.next
                c1 = c1.next
            
            else:
                temp.next = c2
                temp = temp.next
                c2 = c2.next

        if(c1):
            temp.next = c1

        elif(c2):
            temp.next = c2

        return dummyNode.next