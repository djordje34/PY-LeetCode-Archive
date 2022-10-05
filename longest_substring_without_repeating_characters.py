class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        lptr=0
        arr=[]
        val=0
        for rptr in range(len(s)):
            while s[rptr] in arr:
                print(arr)
                print(f"REMOVED {s[lptr]}")
                arr.remove(s[lptr])
                print(arr)
                lptr+=1
            arr.append(s[rptr])
            val=max(val,rptr-lptr+1)
            
        return val
    
    


def main():
    sol=Solution()
    
    print(sol.lengthOfLongestSubstring("abcdefghiijkli"))

if __name__=='__main__':
    main()