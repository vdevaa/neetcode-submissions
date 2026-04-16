class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(gridRows, gridCols):

            ## base cases
            if gridCols >= cols or gridCols < 0 or gridRows >= rows or gridRows < 0:
                return 0
            
            if grid[gridRows][gridCols] == "0":
                return 0
            
            # backtracking
            if grid[gridRows][gridCols] == "1":
                grid[gridRows][gridCols] = "0"

            ## recursive steps
            up = dfs(gridRows - 1, gridCols)
            down = dfs(gridRows + 1, gridCols)
            left = dfs(gridRows, gridCols - 1)
            right = dfs(gridRows, gridCols + 1)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        
        return res


