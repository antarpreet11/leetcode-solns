# Time - O(n), Space - O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        num = [0] * (len(s) + 1)
        num[-1] = 1


        i = len(s) - 1
        for i in range(len(s) - 1, -1, -1): 
            if s[i] == '0':
                num[i] = 0
            else:
                num[i] = num[i+1]

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                num[i] += num[i + 2]
        return num[0]
            
