class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2: 
            temp = ""
            start = int(s[0])
            for i in range(1, len(s)):
                operated = (start + int(s[i])) % 10
                temp += str(operated)
                start = int(s[i])
            s = temp
        return s[0] == s[1] if len(s) == 2 else False