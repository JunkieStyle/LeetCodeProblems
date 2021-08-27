from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        
        carry = 0
        dummy = ListNode(0, None)
        result = dummy
        
        while node1 or node2:
            node = ListNode(carry, None)   
            if node1 is not None:
                node.val += node1.val
                node1 = node1.next
            if node2 is not None:
                node.val += node2.val
                node2 = node2.next
                
            carry = node.val // 10
            node.val %= 10
            
            dummy.next = node
            dummy = node
            
        if carry:
            dummy.next = ListNode(carry, None)
            
        return result.next
