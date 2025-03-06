#2965. Find Missing and Repeated Values March-06/2025
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        count = [1] + [0] * len(grid)**2  
        for row in grid:
            for num in row:
                count[num] += 1
        return [count.index(2), count.index(0)] 