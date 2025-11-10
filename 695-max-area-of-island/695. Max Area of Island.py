class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            if 0 <= row < m and 0 <= col < n:
                if grid[row][col] == 1:
                    return True
            return False

        def dfs(i, j):
            stack = [(i,j)]
            count = 1
            while stack:
                row, col = stack.pop()
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if valid(new_row,new_col) and (new_row, new_col) not in seen:
                        count += 1
                        seen.add((new_row,new_col))
                        stack.append((new_row,new_col)) 
            return count

        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        seen = set()
        area = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == 1:
                    seen.add((i,j))
                    count = dfs(i,j)
                    area = max(area, count)
        return area