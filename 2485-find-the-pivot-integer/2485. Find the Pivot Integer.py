class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        temp_arr = []
        for i in range(n):
            temp_arr.append(i+1)
        
        prefix_sum = [temp_arr[0]]
        for i in range(1, len(temp_arr)):
            prefix_sum.append(temp_arr[i] + prefix_sum[i-1])

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == prefix_sum[n-1]-prefix_sum[i-1]:
                return i+1
        
        return -1