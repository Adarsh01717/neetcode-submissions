# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None and head.next == None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n

        first = head
        sec = prev
        while sec:
            f = first.next
            s = sec.next

            first.next = sec
            sec.next = f

            first = f
            sec = s
        