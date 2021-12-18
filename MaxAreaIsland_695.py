#https://leetcode.com/problems/max-area-of-island/

def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    #Approach #1: Depth-First Search (Recursive)
    '''
    seen = set()
    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r+1, c) + area(r-1, c) +
                area(r, c-1) + area(r, c+1))

    return max(area(r, c)
                for r in range(len(grid))
                for c in range(len(grid[0])))
    '''
    #Runtime: 183 ms, faster than 17.77% of Python online submissions for Max Area of Island.
    #Memory Usage: 16.7 MB, less than 11.64% of Python online submissions for Max Area of Island.
    #Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.
    #Space complexity: O(R*C), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.
   
   #Approach #2: Depth-First Search (Iterative)
    seen = set()
    ans = 0
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                shape = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in seen):
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                ans = max(ans, shape)
    return ans
    #Runtime: 130 ms, faster than 53.22% of Python online submissions for Max Area of Island.
    #Memory Usage: 13.9 MB, less than 83.94% of Python online submissions for Max Area of Island.
    #Time Complexity: O(R*C), where R is the number of rows in the given grid, and CC is the number of columns. We visit every square once.
    #Space complexity: O(R*C), the space used by seen to keep track of visited squares, and the space used by stack.        