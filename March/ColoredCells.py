#2579. Count Total Number of Colored Cells  Mar-05/2025
class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (2 * n**2) - (2*n) +1