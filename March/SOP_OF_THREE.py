#1780. Check if Number is a Sum of Powers of Three   March-04/2025
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
        