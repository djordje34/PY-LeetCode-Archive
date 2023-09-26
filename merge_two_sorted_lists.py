# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        curr = res
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return res.next


def main():
    l1 = None
    l2 = None
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    print(result) 
    print("T1")
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = None
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("T2")
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("T3")
if __name__=='__main__':
    main()