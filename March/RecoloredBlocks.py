#2379. Minimum Recolors to Get K Consecutive Black Blocks March-08/2025
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        current_count = blocks[:k].count('W')
        min_count = current_count

        for i in range(k,len(blocks)):
            if blocks[i - k ] == 'W':
                current_count -= 1
            if blocks[i] == "W":
                current_count += 1
            min_count = min(min_count,current_count)
        return min_count 
                
        