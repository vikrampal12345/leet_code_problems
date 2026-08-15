1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        n = 0
4        result = ""
5
6        for i in s:
7            if i == "(":
8                if n > 0:
9                    result += i
10                n += 1
11
12            else:
13                n -= 1
14                if n > 0:
15                    result += i  
16        return result            
17        
18        