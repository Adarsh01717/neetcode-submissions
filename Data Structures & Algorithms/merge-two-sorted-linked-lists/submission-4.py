# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        arr = []
        curr = list1
        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        d = ListNode
        tail = d

        for n in arr:
            tail.next = ListNode(n)
            tail = tail.next

        return d.next
        