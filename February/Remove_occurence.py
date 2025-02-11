#1910. Remove All Occurrences of a Substring Feb-11/2025
class Solution(object):
    def removeOccurrences(self, s, part):
        while part in s:
            part_start = s.find(part)

            s = s[:part_start] + s[part_start + len(part) :]
        return s