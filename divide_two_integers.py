"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

import time

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_VAL = 2147483647
        MIN_VAL = -2147483648
        
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        if divisor == 1:
            if sign>0:
                return min(dividend, MAX_VAL)
            else:
                return max(dividend, MIN_VAL)
        if divisor == -1:
            if sign>0:
                return min(-dividend,MAX_VAL)
            else:
                return max(-dividend,MIN_VAL)
        
        div = abs(dividend)
        sor = abs(divisor)
        
        tmp = 0
        global_factor = sign
        while div >= sor:
            tmp = sor
            local_factor = sign
            while div >= tmp:
                
                div -= tmp
                local_factor += local_factor
                tmp += tmp
            global_factor += local_factor-sign
            
            if abs(global_factor) >= MAX_VAL:
                break
            
        return global_factor-sign


def main():
    sol = Solution()
    start = time.time()
    print(sol.divide(7,3))
    print(time.time()-start)

if __name__=='__main__':
    main()