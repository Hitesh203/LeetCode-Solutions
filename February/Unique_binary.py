#1980. Find Unique Binary String Feb-20/2025
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""
            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero
            return generate(curr + "1")
        n = len(nums)
        nums = set(nums)
        return generate("")
                
        