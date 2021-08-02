# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True

        fast = slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is None: break

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        one, two = head, prev
        while two:
            if one.val != two.val:
                return False
            one, two = one.next, two.next

        return True

s = Solution()
assert s.isPalindrome(ListNode(1, ListNode(2, ListNode(1))))
assert s.isPalindrome(ListNode(1, ListNode(2))) is False
