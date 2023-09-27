


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        print(nums)
        k = len(nums)
        p = 0
        b = len(nums)-1
        for i in range(len(nums)):
            print(f"{b},{p}")
            if nums[i]!=val:
                nums[p] = nums[i] 
                p+=1   
                
        for j in range(p,len(nums)):
            nums[j] = '_'
        return p
    


def main():
    sol = Solution()
    print(sol.removeElement([0,1,2,2,3,0,4,2],2))

if __name__=='__main__':
    main()