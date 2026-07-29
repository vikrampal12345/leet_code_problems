class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        s = s[-1]
        return len(s)