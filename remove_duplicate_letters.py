"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
from itertools import combinations
from itertools import permutations
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    print(seen,stack, sep='\t')
                    seen.discard(stack.pop())
                print(char, sep='\t')
                seen.add(char)
                stack.append(char)
        return ''.join(stack)
        #return "".join(mini for mini in min([list(x) for x in permutations(list(s),len(set(s))) if set(x) == set(s)]))
        
    
    


def main():
    sol = Solution()
    print(sol.removeDuplicateLetters('mitnlruhznjfyzmtmfnstsxwktxlboxutbic'))

if __name__=='__main__':
    main()