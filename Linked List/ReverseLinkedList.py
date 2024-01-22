'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        prev = None
        front = head
        
        while front and front.next:
            nextNode = front.next
            nextNode.next = front
            front.next = prev
            prev = front
            front = nextNode
        
        return front    
            
        
solution = Solution()
solution.reverseList(ListNode())