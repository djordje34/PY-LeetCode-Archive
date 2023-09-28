class Solution:
    def conv(self,s:str) -> int:
        try:
            return int(float(s))
        except:
            return 0
    
    def myAtoi(self, s: str) -> int:
        y = 2 ** 31
        z = ''
        numsig = False;
        for ss in s.strip():
            if ss.isdigit():
                numsig = True
            if ss.isalpha() or ss == ' ' or (ss in ('-','+') and numsig): 
                z = self.conv(z)
                return z if abs(z)<(y) else ((z > 0) - (z < 0))*(y-(z>0))
            z=z+ss
        z = self.conv(z)
        return z if abs(z)<(y) else ((z > 0) - (z < 0))*(y-(z>0))


def main():
    sol = Solution()
    print(sol.myAtoi("-123-"))
if __name__=='__main__':
    main()