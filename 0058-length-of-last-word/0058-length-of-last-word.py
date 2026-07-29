class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lis = s.split()
        a = lis[-1]
        return len(a)