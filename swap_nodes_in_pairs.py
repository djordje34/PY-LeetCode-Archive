"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""
from pyparsing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head):

        if not head or not head.next:
            return head
        
        curr = head.next
        head.next = self.swapPairs(head.next.next)
        curr.next = head
        
        return curr


def main():
    sol = Solution()
    
    ls = ListNode(7,ListNode(2,ListNode(5,ListNode(1))))

    res = sol.swapPairs(ls)
    
    while res:
        print(res.val)
        res = res.next
    
if __name__=='__main__':
    main()