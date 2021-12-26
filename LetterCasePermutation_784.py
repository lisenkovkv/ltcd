#https://leetcode.com/problems/letter-case-permutation/
#string #backtracking #bit_manipulation

def letterCasePermutation(s):
    #Approach #1: Recursion
    ans = [[]]
    
    for char in s:
        n = len(ans)
        if char.isalpha():
            for i in range(n):
                ans.append(ans[i][:])
                ans[i].append(char.lower())
                ans[n+i].append(char.upper())
                
        else:
            for i in range(n):
                ans[i].append(char)
    return(list(map(''.join, ans)).sort())

    #Runtime: 40 ms, faster than 86.41% of Python online submissions for Letter Case Permutation.
    #Memory Usage: 15 MB, less than 38.08% of Python online submissions for Letter Case Permutation.
    #Time Complexity: O(2^{N} * N)
    #Space Complexity: O(2^N * N)