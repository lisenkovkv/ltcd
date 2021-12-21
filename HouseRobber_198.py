# https://leetcode.com/problems/house-robber/
#array #dynamic_programming

#Approach 1: Dynamic Programming
def rob(nums):
        
        # Special handling for empty case.
    if not nums:
        return 0
        
    maxRobbedAmount = [None for _ in range(len(nums) + 1)]
    N = len(nums)
        
        # Base case initialization.
    maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
    for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
        maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
    return maxRobbedAmount[0]
#Runtime: 16 ms, faster than 82.16% of Python online submissions for House Robber.
#Memory Usage: 13.3 MB, less than 92.99% of Python online submissions for House Robber.
#Time Complexity: O(N)
#Space Complexity: O(N)