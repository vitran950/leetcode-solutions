class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        i, j = 0, len(s)-1
        while i < j and s[i] == s[j]:
            current = s[i]
            while s[i] == current and i < j:
                i += 1
            while s[j] == current and i <= j:
                j -= 1
            if j == i:
                return 1
        return j-i+1 if j-i > 0 else 0