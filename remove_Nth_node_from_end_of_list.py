"""
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    Example 1:


    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    Example 2:

    Input: head = [1], n = 1
    Output: []
    Example 3:

    Input: head = [1,2], n = 1
    Output: [1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        print("_______________")
        if not head:
            return []
        temp = head
        for _ in range(n): temp = temp.next
        if not temp: return head.next
        n = n - 1
        step = 0
        leader = head
        follower = head
        f_head = follower
        while leader.next:
            if step > n:
                follower = follower.next
            leader = leader.next
            step += 1
        follower.next = follower.next.next
        return f_head
    
def main():
    # Test case 1: Remove the 2nd node from the end of [1,2,3,4,5]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n1 = 2
    result1 = Solution().removeNthFromEnd(head1, n1)
    output1 = []
    while result1:
        output1.append(result1.val)
        result1 = result1.next
    print("Test Case 1:")
    print("Input: [1,2,3,4,5], n = 2")
    print("Output:", output1)
    print()

    # Test case 2: Remove the only node from the end of [1]
    head2 = ListNode(1)
    n2 = 1
    result2 = Solution().removeNthFromEnd(head2, n2)
    output2 = []
    while result2:
        output2.append(result2.val)
        result2 = result2.next
    print("Test Case 2:")
    print("Input: [1], n = 1")
    print("Output:", output2)
    print()

    # Test case 3: Remove the last node from the end of [1,2]
    head3 = ListNode(1, ListNode(2))
    n3 = 2
    result3 = Solution().removeNthFromEnd(head3, n3)
    output3 = []
    while result3:
        output3.append(result3.val)
        result3 = result3.next
    print("Test Case 3:")
    print("Input: [1,2], n = 2")
    print("Output:", output3)
    print()
    
if __name__=='__main__':
    main()