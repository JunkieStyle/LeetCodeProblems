from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        size = 0
        dummy = ListNode(None, head)
        node = dummy
        while node.next:
            size += 1
            node = node.next
            
        last = node
        last.next = head
        
        k = k % size
        
        node = dummy
        while size - k:
            k += 1
            node = node.next
        
        dummy.next = node.next
        node.next = None
        return dummy.next
        
