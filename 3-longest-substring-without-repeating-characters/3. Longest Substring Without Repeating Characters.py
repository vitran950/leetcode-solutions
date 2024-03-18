class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        ans = 0
        hash = set()
        for right in range(len(s)):
            while s[right] in hash:
                hash.remove(s[left])                    
                left += 1
            hash.add(s[right])
            ans = max(ans, right-left+1)
            
        return ans