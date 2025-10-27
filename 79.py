# Time - O(R * C * 4^L), Space - O(L), R - rows C - cols L - length of word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i: int, j: int, curr: int, visited: Set[Tuple[int, int]]) -> bool:
            if curr >= len(word):
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[curr]:
                return False

            visited.add((i, j))
            
            found = (
                dfs(i, j + 1, curr + 1, visited) or
                dfs(i, j - 1, curr + 1, visited) or
                dfs(i + 1, j, curr + 1, visited) or
                dfs(i - 1, j, curr + 1, visited)
            )

            visited.remove((i, j))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True
        return False
