# https://leetcode.com/problems/climbing-stairs/
#math #dynamic_programming #memoization

def climbStairs(n):
    a = b = 1
    
    for _ in range(n):
        a,b = b, a+b
    return(a)

#Runtime: 20 ms, faster than 45.47% of Python online submissions for Climbing Stairs.
#Memory Usage: 13.5 MB, less than 12.43% of Python online submissions for Climbing Stairs.
#Time complexity : O(n)
#Space complexity : O(1)