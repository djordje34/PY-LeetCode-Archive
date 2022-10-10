from functools import reduce

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.cache=""
        self.cache+=(reduce(self.getSimilarities,strs))
        
                
        
        return self.cache
        
        
    def getSimilarities(self,s1,s2):
        rtn=""
        if s1=="":
            return s1
        if s2=="":
            return s2
        if not s1:
            return s2
        if not s2:
            return s1
        
        for x in range(min(len(s1),len(s2))):
            if s1[x]==s2[x]:
                rtn+=s1[x]
            else:
                break  
        return rtn

def main():
    
    sol=Solution()
    str=["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    a=["reflower","flow","flight"]
    b=["flower","flower","flower","flower"]
    c=["c","acc","ccc"]
    print(sol.longestCommonPrefix(str))

if __name__=='__main__':
    main()