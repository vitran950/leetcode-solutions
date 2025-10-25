class Solution:
    def totalMoney(self, n: int) -> int:
        # get whole_num
        whole = floor(n/7)
        
        # get first half
        ans = 0 
        for i in range(whole):
            ans += 28 + (7*i)
        
        # get the remainder
        remainder = n % 7 
        for i in range(remainder):
            ans += (whole + i + 1)
        
        return ans
