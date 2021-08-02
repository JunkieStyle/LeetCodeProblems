# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        first = headA
        second = headB
        while first != second:
            first = headB if not first else first.next
            second = headA if not second else second.next

        return first


s = Solution()
common = ListNode(10, ListNode(20))
# print(s.getIntersectionNode(ListNode(1, ListNode(2, common)), ListNode(-1, common)).val)
print(s.getIntersectionNode(ListNode(-1, common), ListNode(1, ListNode(2, common))).val)