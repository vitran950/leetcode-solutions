class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        count = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count.append(i)
        
        if len(count) != 2:
            return False
        
        if s1[count[0]] != s2[count[1]] or s2[count[0]] != s1[count[1]]: 
            return False

        return True