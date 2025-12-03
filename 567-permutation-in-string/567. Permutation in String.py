from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        sorted_str = "".join(sorted(s1))
        n = len(sorted_str)
        curr = ""

        # get first characters first
        for i in range(n):
            curr += s2[i]

        if ''.join(sorted(curr)) == sorted_str:
            return True
        
        # start the rest of the iterations
        for right in range(n, len(s2)):
            curr = curr[1:] + s2[right]
            temp_curr = ''.join(sorted(curr))
            if temp_curr == sorted_str:
                return True
        
        return False
    