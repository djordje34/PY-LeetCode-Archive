class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        
        newl=nums1+nums2
        newl.sort()
        if len(newl)==1:return newl[0]
        if not len(newl)%2:
            mid=float(newl[(len(newl)+1)//2])
            mid2=newl[(len(newl)-1)//2]
            fin= (mid+mid2)/2
        else:
            fin = newl[len(newl)//2]
        return fin



def main():
    sol=Solution()
    nums1=[1,2]
    nums2=[3]
    print(sol.findMedianSortedArrays(nums1,nums2))

if __name__=='__main__':
    main()