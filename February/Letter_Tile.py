#1079.LETTER TILES POSSIBILITIES Feb-17/2025
from collections import Counter
class Solution(object):
    def numTilePossibilities(self, tiles):
        count = Counter(tiles)
        def dfs(counter):
            total = 0
            for letter in counter:
                if counter[letter] > 0:
                    total += 1
                    counter[letter] -= 1
                    total += dfs(counter)
                    counter[letter] += 1
            return total
        return dfs(count)
        