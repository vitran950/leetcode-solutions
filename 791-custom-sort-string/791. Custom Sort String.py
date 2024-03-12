from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        unique_s = defaultdict(int)
        for letter in s:
            unique_s[letter] += 1
        
        stack = []
        seen = set()
        i = len(order)-1
        while i >= 0:
            while order[i] in unique_s:
                stack.append(order[i])
                seen.add(order[i])
                unique_s[order[i]] -= 1
                if unique_s[order[i]] == 0:
                    del unique_s[order[i]]
            i -= 1

        result = ""
        for letter in s:
            if letter not in seen:
                result += letter
    
        while stack:
            result += stack.pop()

        return result

    

        