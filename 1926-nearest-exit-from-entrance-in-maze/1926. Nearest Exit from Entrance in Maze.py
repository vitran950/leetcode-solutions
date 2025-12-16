from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbounds(row, col):
            if 0 <= row < m and 0 <= col < n:
                return True
            return False

        m = len(maze)
        n = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        seen = set((entrance[0], entrance[1]))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            row, col, steps = queue.popleft()
            if [row, col] != entrance and (row == 0 or col == 0 or row == m-1 or col == n-1):
                return steps
            
            for x, y in directions:
                new_x = row + x
                new_y = col + y
                if inbounds(new_x, new_y):
                    if maze[new_x][new_y] == "." and (new_x, new_y) not in seen:
                        seen.add((new_x, new_y))
                        queue.append((new_x, new_y, steps + 1))
        
        return -1