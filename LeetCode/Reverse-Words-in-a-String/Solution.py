1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s = s.split()
4        s.reverse()
5        return " ".join(s)
6
7        