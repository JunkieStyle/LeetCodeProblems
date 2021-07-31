# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def to_list(self):
        res = []
        curr = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            cached = curr.next
            curr.next = prev
            prev = curr
            curr = cached

        return prev



s = Solution()
assert s.reverseList(ListNode(1, ListNode(2, ListNode(3)))).to_list() == [3, 2, 1]
assert s.reverseList(ListNode(1)).to_list() == [1]