1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        num3 = sorted(nums1 + nums2)
4        numl = len(num3)
5        sum1 = 0
6
7        if numl % 2 != 0:
8            sum1 += num3[numl  // 2]
9        else:
10            sum1 += (num3[(numl//2)-1] + num3[numl//2])/2  
11
12
13
14        return sum1    
15        