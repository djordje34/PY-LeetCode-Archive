"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                current_diff = abs(target - current_sum)
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum       

def main():
    print(Solution().threeSumClosest([428,-119,561,445,772,-893,777,328,-941,-575,182,-103,1000,-481,915,881,-335,55,972,833,726,555,-434,635,122,-927,420,835,499,-760,928,-299,593,340,-88,392,744,16,65,661,-615,-116,704,925,183,7,-595,-714,-641,971,543,-167,119,715,-597,-871,281,810,911,156,27,735,815,-465,-900,416,-817,21,261,705,-644,187,275,223,617,-647,276,679,-173,-706,143,-764,891,-570,-478,-348,829,-845,-186,837,82,-256,983,696,408,413,857,346,-168,258,687,-738,352,-684,-779,-891,362,-793,-117,-381,-625,432,526,157,570,-861,-895,-789,-12,195,798,-106,-166,706,-129,-338,94,-382,-944,774,790,-177,267,-660,974,652,677,10,282,-45,-93,15,613,-688,-32,637,-835,-959,222,444,-189,169,-421,608,676,-6,-632,50,379,-133,909,-813,673,960,564,-243,-613,-247,954,-497,-594,-747,-929,135,-775,208,0,547,536,-589,993,-1,-768,87,251,-460,698,-614,-512,-507,795,-958,504,185,522,524,623,-553,868,-573,-432,-351,512,-525,-322,-163,-408,-274,217,310,-544,-890,605,-710,356,-769,205,746,45,186,728,775,-161,296,-749,611,421,-637,440,439,-907,-943,-730,171,-804,-806,573,598,-791,-681,377,365,329,877,311,83,436,-339,-916,-876,-389,958,-25,-842,773,-65,134,353,479,59,-231,943,-682,235,-510,-951,482,970,668,878,355,60,-519,-357,686,883,-794,289,-413,-375,265,568,-350,-49,545,319,-538,141,422,-875,25,-69,147,-860,-248,-221,847,-268,-987,104,-275,-753,466,866,-244,-499,-495,317,-19,-622,-588,341],8251))

if __name__=='__main__':
    main()