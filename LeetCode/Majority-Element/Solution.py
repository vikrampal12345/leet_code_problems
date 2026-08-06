1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        count = {}
4        for i in nums:
5            count[i] = count.get(i, 0) + 1
6            if len(nums)//2 < count[i]:
7                return i
8            