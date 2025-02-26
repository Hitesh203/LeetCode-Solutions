#1749. Maximum Absolute Sum of Any Subarray Feb-26/2025
class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = cur_max = 0
        min_sum = cur_min = 0
        
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            
        return max(abs(max_sum), abs(min_sum))

        