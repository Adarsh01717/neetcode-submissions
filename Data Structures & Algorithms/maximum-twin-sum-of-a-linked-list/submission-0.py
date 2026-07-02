# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # convert it into array

        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        # two pointer approch

        i = 0
        j = len(arr)-1
        sum = 0

        while i<j:
            sum = max(sum, arr[i] + arr[j])
            i = i + 1
            j = j -1
        return sum