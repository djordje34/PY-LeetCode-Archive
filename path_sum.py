# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    global i
    i=0
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        global i
        s=targetSum
        if not root:
            return False
        else:

            if s==0:
                return True
            else:
                if root.left:
                    
                    if self.hasPathSum(root.left,s):
                        return True
                if root.right:
                    
                    if self.hasPathSum(root.right,s):
                        return True
                    
            return False

        


def main():
    o=TreeNode()
    o.val=1
    o.right=TreeNode(val=2)
    #o.right=TreeNode(val=3)
    #o.left.left=TreeNode(val=4)
    #o.left.right=TreeNode(val=5)
    #o.right.left=TreeNode(val=6)
    #o.right.right=TreeNode(val=7)
    sol=Solution()
    sol.root=o
    print(sol.hasPathSum(o,1))

if __name__=='__main__':
    main()