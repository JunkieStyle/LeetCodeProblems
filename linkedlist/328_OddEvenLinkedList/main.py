from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 1
        node = head
        odd_head = ListNode(0)
        even_head = ListNode(0)
        odd = odd_head
        even = even_head
        
        while node:
            if index % 2:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next

            node = node.next 
            index += 1
            
        odd.next = even_head.next
        even.next = None
        return odd_head.next
