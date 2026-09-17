1
2class Solution:
3    def reversePairs(self, nums: list[int]) -> int:
4
5        def merge_sort(nums):
6            if len(nums) <= 1:
7                return nums, 0
8
9            mid = len(nums) // 2
10
11            left, c1 = merge_sort(nums[:mid])
12            right, c2 = merge_sort(nums[mid:])
13
14            count = c1 + c2
15
16            j = 0
17            for x in left:
18                while j < len(right) and x > 2 * right[j]:
19                    j += 1
20                count += j
21
22            i = 0
23            j = 0
24            result = []
25
26            while i < len(left) and j < len(right):
27                if left[i] <= right[j]:
28                    result.append(left[i])
29                    i += 1
30                else:
31                    result.append(right[j])
32                    j += 1
33
34            result.extend(left[i:])
35            result.extend(right[j:])
36
37            return result, count
38
39        return merge_sort(nums)[1]
40
41
42
43        