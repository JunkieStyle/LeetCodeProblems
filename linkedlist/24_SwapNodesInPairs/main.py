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

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def swapPairs(self, head):
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

s = Solution()
print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))).to_list())



