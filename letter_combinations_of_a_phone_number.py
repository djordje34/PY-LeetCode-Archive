"""
    Given a string containing digits from 2-9 inclusive, return all 
    possible letter combinations that the number could represent. 
    Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
    """

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        rtn = []
        init = False
        comb = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        for num in digits:
            if not init:
                rtn = ([x for x in comb[num]])
                init = True
                continue
            rtn = [x+y for x in rtn for y in comb[num]]
        return rtn

def main():
    print(Solution().letterCombinations("234"))

if __name__=='__main__':
    main()