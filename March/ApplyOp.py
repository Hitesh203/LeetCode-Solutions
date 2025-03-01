#2460
class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        
        # Step 1: Apply operations to double equal adjacent values
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Move all zeros to the end while maintaining order
        non_zero_nums = [num for num in nums if num != 0]
        zero_count = nums.count(0)
        
        return non_zero_nums + [0] * zero_count