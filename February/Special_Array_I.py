#Problem No:3151 - Feb 01/2025
class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        else:
            for i in range(len(nums)-1):
                if nums[i] % 2 == nums[i+1] % 2:
                    return False
        return True
        