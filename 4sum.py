"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
"""

class Solution(object):
    def fourSum(self, nums:list[int], target:int)->list[list[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = set()
        seen = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    last = target - nums[i] - nums[j] - nums[k]
                    if last in seen:
                        quad = tuple(sorted([nums[i],nums[j],nums[k],last]))
                        res.add(quad)
            seen.add(nums[i])
        return res
                        
    


def main():
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2],0))

if __name__=='__main__':
    main()
        
        