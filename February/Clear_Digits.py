#3174. Clear Digits  Feb 10/2025
class Solution(object):
    def clearDigits(self, s):
        result = []
        for i in range(len(s)):
            if s[i].isdigit():
                if result:
                    result.pop()
            else:
                result.append(s[i])
        return "".join(result)