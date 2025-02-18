#2375. Construct Smallest Number From DI String Feb-18/2025
class Solution(object):
    def smallestNumber(self, pattern):
        n = len(pattern)
        res=list(range(1, n+2))
        i = 0 
        while i < n:
            if pattern[i] =="D":
                start = i
                while i < n and pattern[i] =="D":
                    i += 1
                res[start:i+1] = reversed(res[start:i+1])
            else:
                i += 1
        return ''.join(map(str,res))