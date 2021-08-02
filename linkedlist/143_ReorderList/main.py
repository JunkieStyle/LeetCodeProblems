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
    def reorderList(self, head: ListNode) -> None:
        fast = slow = head
    
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
                
        curr = slow
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        dummy = ListNode(-1)
        tail = prev
        prev = dummy
        while tail:
            prev.next, head = head, head.next
            if tail != prev.next:
                prev.next.next, tail = tail, tail.next
                prev = prev.next.next
            else:
                break
        return dummy.next
