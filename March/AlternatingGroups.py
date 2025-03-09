#3208. Alternating Groups II  March-09/2025
class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        for i in range(k-1):
            colors.append(colors[i])
        l = len(colors)
        ans = 0
        left = 0
        right = 1
        while right < l:
            if colors[right] == colors[right -1]:
                left = right
                right += 1
                continue
            right += 1

            if right - left < k:
                continue
            
            ans += 1
            left += 1
        return ans
        