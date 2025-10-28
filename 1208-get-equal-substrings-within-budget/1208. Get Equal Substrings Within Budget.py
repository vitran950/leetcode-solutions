class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        curr = 0 
        ans = 0

        for right in range(len(s)):
            t_element = ord(t[right])
            s_element = ord(s[right])
            diff = abs(t_element - s_element)
            curr += diff

            while curr > maxCost:
                t_element = ord(t[left])
                s_element = ord(s[left])
                diff = abs(t_element - s_element)
                curr -= diff
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans