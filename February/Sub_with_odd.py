#1524. Number of Sub-arrays With Odd Sum Feb-25/2025
class Solution(object):
    def numOfSubarrays(self, arr):
        odd_count = 0
        even_count = 1
        MOD = 10**9 + 7
        prefix_sum = 0
        result = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 ==0:
                even_count += 1
                result += odd_count
            else:
                odd_count += 1
                result += even_count
        return result % MOD  