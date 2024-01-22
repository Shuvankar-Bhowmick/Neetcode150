'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        head = ListNode()
        res = head
        while curr1 and curr2:
            if curr1.val <= curr2.val: 
                res.next = curr1
                res = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                res = curr2
                curr2 = curr2.next
                
        res.next = curr1 or curr2    
        return head.next 
    