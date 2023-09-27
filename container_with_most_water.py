import time

class Solution:
    def maxArea1(self, height: list[int]) -> int:
        return max([min(x,y)*abs(i-j) for i,y in enumerate(height) for j,x in enumerate(height)])

    def maxArea(self, height:list[int]) -> int:
        max_area = 0
        l,r = 0, len(height) - 1
        while l < r:
            h_l, h_r = height[l], height[r]
            area = (r - l) * min(h_l, h_r)
            max_area = max(max_area, area)
            if h_l < h_r:
                l +=1
            else:
                r -= 1
        return max_area
    
    
def main():
    sol = Solution()
    start_time = time.time()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(f"{(time.time()-start_time):.12f}")
if __name__=='__main__':
    main()