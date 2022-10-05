class Solution(object):
    def isPalindrome(self, x):  #MEMORY WISE
        """
        :type x: int
        :rtype: bool
        """
        val=str(x)
        if x<0:
            return False
        else:
            return val==val[::-1]
        
    def isPalindrome2(self,x):  #RUNTIME WISE
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            val=str(x)
            rval=val[::-1]
            return val==rval