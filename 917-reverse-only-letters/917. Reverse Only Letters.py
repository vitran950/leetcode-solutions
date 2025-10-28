class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left = 0
        right = len(ans) - 1

        while left < right:
            if not ans[left].isalpha():
                left += 1
                continue
            if not ans[right].isalpha():
                right -= 1
                continue
            
            ans[left], ans[right] = ans[right], ans[left]

            left += 1
            right -= 1
        
        return "".join(ans)