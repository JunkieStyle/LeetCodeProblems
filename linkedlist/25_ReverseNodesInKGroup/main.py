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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head is None:
            return head

        index = 0
        out = ListNode(0, head)
        ohead = out
        curr = head

        while curr:
            index += 1
            if index % k == 0:
                otail = curr.next
                whead, wtail = self.reverse(ohead.next, curr.next)
                ohead.next = whead
                wtail.next = otail
                ohead = wtail
                curr = wtail.next
            else:
                curr = curr.next
        
        return out.next

    
    def reverse(self, head, tail):
        curr, prev = head, None
        while curr != tail:
            curr.next, prev, curr = prev, curr, curr.next
        return prev, head
            


s = Solution()
print(s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2).to_list())
