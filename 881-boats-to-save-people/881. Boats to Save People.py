class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        end = len(people) - 1
        start = 0
        ans = 0

        while start <= end:
            ans += 1
            if start == end:
                break
            elif people[end] + people[start] <= limit:
                start += 1
            end -= 1
                
        return ans 