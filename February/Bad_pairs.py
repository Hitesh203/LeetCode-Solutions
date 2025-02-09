# 2364. Count Number of Bad Pair  Feb 09/2025
from collections import defaultdict
class Solution(object):
    def countBadPairs(self, nums):
        total_pairs = len(nums) * (len(nums) -1) // 2
        count = defaultdict(int)
        good_pairs = 0
        for j , num in enumerate(nums):
            diff = num - j
            good_pairs += count[diff]
            count[diff] += 1
        return total_pairs - good_pairs