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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = second = head
        for _ in range(n): 
            first = first.next
          
        dummy = ListNode(0, second)
        prev = dummy
        while first:
            prev = second
            first = first.next
            second = second.next

        prev.next = second.next

        return dummy.next


s = Solution()
print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 1).to_list())
