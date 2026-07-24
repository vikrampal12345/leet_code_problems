class Solution:
    def findComplement(self, num: int) -> int:
            lis = []
            while (num>0):
                digit = num%2
                num//=2
                lis.append(digit)

            lis.reverse()    
            
        
            new_lis = []
            for i in lis:
                if i == 0: 
                    new_lis.append(1)
                elif i == 1:
                    new_lis.append(0)
            
            new_lis.reverse()
            sum = 0
            for i in range(len(new_lis)):
                
                sum += new_lis[i]*(2**i)
            return sum 
       
        