'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        if head == None: return None
        mid = self.findMidpoint(head)
        
        # reverse the second half of the list from mid
        head2 = self.reverseLinkedList(mid.next)
        mid.next = None

        # merge the two linked lists
        curr = head
        while curr and head2:
            temp = head2.next
            
            head2.next = curr.next
            curr.next = head2
            curr = head2.next
            
            head2 = temp
        
    def reverseLinkedList(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def findMidpoint(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow