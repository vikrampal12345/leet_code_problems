class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum= "".join(str(x) for x in digits)
        sum = int(sum) + 1
        lis = []
        while sum > 0 :
            digit = sum % 10
            lis.append(digit)
            sum //= 10
        lis.reverse()
        return lis