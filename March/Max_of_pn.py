#2529. Maximum Count of Positive Integer and Negative Integer  -- March -12/2025
class Solution(object):
    def maximumCount(self, nums):
        pos = 0
        neg = 0
        for i in nums:
            if i < 0:
                neg+=1
            elif i >0:
                pos += 1
                
        return max(pos,neg)