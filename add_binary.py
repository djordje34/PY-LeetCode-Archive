"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution(object):
    def addBinary(self, a:str, b:str):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        c = 0
        nc = max(len(a),len(b))
        a, b = a.rjust(nc, "0"), b.rjust(nc,"0")
        for i in range(len(a)-1,-1,-1):
            local_res=(int(a[i])+int(b[i])+c)
            modified_res = local_res%2
            res += str(modified_res)
            c = int(local_res > 1)
            print(res, c)

        if c:
            res += str(c)
        return res[::-1]
        
def main():
    Solution.addBinary(Solution, "11","1")

if __name__=='__main__':
    main()