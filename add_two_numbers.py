class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        tmp=[]
        l3=ListNode()
        fi=0
        v1,v2=1,1
        avail1,avail2=1,1
        while l1 or l2:
        
            if not l1 or not avail1:
                v1=0
            else:
                v1=l1.val            
            if(not l1.next):
                avail1=0

            print("OCITANA VREDNOST",v1,end=" ")
            if not l2 or avail2==0:
                v2=0
            else:
                v2=l2.val                
            if not l2.next:
                avail2=0
            print("OCITANA VREDNOST2",v2,end=" ")
            temp=v2+v1+carry
            carry=temp//10
            temp=temp%10
            print(v1,v2,carry,"PISE SE",temp)
            l3.val=temp
            if fi==0:
                orig=l3
            fi+=1
            if avail1:
                l1=l1.next
            if avail2:
                l2=l2.next
            if avail1 or avail2:
                l3.next=ListNode()
                l3=l3.next
            if not (avail1 or avail2):
                break
        if carry==1:
            l3.next=ListNode(val=carry)
        return orig
    
    def printList(self,l):
        print("\n")
        while l:
            print(l.val,end=" ")
            l=l.next
            
        


def main():
    l1=ListNode(val=2)
    l1.next=ListNode(val=4)
    l1.next.next=ListNode(val=3)
    #l1.next.next.next=ListNode(val=9)
    #l1.next.next.next.next=ListNode(val=9)
    #l1.next.next.next.next.next=ListNode(val=9)
    #l1.next.next.next.next.next.next=ListNode(val=9)
    
    l2=ListNode(val=5)
    l2.next=ListNode(val=6)
    l2.next.next=ListNode(val=4)
    #l2.next.next.next=ListNode(val=9)

    x=Solution()
    fin=x.addTwoNumbers(l1,l2)
    x.printList(fin)

if __name__=='__main__':
    main()