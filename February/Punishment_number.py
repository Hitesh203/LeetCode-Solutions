#2698. Find the Punishment Number of an Integer Feb-15/2025
class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_partition(num_str, target, index):
            if index == len(num_str):
                return target == 0
            
            current_sum = 0
            for i in range(index, len(num_str)):
                current_sum = current_sum * 10 + int(num_str[i])
                if current_sum > target:
                    break
                if can_partition(num_str, target - current_sum, i + 1):
                    return True
            return False
        
        punishment_sum = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(str(square), i, 0):
                punishment_sum += square
        
        return punishment_sum

        