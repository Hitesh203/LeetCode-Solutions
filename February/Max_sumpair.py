#2342. Max Sum of a Pair With Equal Sum of Digits Feb-12/2025
class Solution(object):
    def digitSum(self,num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    def maximumSum(self, nums):
        sumpairs = []
        max_pairs = -1
        for number in nums:
            digit_sum = self.digitSum(number)
            sumpairs.append((digit_sum,number))
        sumpairs.sort()
        for index in range(1,len(sumpairs)):
            current_digit_sum = sumpairs[index][0]
            previous_digit_sum = sumpairs[index - 1 ][0]
            if current_digit_sum == previous_digit_sum:
                current_sum=(sumpairs[index][1] + sumpairs[index -1][1])
                max_pairs = max(max_pairs,current_sum)
        return max_pairs