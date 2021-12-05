# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        info = deque()
        curr = head
        
        while curr:
            info.append(curr.val)
            curr = curr.next
        
        while len(info) >= 2:
            if info.popleft() != info.pop():
                return False
            
        return True