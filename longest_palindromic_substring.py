import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand_palindrome(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                            
            return (i+1, j)
        
        res=(0,0)
        for i in range(n):
            b1 = expand_palindrome(i,i)
            b2 = expand_palindrome(i,i+1) 
            print(s[b1[0]:b1[1]],"|",print(s[b2[0]:b2[1]]) )           
            res=max(res, b1, b2,key=lambda x: x[1]-x[0]+1)
                    
        return s[res[0]:res[1]] 
    
    
def main():
    start = time.time()
    sol = Solution()
    ss = ["babaddtattarrattatddetartrateedredividerb"]
    for s in ss:
        print(sol.longestPalindrome(s))
        
    print(time.time()-start)
    

if __name__=='__main__':
    main()