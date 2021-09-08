from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        curr = dummy.next
        
        while curr:
            count = 1
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                count += 1
            
            if count > 1:
                prev.next = curr.next
                curr = prev.next 
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next
