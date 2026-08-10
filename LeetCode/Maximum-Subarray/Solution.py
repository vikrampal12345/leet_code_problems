1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        sum = 0
4        maximum = nums[0]
5        for i in nums:
6            sum += i
7            maximum = max(maximum, sum)
8
9            if sum < 0:
10                sum = 0
11                
12        return maximum        
13        