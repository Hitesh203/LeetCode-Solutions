#3160. Find the Number of Distinct Colors Among the Balls  Feb-07/2025
class Solution(object):
    def queryResults(self, limit, queries):
        ball, color, ans, distinct = {}, {}, [], 0
        for pos, c in queries:
            if pos in ball:
                color[ball[pos]] -= 1
                if color[ball[pos]] == 0:
                    distinct -= 1
            ball[pos] = c
            color[c] = color.get(c, 0) + 1
            if color[c] == 1: distinct += 1
            ans.append(distinct)
        return ans
        