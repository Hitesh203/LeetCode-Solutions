#1092.Shortest Common Supersequence -Feb-28/2025
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        m,n=len(str1),len(str2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1 , m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        result = []
        i,j = m,n
        while i > 0 or j > 0:
            if i >0 and j > 0 and str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif i > 0 and (j ==0 or dp[i][j] == dp[i-1][j]):
                result.append(str1[i-1])
                i-= 1
            else:
                result.append(str2[j-1])
                j -= 1
        return ''.join(result[::-1])
        