class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(t):
            if j == len(s):
                return True

            if s[j] == t[i]:
                j += 1
            i += 1

        return True if j == len(s) else False