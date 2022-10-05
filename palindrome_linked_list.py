# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def __init__(self):
        self.head=None

    
    def checkIfPal(self,str):
        return str[::-1]==str
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.head=head
        node=self.head
        
        temp=[]
        while (node is not None):
            temp.append(node.val)
            node = node.next
        return self.checkIfPal(temp)
  
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val,end=" ")
            temp = temp.next
        

def main():
        
    x=Solution()
    llist = Solution()
    llist.head = ListNode('1')
    llist.head.next = ListNode('2')
    llist.head.next.next = ListNode("3")
    llist.head.next.next.next = ListNode("2")
    llist.head.next.next.next.next = ListNode("1")
    llist.printList()
    print (llist.isPalindrome(llist.head))

if __name__=='__main__':
    main()