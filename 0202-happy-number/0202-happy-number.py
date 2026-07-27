class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 8 or n == 9:
            return False    
        n = str(n)
        
        sum = 0
        for i in n:
            sum += int(i)**2

        return  self.isHappy(sum)
        