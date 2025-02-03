#1752. Check if Array Is Sorted and Rotated Feb-02/2025
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] :
                count+=1
        if nums[-1]> nums[0]:
            count +=1
        return count <= 1