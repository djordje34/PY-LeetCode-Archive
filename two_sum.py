import numpy as np


class Solution(object):
    #napravi funkciju da vraca ind1 ind2 i da prekida list compreh
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=np.array(nums)
        for ind,x in enumerate(nums):
            y=target-x
            print(ind)
            if y in np.delete(nums,ind):
                ind2=np.where(nums==y)[0][0]
                if(ind!=ind2):
                    return(min(ind,ind2),max(ind,ind2))
        
        
        


def main():
    sol=Solution()
    print(sol.twoSum([3,3],6))

if __name__=='__main__':
    main()