'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        # Remove curr1
        left.next = left.next.next
        return dummy.next