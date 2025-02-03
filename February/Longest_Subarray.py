#3105. Longest Strictly Increasing or Strictly Decreasing Subarray Feb-03/2025
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        inc=dec=max_length=1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                    inc+=1
                    dec =1
            elif nums[i] < nums[i+1]:
                    inc =1
                    dec+=1
            else:
                    inc=1
                    dec=1
               
            max_length=max(inc,dec,max_length)
        return max_length
