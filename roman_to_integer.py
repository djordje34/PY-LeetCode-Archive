from functools import reduce

from numpy import argmin

class Solution(object):
    def __init__(self):
         self.lc=0
    def romanMap(self):
        return {
            "I":1,
            "IX":9,
            "XL":40,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
    def rMap(self):
                return {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    def reducer(self,x,y):
        if self.lc==0:self.lc=x
            
        if x<y or self.lc<y:
            x+=y
        else:
            if self.lc>y:
                x=y-x
            else:
                x+=y
        x=abs(x)
        self.lc=y
        print(x,self.lc,end="\n")
        return x
    
    
        
    def romanToInt(self, s):
        mp=self.rMap()

        x=reduce(self.reducer,[mp[x] for x in s][::-1])
        print(x)
        return x
    
    
    def fasterSol(self,s):
        sm=0
        mp=self.romanMap()
        i=0
        while i<len(s):
            if i+1<len(s) and s[i:i+2] in mp:
                sm+=mp[s[i:i+2]]
                print(mp[s[i:i+2]],"MAPS TO",s[i:i+2],end=" ")
                print(i,"!")
                i+=2
                print(i,"!")
            else:
                sm+=mp[s[i]]
                print(mp[s[i]],end=" ")
                i+=1
            print(sm)
        return sm
        
def main():
    sol=Solution()
    print(sol.fasterSol("MCMXCIV"))

if __name__=='__main__':
    main()