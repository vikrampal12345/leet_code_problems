class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lis = []

        for i in nums:
            if i not in lis:
                lis.append(i)

        for i in range(len(lis)):
            nums[i] = lis[i]

        return len(lis)
        