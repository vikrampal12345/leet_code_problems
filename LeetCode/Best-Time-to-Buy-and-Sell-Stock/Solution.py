1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_no = prices[0]
4        max_no = 0
5
6        for i in prices:
7            min_no = min(min_no, i)
8            profit = i - min_no
9            max_no = max(max_no, profit)
10
11        return max_no
12
13        
14        