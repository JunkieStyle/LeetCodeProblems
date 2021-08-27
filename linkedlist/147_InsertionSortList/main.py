# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        
        while node.next:
            node2 = dummy
            while node.next.val > node2.next.val:
                node2 = node2.next
                
            if node2 == node:
                node = node.next
                continue
            
            insert = node.next
            node.next = insert.next
            insert.next = node2.next
            node2.next = insert
        
        return dummy.next
