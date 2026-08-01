class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lis = []
        i = 0
        while i < len(word1) and i < len(word2):
            lis.append(word1[i])
            lis.append(word2[i])
            i +=1


        lis.extend(word1[i:])
        lis.extend(word2[i:])       
        return "".join(lis)     