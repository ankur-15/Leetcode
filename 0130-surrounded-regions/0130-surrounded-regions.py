class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(i, j):
            # Base case: out of bounds, already visited, or 'X'
            if i < 0 or i >= m or j < 0 or j >= n or vis[i][j] or board[i][j] == 'X':
                return
            
            vis[i][j] = True
            
            # DFS on neighbors
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 1 & 2. DFS from boundary 'O's to mark unflippable regions
        # Left and Right borders
        for i in range(m):
            if board[i][0] == 'O' and not vis[i][0]:
                dfs(i, 0)
            if board[i][n - 1] == 'O' and not vis[i][n - 1]:
                dfs(i, n - 1)
        
        # Top and Bottom borders
        for j in range(n):
            if board[0][j] == 'O' and not vis[0][j]:
                dfs(0, j)
            if board[m - 1][j] == 'O' and not vis[m - 1][j]:
                dfs(m - 1, j)

        # 3. Flip surrounded 'O's
        for i in range(m):
            for j in range(n):
                # If 'O' is not visited, it means it's surrounded
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'