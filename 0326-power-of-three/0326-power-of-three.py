class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 0
        i = 0
        while 3**i <= n:
            if 3**i == n:
                num += i
            i +=1
        if 3**num == n:
            return True
        else:
            return False
                    
        