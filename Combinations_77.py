# https://leetcode.com/problems/combinations/
#array #backtracking

def combine(n,k):
    #Approach 1: Backtracking
    '''
    output = []
    def backtrack(first = 1, curr = []):
        if len(curr) == k:
            output.append(curr[:])
        for i in range(first, n+1):
            curr.append(i)
            backtrack(i+1, curr)
            curr.pop()
    
    backtrack()
    return(output)
    '''
    #Runtime: 468 ms, faster than 59.53% of Python3 online submissions for Combinations.
    #Memory Usage: 15.8 MB, less than 23.16% of Python3 online submissions for Combinations.
    #Time complexity : O(k C_N^k)
    #Space complexity : O(C_N^k)
    
    #Approach 2: Lexicographic (binary sorted) combinations
    
    nums = list(range(1,k+1)) + [n+1]
    
    output, j = [], 0
    
    while j<k:
        output.append(nums[:k])
        j=0
        while j<k and nums[j+1] == nums[j]+1:
            nums[j] = j+1
            j += 1
        nums[j] += 1
    
    return(output)
    #Runtime: 76 ms, faster than 97.16% of Python3 online submissions for Combinations.
    #Memory Usage: 15.6 MB, less than 93.29% of Python3 online submissions for Combinations.
    #Time complexity : O(k C_N^k)
    #Space complexity : O(C_N^k)