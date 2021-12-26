# https://leetcode.com/problems/reverse-string/
#two_pointers #string #recursive #recursion

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # Approach 1: Life is short, use Python
    #return(s.reverse())
    #Runtime: 243 ms, faster than 12.50% of Python online submissions for Reverse String.
    #Memory Usage: 21.3 MB, less than 31.40% of Python online submissions for Reverse String.
    
    # Approach 2: Recursion, In-Place, O(N) Space
    #def helper(left, right):
    #    if left < right:
    #        s[left], s[right] = s[right], s[left]
    #        helper(left + 1, right - 1)
#
    #helper(0, len(s) - 1)
    #return(s)
    #Runtime: 304 ms, faster than 5.04% of Python online submissions for Reverse String.
    #Memory Usage: 43.5 MB, less than 5.21% of Python online submissions for Reverse String.
    #Time complexity : O(N) time to perform N/2N/2 swaps.
    #Space complexity : O(N) to keep the recursion stack.
    
    #Approach 3: Two Pointers, Iteration, \mathcal{O}(1)O(1) Space
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return(s)
    #Runtime: 180 ms, faster than 36.15% of Python online submissions for Reverse String.
    #Memory Usage: 21.2 MB, less than 58.33% of Python online submissions for Reverse String.
    #Time complexity : O(N) to swap N/2 element.
    #Space complexity : O(1), it's a constant space solution.