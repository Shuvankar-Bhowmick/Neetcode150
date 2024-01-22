'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        
        while len(lists) > 1:
            mergedList = []    
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList
        
        return lists[0]    
    
    def mergeLists(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        
        curr1, curr2 = head1, head2
        dummy = res = ListNode()
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            res = res.next
        res.next = curr1 or curr2
        return dummy.next    