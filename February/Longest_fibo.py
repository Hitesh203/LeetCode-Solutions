#873. Length of Longest Fibonacci Subsequence Feb-27/2025
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        dp = [[0] * n for i in range(n)]
        max_len = 0
        for current in range(2,n):
            start = 0
            end = current - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[current]:
                    end -=1
                elif pair_sum < arr[current]:
                    start += 1
                else:
                    dp[end][current] = dp[start][end] + 1
                    max_len = max(dp[end][current],max_len)
                    end -= 1
                    start += 1
        return max_len + 2 if max_len else 0