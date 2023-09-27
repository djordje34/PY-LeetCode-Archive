
class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        huns = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ks   = ["","M","MM","MMM"]
        return ks[num//1000] + huns[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]
        


def main():
    sol = Solution()
    print(sol.intToRoman(1994))

if __name__=='__main__':
    main()