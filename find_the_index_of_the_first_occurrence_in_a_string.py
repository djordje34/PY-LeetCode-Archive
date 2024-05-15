"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        """
        Fixed sliding window
        """
        if (nh:=len(haystack)) < (nl:=len(needle)):
            return -1
        
        for i in range(nh - nl + 1):
            if haystack[i : i+ nl] == needle:
                return i
        return -1
        
        
        
def main():
    sol = Solution()
    print(sol.strStr("leetcode","leeto"))

if __name__=='__main__':
    main()