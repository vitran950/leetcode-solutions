class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(num):
            room = rooms[num]
            for key in room:
                if key not in seen:
                    seen.add(key)
                    dfs(key)
        
        seen = set()
        seen.add(0)

        dfs(0)
        return len(seen) == len(rooms)