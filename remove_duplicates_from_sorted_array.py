class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
    


def main():
    sol = Solution()
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

if __name__=='__main__':
    main()