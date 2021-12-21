#https://leetcode.com/problems/triangle/
#array #dynamic_programming

import math
#Approach 1: Dynamic Programming
def minimumTotal(triangle):
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            smallest_above = math.inf
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])

#Runtime: 64 ms, faster than 82.12% of Python3 online submissions for Triangle.
#Memory Usage: 15 MB, less than 79.20% of Python3 online submissions for Triangle.
#Time Complexity: O(n^2)
#Space Complexity: O(1)