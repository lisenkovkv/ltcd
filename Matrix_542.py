#https://leetcode.com/problems/01-matrix/
#array #dynamic_programming #BFS #matrix

from collections import deque

def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    DIR = [0, 1, 0, -1, 0]

    q = deque([])
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i + 1]
            if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
            mat[nr][nc] = mat[r][c] + 1
            q.append((nr, nc))
    return mat
#Runtime: 656 ms, faster than 61.68% of Python online submissions for 01 Matrix.
#Memory Usage: 15.9 MB, less than 93.30% of Python online submissions for 01 Matrix.
#Time: O(M * N), where M is number of rows, N is number of columns in the matrix.
#Space: O(M * N), space for the queue.