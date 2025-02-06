#1726. Tuple with Same Product Feb-06/2025
from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        product_dictionary = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                product_dictionary[product] +=1
        for value in product_dictionary.values():
            answer += 4 * value * (value -1)
        return answer