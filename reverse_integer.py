class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val=str(x)
        if x <0:
            abn=val[1:]
            rtn=int("-"+abn[::-1])
            if rtn>-2147483648:
                return int("-"+abn[::-1])
            else:
                return 0
        else:
            rtn=int(val[::-1])
            if rtn<2147483648:
                return rtn
            else: return 0
            
            


def main():
    sol=Solution()
    print(sol.reverse(2147483648))

if __name__=='__main__':
    main()
        
