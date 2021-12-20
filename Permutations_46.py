#https://leetcode.com/problems/permutations/

def permute(nums):
    #Approach 1: Backtracking
    output = []
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first+1)
            nums[first], nums[i] = nums[i], nums[first]
        
    n = len(nums)
    backtrack()
    return(output)
    #Runtime: 24 ms, faster than 91.47% of Python online submissions for Permutations.
    #Memory Usage: 13.7 MB, less than 16.42% of Python online submissions for Permutations.
    #Time complexity : O(\sum_{k = 1}^{N}{P(N, k)})
    #Space complexity : O(N!)
    