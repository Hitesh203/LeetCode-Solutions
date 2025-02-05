#1790. Check if One String Swap Can Make Strings Equal Feb-05/2025
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = 0
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count != 2:
            return False
        return True

        