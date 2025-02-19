#1415. The k-th Lexicographical String of All Happy Strings of Length n Feb-19/2025 
class Solution(object):
    def getHappyString(self, n, k):
        happy_strings =[]
        def backtrack(current):
            if len(current) == n:
                happy_strings.append(current)
                return
            for character in ['a','b','c']:
                if not current or current[-1] != character:
                    backtrack(current + character)
        backtrack("")
        happy_strings.sort()
        if k <= len(happy_strings):
            return happy_strings[k -1]
        else:
            return ""
        