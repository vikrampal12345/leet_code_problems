class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        new_x = x[::-1]
        if x == new_x:
            return True
        else:
            return False    


        